using StopCorruption.Domain.Enums;
using StopCorruption.Service.DTOs.Sectors;

namespace StopCorruption.Service.DTOs.Applications;

public class ApplicationForResultDto
{
    public long Id { get; set; }
    public string Description { get; set; }
    public string SectorId { get; set; }
    public SectorForResultDto Sector { get; set; }
    public string OrganizationName { get; set; }
    public string NameOftheAccused { get; set; }
    public string DateSubmitted { get; set; }
    public string UserId { get; set; }
    public Status Status { get; set; }
    public string MediaPath { get; set; }
}
