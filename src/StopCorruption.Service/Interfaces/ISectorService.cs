using StopCorruption.Service.DTOs.Sectors;
using StopCorruption.Service.DTOs.Users;

namespace StopCorruption.Service.Interfaces;

public interface ISectorService
{
    Task<bool> RemoveAsync(long Id);
    Task<SectorForResultDto> RetrieveByIdAsync(long id);
    Task<IEnumerable<SectorForResultDto>> RetrieveAllAsync();
    Task<SectorForResultDto> AddAsync(SectorForCreationDto dto);
    Task<SectorForResultDto> ModifyAsync(long id, SectorForUpdateDto dto);
}
