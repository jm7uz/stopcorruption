using Microsoft.AspNetCore.Mvc;
using StopCorruption.Service.DTOs.Statistics;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Api.Controllers;

public class StatisticsController : BaseController
{
    private readonly IStatisticService _statisticService;

    public StatisticsController(IStatisticService statisticService)
    {
        _statisticService = statisticService;
    }

    [HttpPost]
    public async Task<IActionResult> PostAsync([FromBody] StatisticForCreationDto dto)
        => Ok(await this._statisticService.AddAsync(dto));

    [HttpGet]
    public async Task<IActionResult> GetAllAsync()
        => Ok(await this._statisticService.RetrieveAllAsync());

    [HttpGet("{id}")]
    public async Task<IActionResult> GetAsync([FromRoute(Name = "id")] long id)
        => Ok(await this._statisticService.RetrieveByIdAsync(id));

    [HttpDelete("{id:long}")]
    public async Task<IActionResult> DeleteAsync([FromRoute(Name = "id")] long id)
        => Ok(await this._statisticService.RemoveAsync(id));

    [HttpPut("{id}")]
    public async Task<IActionResult> PutAsync([FromRoute(Name = "id")] long id, [FromBody] StatisticForUpdateDto dto)
        => Ok(await this._statisticService.ModifyAsync(id, dto));
}
