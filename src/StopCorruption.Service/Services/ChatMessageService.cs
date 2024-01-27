using AutoMapper;
using Microsoft.EntityFrameworkCore;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;
using StopCorruption.Service.DTOs.ChatMessages;
using StopCorruption.Service.Exceptions;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Service.Services;

public class ChatMessageService : IChatMessageService
{
    private readonly IMapper _mapper;
    private readonly IChatMessageRepository _chatMessageRepository;

    public ChatMessageService(IMapper mapper, IChatMessageRepository chatMessageRepository)
    {
        _mapper = mapper;
        _chatMessageRepository = chatMessageRepository;
    }

    public async Task<ChatMessageForResultDto> AddAsync(ChatMessageForCreationDto dto)
    {
        var chat = await _chatMessageRepository.SelectAll()
            .Where(c => c.ApplicationId == dto.ApplicationId)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (chat is not null)
            throw new CorruptionException(400, "Chat already exists");

        var mappedUser = _mapper.Map<ChatMessage>(dto);
        mappedUser.CreatedAt = DateTime.UtcNow;
        var createdUser = await _chatMessageRepository.InsertAsync(mappedUser);

        return _mapper.Map<ChatMessageForResultDto>(createdUser);
    }

    public async Task<ChatMessageForResultDto> ModifyAsync(long id, ChatMessageForUpdateDto dto)
    {
        var user = await _chatMessageRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "Chat is not found");

        user.UpdatedAt = DateTime.UtcNow;
        var person = _mapper.Map(dto, user);
        await _chatMessageRepository.UpdateAsync(user);

        return _mapper.Map<ChatMessageForResultDto>(person);
    }

    public async Task<bool> RemoveAsync(long Id)
    {
        var user = await _chatMessageRepository.SelectAll()
            .Where(u => u.Id == Id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "User is not found");

        await _chatMessageRepository.DeleteAsync(Id);

        return true;
    }

    public async Task<IEnumerable<ChatMessageForResultDto>> RetrieveAllAsync()
    {
        var users = await _chatMessageRepository.SelectAll().ToListAsync();

        return _mapper.Map<IEnumerable<ChatMessageForResultDto>>(users);
    }

    public async Task<ChatMessageForResultDto> RetrieveByIdAsync(long id)
    {
        var user = await _chatMessageRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "User is not found");

        return _mapper.Map<ChatMessageForResultDto>(user);
    }
}
