using StopCorruption.Domain.Commons;

namespace StopCorruption.Domain.Entities;

public class Statistics : Auditable
{
    public string Name { get; set; }
    public float CurruptionValue { get; set; }
    public DateTime Date { get; set; }
    public string Period { get; set; }
    public string Sector {  get; set; }
    public string Location { get; set; }
    public string CorruptionType { get; set; }
    public string InvestigationOutcome { get; set; }
    
    public ICollection<Application> Application { get; set; }
}
