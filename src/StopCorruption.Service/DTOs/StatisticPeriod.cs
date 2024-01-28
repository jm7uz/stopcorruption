using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StopCorruption.Service.DTOs
{
    public class StatisticPeriod
    {
        public int MonthlyApplications { get; set; }
        public int WeeklyApplications { get; set; }
        public int QuarterlyApplications { get; set; }
        public int YearlyApplications { get; set; }
    }
}
