using AutoMapper;
using Microsoft.EntityFrameworkCore;
using StopCorruption.Data.IRepositories;
using StopCorruption.Data.Repositries;
using StopCorruption.Domain.Entities;
using StopCorruption.Service.DTOs.Sectors;
using StopCorruption.Service.DTOs.Users;
using StopCorruption.Service.Exceptions;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Service.Services;

public class SectorService : ISectorService
{
    private readonly IMapper _mapper;
    private readonly ISectorRepository _sectorRepository;

    public SectorService(IMapper mapper, ISectorRepository sectorRepository)
    {
        _mapper = mapper;
        _sectorRepository = sectorRepository;
    }

    public async Task<SectorForResultDto> AddAsync(SectorForCreationDto dto)
    {
        var IsExistSectorName = await _sectorRepository.SelectAll()
            .Where(s => s.Name.ToLower() == dto.Name.ToLower())
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (IsExistSectorName is not null)
            throw new CorruptionException(400, "Sector is already exist");

        var mappedSectorName = _mapper.Map<Sector>(dto);
        mappedSectorName.CreatedAt = DateTime.UtcNow;
        var createdUser = await _sectorRepository.InsertAsync(mappedSectorName);

        return _mapper.Map<SectorForResultDto>(createdUser);
    }

    public async Task<SectorForResultDto> ModifyAsync(long id, SectorForUpdateDto dto)
    {
        var sector = await _sectorRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (sector is null)
            throw new CorruptionException(404, "User is not found");

        sector.UpdatedAt = DateTime.UtcNow;
        var category = _mapper.Map(dto, sector);
        await _sectorRepository.UpdateAsync(sector);

        return _mapper.Map<SectorForResultDto>(category);
    }

    public async Task<bool> RemoveAsync(long Id)
    {
        var sector = await _sectorRepository.SelectAll()
            .Where(u => u.Id == Id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (sector is null)
            throw new CorruptionException(404, "User is not found");

        await _sectorRepository.DeleteAsync(Id);
        return true;
    }

    public async Task<IEnumerable<SectorForResultDto>> RetrieveAllAsync()
    {
        var sectors = await _sectorRepository.SelectAll().ToListAsync();

        return _mapper.Map<IEnumerable<SectorForResultDto>>(sectors);
    }

    public async Task<SectorForResultDto> RetrieveByIdAsync(long id)
    {
        var SectorById = await _sectorRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (SectorById is null)
            throw new CorruptionException(404, "User is not found");

        return _mapper.Map<SectorForResultDto>(SectorById);
    }
}
