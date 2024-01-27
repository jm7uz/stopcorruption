using StopCorruption.Service.DTOs.Applications;
using StopCorruption.Service.DTOs.Users;

namespace StopCorruption.Service.Interfaces;

public interface IApplicationService
{
    Task<bool> RemoveAsync(long Id);
    Task<ApplicationForResultDto> RetrieveByIdAsync(long id);
    Task<IEnumerable<ApplicationForResultDto>> RetrieveAllAsync();
    Task<ApplicationForResultDto> AddAsync(ApplicationForCreationDto dto);
    Task<ApplicationForResultDto> ModifyAsync(long id, ApplicationForUpdateDto dto);
}
