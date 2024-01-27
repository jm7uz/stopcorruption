using StopCorruption.Domain.Commons;
using StopCorruption.Domain.Enums;

namespace StopCorruption.Domain.Entities;

public class Application : Auditable
{
    public string Description { get; set; }
    public string Sector {  get; set; }
    public string OrganizationName { get; set; }
    public string NameOftheAccused { get; set; }
    public string DateSubmitted { get; set; }
    public string UserId { get; set; }
    public Status Status { get; set; }
    public string MediaPath { get; set; }
}
