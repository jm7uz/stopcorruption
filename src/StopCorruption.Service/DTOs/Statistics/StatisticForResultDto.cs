﻿using StopCorruption.Service.DTOs.Applications;

namespace StopCorruption.Service.DTOs.Statistics;

public class StatisticForResultDto
{
    public long Id { get; set; }
    public string Name { get; set; }
    public float CurruptionValue { get; set; }
    public DateTime Date { get; set; }
    public string Period { get; set; }
    public long SectorId { get; set; }
    public string latitude { get; set; }
    public string longitude { get; set; }
    public string InvestigationOutcome { get; set; }

    public ICollection<ApplicationForResultDto> ApplicationForResult { get; set; }
}
