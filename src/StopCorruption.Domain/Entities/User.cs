using StopCorruption.Domain.Commons;
using System.Text.Json.Serialization;

namespace StopCorruption.Domain.Entities;

public class User : Auditable
{
    public bool IsOneID { get; set; }
    public string OneID {  get; set; }
    public long TelegramId { get; set; }
    [JsonIgnore]
    public ICollection<Application> Applications { get; set; }
}
