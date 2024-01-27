using StopCorruption.Data.DbContexts;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;

namespace StopCorruption.Data.Repositries;

public class ChatMessageRepository : Repository<ChatMessage>, IChatMessageRepository
{
    public ChatMessageRepository(AppDbContext dbContext) : base(dbContext)
    {
    }
}
