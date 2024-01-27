using StopCorruption.Data.DbContexts;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;

namespace StopCorruption.Data.Repositries;

public class UserRepository : Repository<User>, IUserRepository
{
    public UserRepository(AppDbContext dbContext) : base(dbContext)
    {
    }
}
