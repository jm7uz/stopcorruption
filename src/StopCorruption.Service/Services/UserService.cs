using StopCorruption.Service.DTOs.Users;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Service.Services;

public class UserService : IUserService
{
    public Task<UserForResultDto> AddAsync(UserForCreationDto dto)
    {
        throw new NotImplementedException();
    }

    public Task<UserForResultDto> ModifyAsync(long id, UserForUpdateDto dto)
    {
        throw new NotImplementedException();
    }

    public Task<bool> RemoveAsync(long Id)
    {
        throw new NotImplementedException();
    }

    public Task<IEnumerable<UserForResultDto>> RetrieveAllAsync()
    {
        throw new NotImplementedException();
    }

    public Task<UserForResultDto> RetrieveByIdAsync(long id)
    {
        throw new NotImplementedException();
    }
}
