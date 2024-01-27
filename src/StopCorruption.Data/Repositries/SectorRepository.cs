using StopCorruption.Data.DbContexts;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;

namespace StopCorruption.Data.Repositries;

public class SectorRepository : Repository<Sector>, ISectorRepository
{
    public SectorRepository(AppDbContext dbContext) : base(dbContext)
    {
    }
}
