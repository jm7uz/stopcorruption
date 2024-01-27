namespace StopCorruption.Service.DTOs.ChatMessages;

public class ChatMessageForResultDto
{
    public long Id { get; set; }
    public long SenderUserId { get; set; }
    public string MediaPath { get; set; }
    public DateTime SendDate { get; set; }
    public string Content { get; set; }
    public long ApplicationId { get; set; }
}
