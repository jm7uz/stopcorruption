using StopCorruption.Data.DbContexts;
using StopCorruption.Domain.Entities;

namespace StopCorruption.Data.Repositries;

public class StatisticRepository : Repository<Statistic>
{
    public StatisticRepository(AppDbContext dbContext) : base(dbContext)
    {
    }
}
