using StopCorruption.Service.DTOs;
using StopCorruption.Services;

namespace StopCorruption.Service.Interfaces
{
    public interface IStatisticService
    {
        public Task<StatisticSummary> GetApplicationStatistics();
    }
}
