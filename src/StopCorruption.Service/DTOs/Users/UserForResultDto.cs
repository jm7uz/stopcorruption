using StopCorruption.Service.DTOs.Applications;

namespace StopCorruption.Service.DTOs.Users;

public class UserForResultDto
{
    public long Id { get; set; }
    public bool IsOneID { get; set; }
    public long TelegramId { get; set; }
    public string FullName { get; set; }
    public string PermitAddress { get; set; }
    public string Phone { get; set; }
    public string Language { get; set; }
    public string passportNumber { get; set; }
    public string passportIssuedBy { get; set; }
    public ICollection<ApplicationForResultDto> Application { get; set; }
}
