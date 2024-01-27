using StopCorruption.Domain.Enums;
using StopCorruption.Service.DTOs.Sectors;

namespace StopCorruption.Service.DTOs.Applications;

public class ApplicationForResultDto
{
    public long Id { get; set; }
    public string Description { get; set; }
    public long SectorId { get; set; }
    public string OrganizationName { get; set; }
    public string NameOftheAccused { get; set; }
    public DateTime DateSubmitted { get; set; }
    public long UserId { get; set; }
    public Status Status { get; set; }
    public string? MediaPath { get; set; }
}
