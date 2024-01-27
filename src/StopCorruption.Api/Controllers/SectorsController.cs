using Microsoft.AspNetCore.Mvc;
using StopCorruption.Service.DTOs.Sectors;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Api.Controllers;

public class SectorsController : BaseController
{
    private readonly ISectorService _sectorService;

    public SectorsController(ISectorService sectorService)
    {
        _sectorService = sectorService;
    }


    [HttpPost]
    public async Task<IActionResult> PostAsync([FromBody] SectorForCreationDto dto)
        => Ok(await this._sectorService.AddAsync(dto));

    [HttpGet]
    public async Task<IActionResult> GetAllAsync()
        => Ok(await this._sectorService.RetrieveAllAsync());

    [HttpGet("{id}")]
    public async Task<IActionResult> GetAsync([FromRoute(Name = "id")] long id)
        => Ok(await this._sectorService.RetrieveByIdAsync(id));

    [HttpDelete("{id:long}")]
    public async Task<IActionResult> DeleteAsync([FromRoute(Name = "id")] long id)
        => Ok(await this._sectorService.RemoveAsync(id));

    [HttpPut("{id}")]
    public async Task<IActionResult> PutAsync([FromRoute(Name = "id")] long id, [FromBody] SectorForUpdateDto dto)
        => Ok(await this._sectorService.ModifyAsync(id, dto));
}
