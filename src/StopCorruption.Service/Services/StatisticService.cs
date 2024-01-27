using AutoMapper;
using Microsoft.EntityFrameworkCore;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;
using StopCorruption.Domain.Enums;
using StopCorruption.Service.DTOs.Statistics;
using StopCorruption.Service.Exceptions;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Service.Services;

public class StatisticService : IStatisticService
{
    private readonly IMapper _mapper;
    private readonly IStatisticRepository _repository;

    public StatisticService(IMapper mapper, IStatisticRepository repository)
    {
        _mapper = mapper;
        _repository = repository;
    }

    public async Task<StatisticForResultDto> AddAsync(StatisticForCreationDto dto)
    {
        var IsExistTelegramId = await _repository.SelectAll()
            .Where(t => t.Name.ToLower() == dto.Name.ToLower())
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (IsExistTelegramId is not null)
            throw new CorruptionException(400, "Name is already exist");

        var IsExistSectorId = await _repository.SelectAll()
            .Where(t => t.SectorId == dto.SectorId)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (IsExistSectorId is not null)
            throw new CorruptionException(400, "Sector is already exist");

        var mappedUser = _mapper.Map<Statistic>(dto);
        mappedUser.CreatedAt = DateTime.UtcNow;
        var createdUser = await _repository.InsertAsync(mappedUser);

        return _mapper.Map<StatisticForResultDto>(createdUser);
    }

    public async Task<StatisticForResultDto> ModifyAsync(long id, StatisticForUpdateDto dto)
    {
        var IsExistSectorId = await _repository.SelectAll()
            .Where(t => t.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (IsExistSectorId is null)
            throw new CorruptionException(400, "Statistic is already exist");

        IsExistSectorId.UpdatedAt = DateTime.UtcNow;
        var person = _mapper.Map(dto, IsExistSectorId);
        await _repository.UpdateAsync(IsExistSectorId);

        return _mapper.Map<StatisticForResultDto>(person);
    }

    public async Task<bool> RemoveAsync(long Id)
    {
        var user = await _repository.SelectAll()
            .Where(u => u.Id == Id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "User is not found");

        await _repository.DeleteAsync(Id);

        return true;
    }

    public async Task<IEnumerable<StatisticForResultDto>> RetrieveAllAsync()
    {
        var users = await _repository.SelectAll().ToListAsync();

        return _mapper.Map<IEnumerable<StatisticForResultDto>>(users);
    }

    public async Task<StatisticForResultDto> RetrieveByIdAsync(long id)
    {
        var user = await _repository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "Statistic is not found");

        return _mapper.Map<StatisticForResultDto>(user);
    }

}
