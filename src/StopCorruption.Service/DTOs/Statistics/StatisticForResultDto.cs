using StopCorruption.Service.DTOs.Applications;

namespace StopCorruption.Service.DTOs.Statistics;

public class StatisticForResultDto
{
    public long Id { get; set; }
    public string Name { get; set; }
    public float CurruptionValue { get; set; }
    public DateTime Date { get; set; }
    public string Period { get; set; }
    public string Sector { get; set; }
    public string Location { get; set; }
    public string CorruptionType { get; set; }
    public string InvestigationOutcome { get; set; }

    public ICollection<ApplicationForResultDto> ApplicationForResult { get; set; }
}
