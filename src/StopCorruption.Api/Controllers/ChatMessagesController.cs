using Microsoft.AspNetCore.Mvc;
using StopCorruption.Service.DTOs.ChatMessages;
using StopCorruption.Service.DTOs.Sectors;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Api.Controllers;

public class ChatMessagesController : BaseController
{
    private readonly IChatMessageService _chatMessageService;

    public ChatMessagesController(IChatMessageService chatMessageService)
    {
        _chatMessageService = chatMessageService;
    }

    [HttpPost]
    public async Task<IActionResult> PostAsync([FromBody] ChatMessageForCreationDto dto)
        => Ok(await this._chatMessageService.AddAsync(dto));

    [HttpGet]
    public async Task<IActionResult> GetAllAsync()
        => Ok(await this._chatMessageService.RetrieveAllAsync());

    [HttpGet("{id}")]
    public async Task<IActionResult> GetAsync([FromRoute(Name = "id")] long id)
        => Ok(await this._chatMessageService.RetrieveByIdAsync(id));

    [HttpDelete("{id:long}")]
    public async Task<IActionResult> DeleteAsync([FromRoute(Name = "id")] long id)
        => Ok(await this._chatMessageService.RemoveAsync(id));

    [HttpPut("{id}")]
    public async Task<IActionResult> PutAsync([FromRoute(Name = "id")] long id, [FromBody] ChatMessageForUpdateDto dto)
        => Ok(await this._chatMessageService.ModifyAsync(id, dto));
}
