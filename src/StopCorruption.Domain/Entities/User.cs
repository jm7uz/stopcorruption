using StopCorruption.Domain.Commons;
using System.Text.Json.Serialization;

namespace StopCorruption.Domain.Entities;

public class User : Auditable
{
    public bool IsOneID { get; set; }
    public long TelegramId { get; set; }
    public string FullName { get; set; }
    public string PermitAddress { get; set; }
    public string Phone { get; set; }
    public string Language { get; set; }
    public string passportNumber { get; set; }
    public string passportIssuedBy { get; set; }

    [JsonIgnore]
    public ICollection<Application> Applications { get; set; }
}
