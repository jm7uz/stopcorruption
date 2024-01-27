using StopCorruption.Service.DTOs.ChatMessages;

namespace StopCorruption.Service.Interfaces;

public interface IChatMessageService
{
    Task<bool> RemoveAsync(long Id);
    Task<ChatMessageForResultDto> RetrieveByIdAsync(long id);
    Task<IEnumerable<ChatMessageForResultDto>> RetrieveAllAsync();
    Task<ChatMessageForResultDto> AddAsync(ChatMessageForCreationDto dto);
    Task<ChatMessageForResultDto> ModifyAsync(long id, ChatMessageForUpdateDto dto);
}
