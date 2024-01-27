using StopCorruption.Domain.Commons;
using StopCorruption.Domain.Enums;

namespace StopCorruption.Domain.Entities;

public class Statistic : Auditable
{
    public string Name { get; set; }
    public float CurruptionValue { get; set; }
    public DateTime Date { get; set; }
    public PeriodType PeriodType { get; set; }
    public long SectorId {  get; set; }
    public Sector Sector { get; set; }
    public Region? Region { get; set; }
    public string? District { get; set; }
    public string latitude { get; set; }
    public string longitude { get; set; }
    public string InvestigationOutcome { get; set; }
    
    public ICollection<Application> Applications { get; set; }
}
