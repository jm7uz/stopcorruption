using StopCorruption.Data.DbContexts;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;

namespace StopCorruption.Data.Repositries;

public class StatisticRepository : Repository<Statistic>, IStatisticRepository
{
    public StatisticRepository(AppDbContext dbContext) : base(dbContext)
    {
    }
}
