using StopCorruption.Data.DbContexts;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;

namespace StopCorruption.Data.Repositries;

public class ApplicationRepository : Repository<Application>, IApplicationRepository
{
    public ApplicationRepository(AppDbContext dbContext) : base(dbContext)
    {
    }
}
