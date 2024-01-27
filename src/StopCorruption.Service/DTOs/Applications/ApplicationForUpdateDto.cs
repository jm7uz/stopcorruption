using StopCorruption.Domain.Enums;

namespace StopCorruption.Service.DTOs.Applications;

public class ApplicationForUpdateDto
{
    public string Description { get; set; }
    public string SectorId { get; set; }
    public string OrganizationName { get; set; }
    public string NameOftheAccused { get; set; }
    public string DateSubmitted { get; set; }
    public string UserId { get; set; }
    public Status Status { get; set; }
    public string MediaPath { get; set; }
}
