using StopCorruption.Service.DTOs.Applications;

namespace StopCorruption.Service.DTOs.Users;

public class UserForResultDto
{
    public long Id { get; set; }
    public bool IsOneID { get; set; }
    public string OneID { get; set; }
    public long TelegramId { get; set; }
    public ICollection<ApplicationForResultDto> Application { get; set; }
}
