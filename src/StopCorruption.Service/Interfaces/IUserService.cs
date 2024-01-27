using StopCorruption.Service.DTOs.Users;

namespace StopCorruption.Service.Interfaces;

public interface IUserService
{
    Task<bool> RemoveAsync(long Id);
    Task<UserForResultDto> RetrieveByIdAsync(long id);
    Task<IEnumerable<UserForResultDto>> RetrieveAllAsync();
    Task<UserForResultDto> AddAsync(UserForCreationDto dto);
    Task<UserForResultDto> ModifyAsync(long id, UserForUpdateDto dto);
}
