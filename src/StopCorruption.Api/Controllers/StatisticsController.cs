using Microsoft.AspNetCore.Mvc;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Api.Controllers;

public class StatisticController : BaseController
{
    private readonly IStatisticService _statisticService;

    public StatisticController(IStatisticService stasticService)
    {
        _statisticService = stasticService;
    }
    [HttpGet]
    public async Task<IActionResult> GetAllAsync()
        => Ok(await _statisticService.GetApplicationStatistics());
}
