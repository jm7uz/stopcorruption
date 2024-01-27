using StopCorruption.Domain.Commons;

namespace StopCorruption.Domain.Entities;

public class ChatMessage : Auditable
{
    public long FromId { get; set; }
    public string? MediaPath { get; set; }
    public DateTime SendDate { get; set; } 
    public string Content { get; set; }
    public long ApplicationId { get; set; }
}
