using StopCorruption.Domain.Enums;

namespace StopCorruption.Service.DTOs.Statistics;

public class StatisticForUpdateDto
{
    public string Name { get; set; }
    public float CurruptionValue { get; set; }
    public DateTime Date { get; set; }
    public PeriodType PeriodType { get; set; }
    public long SectorId { get; set; }
    public Region? Region { get; set; }
    public string? District { get; set; }
    public string latitude { get; set; }
    public string longitude { get; set; }
    public string InvestigationOutcome { get; set; }
}
