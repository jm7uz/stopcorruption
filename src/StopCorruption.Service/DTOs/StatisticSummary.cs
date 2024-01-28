using StopCorruption.Services;

namespace StopCorruption.Service.DTOs
{
    public class StatisticSummary
    {
        public int TotalApplications { get; set; }
        public int ApprovedApplications { get; set; }
        public int RejectedApplications { get; set; }
        public int InprocessApplications { get; set; }
        public int SubmittedApplications { get; set; }
        public StatisticPeriod PeriodStatistics { get; set; }
    }

}
