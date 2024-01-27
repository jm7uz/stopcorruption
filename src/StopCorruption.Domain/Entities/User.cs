using StopCorruption.Domain.Commons;

namespace StopCorruption.Domain.Entities;

public class User : Auditable
{
    public bool IsOneID { get; set; }
    public long OneID {  get; set; }
    public long TelegramId { get; set; }
    
}
