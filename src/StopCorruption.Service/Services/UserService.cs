using AutoMapper;
using Microsoft.EntityFrameworkCore;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;
using StopCorruption.Service.DTOs.Users;
using StopCorruption.Service.Exceptions;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Service.Services;

public class UserService : IUserService
{
    private readonly IMapper _mapper;
    private readonly IUserRepository _userRepository;
    public UserService(IMapper mapper, IUserRepository userRepository)
    {
        _mapper = mapper;
        _userRepository = userRepository;
    }

    public async Task<UserForResultDto> AddAsync(UserForCreationDto dto)
    {
        var IsExistTelegramId = await _userRepository.SelectAll()
            .Where(t => t.TelegramId == dto.TelegramId)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (IsExistTelegramId is not null)
            throw new CorruptionException(400, "User is already exist");

        var mappedUser = _mapper.Map<User>(dto);
        mappedUser.CreatedAt = DateTime.UtcNow;
        var createdUser = await _userRepository.InsertAsync(mappedUser);

        return _mapper.Map<UserForResultDto>(createdUser);

    }

    public async Task<UserForResultDto> ModifyAsync(long id, UserForUpdateDto dto)
    {
        var user = await _userRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "User is not found");

        user.UpdatedAt = DateTime.UtcNow;   
        var person = _mapper.Map(dto, user);
        await _userRepository.UpdateAsync(user);

        return _mapper.Map<UserForResultDto>(person);
    }

    public async Task<bool> RemoveAsync(long Id)
    {
        var user = await _userRepository.SelectAll()
            .Where(u => u.Id == Id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "User is not found");

        await _userRepository.DeleteAsync(Id);
        
        return true;
    }

    public async Task<IEnumerable<UserForResultDto>> RetrieveAllAsync()
    {
        var users = await _userRepository.SelectAll().ToListAsync();

        return _mapper.Map<IEnumerable<UserForResultDto>>(users);
    }

    public async Task<UserForResultDto> RetrieveByIdAsync(long id)
    {
        var user = await _userRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "User is not found");

        return _mapper.Map<UserForResultDto>(user);
    }
}
