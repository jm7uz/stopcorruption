using StopCorruption.Domain.Enums;

namespace StopCorruption.Service.DTOs.Applications;

public class ApplicationForCreationDto
{
    public string Description { get; set; }
    public long SectorId { get; set; }
    public string OrganizationName { get; set; }
    public string NameOftheAccused { get; set; }
    public DateTime DateSubmitted { get; set; }
    public long UserId { get; set; }
    public Status Status { get; set; }
    public string MediaPath { get; set; }
}
