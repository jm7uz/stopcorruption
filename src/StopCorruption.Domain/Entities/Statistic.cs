using StopCorruption.Domain.Commons;

namespace StopCorruption.Domain.Entities;

public class Statistic : Auditable
{
    public string Name { get; set; }
    public float CurruptionValue { get; set; }
    public DateTime Date { get; set; }
    public string Period { get; set; }
    public long SectorId {  get; set; }
    public Sector Sector { get; set; }
    public string Location { get; set; }
    public string CorruptionType { get; set; }
    public string InvestigationOutcome { get; set; }
    
    public ICollection<Application> Application { get; set; }
}
