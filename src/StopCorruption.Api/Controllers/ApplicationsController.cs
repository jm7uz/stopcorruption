using Microsoft.AspNetCore.Mvc;
using StopCorruption.Service.DTOs.Applications;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Api.Controllers;

public class ApplicationsController : BaseController
{
    private readonly IApplicationService _applicationService;

    public ApplicationsController(IApplicationService applicationService)
    {
        _applicationService = applicationService;
    }

    [HttpPost]
    public async Task<IActionResult> PostAsync([FromBody] ApplicationForCreationDto dto)
        => Ok(await this._applicationService.AddAsync(dto));

    [HttpGet]
    public async Task<IActionResult> GetAllAsync()
        => Ok(await this._applicationService.RetrieveAllAsync());

    [HttpGet("{id}")]
    public async Task<IActionResult> GetAsync([FromRoute(Name = "id")] long id)
        => Ok(await this._applicationService.RetrieveByIdAsync(id));

    [HttpDelete("{id:long}")]
    public async Task<IActionResult> DeleteAsync([FromRoute(Name = "id")] long id)
        => Ok(await this._applicationService.RemoveAsync(id));

    [HttpPut("{id}")]
    public async Task<IActionResult> PutAsync([FromRoute(Name = "id")] long id, [FromBody] ApplicationForUpdateDto dto)
        => Ok(await this._applicationService.ModifyAsync(id, dto));
}
