using Microsoft.EntityFrameworkCore;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Enums;
using StopCorruption.Service.DTOs;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Services
{
    public class StatisticService : IStatisticService
    {
        private readonly IApplicationRepository _applicationRepository;

        public StatisticService(IApplicationRepository applicationRepository)
        {
            _applicationRepository = applicationRepository ?? throw new ArgumentNullException(nameof(applicationRepository));
        }

        public async Task<StatisticSummary> GetApplicationStatistics()
        {
            var applications = await _applicationRepository.SelectAll().ToListAsync();

            var totalApplications = applications.Count();
            var approvedApplications = applications.Count(a => a.Status == Status.Success);
            var rejectedApplications = applications.Count(a => a.Status == Status.Rejected);
            var inprocessApplications = applications.Count(a => a.Status == Status.Inprocces);
            var submittedApplications = applications.Count(a => a.Status == Status.Submitted);

            var monthlyApplications = applications.Count(a => a.PeriodType == PeriodType.monthly);
            var weeklyApplications = applications.Count(a => a.PeriodType == PeriodType.weekly);
            var quarterlyApplications = applications.Count(a => a.PeriodType == PeriodType.quarterly);
            var yearlyApplications = applications.Count(a => a.PeriodType == PeriodType.yearly);

            var statisticSummary = new StatisticSummary
            {
                TotalApplications = totalApplications,
                ApprovedApplications = approvedApplications,
                RejectedApplications = rejectedApplications,
                InprocessApplications = inprocessApplications,
                SubmittedApplications = submittedApplications,
                PeriodStatistics = new StatisticPeriod
                {
                    MonthlyApplications = monthlyApplications,
                    WeeklyApplications = weeklyApplications,
                    QuarterlyApplications = quarterlyApplications,
                    YearlyApplications = yearlyApplications
                }
            };

            return statisticSummary;
        }
    }

    
}
