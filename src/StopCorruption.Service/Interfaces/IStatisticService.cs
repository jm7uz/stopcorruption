using StopCorruption.Domain.Enums;
using StopCorruption.Service.DTOs.Sectors;
using StopCorruption.Service.DTOs.Statistics;

namespace StopCorruption.Service.Interfaces;

public interface IStatisticService
{
    Task<bool> RemoveAsync(long Id);
    Task<StatisticForResultDto> RetrieveByIdAsync(long id);
    Task<IEnumerable<StatisticForResultDto>> RetrieveAllAsync();
    Task<StatisticForResultDto> AddAsync(StatisticForCreationDto dto);
    Task<StatisticForResultDto> ModifyAsync(long id, StatisticForUpdateDto dto);
}
