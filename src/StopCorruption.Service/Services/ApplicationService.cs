using AutoMapper;
using Microsoft.EntityFrameworkCore;
using StopCorruption.Data.IRepositories;
using StopCorruption.Domain.Entities;
using StopCorruption.Service.DTOs.Applications;
using StopCorruption.Service.Exceptions;
using StopCorruption.Service.Interfaces;

namespace StopCorruption.Service.Services;

public class ApplicationService : IApplicationService
{
    private readonly IMapper _mapper;
    private readonly IApplicationRepository _applicationRepository;

    public ApplicationService(IMapper mapper,
        IApplicationRepository applicationRepository
        )
    {
        _mapper = mapper;
        _applicationRepository = applicationRepository;
    }

    public async Task<ApplicationForResultDto> AddAsync(ApplicationForCreationDto dto)
    {
        var mappedSectorName = _mapper.Map<Application>(dto);
        mappedSectorName.CreatedAt = DateTime.UtcNow;
        var createdUser = await _applicationRepository.InsertAsync(mappedSectorName);

        return _mapper.Map<ApplicationForResultDto>(createdUser);
    }

    public async Task<ApplicationForResultDto> ModifyAsync(long id, ApplicationForUpdateDto dto)
    {
        var sector = await _applicationRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (sector is null)
            throw new CorruptionException(404, "Application is not found");

        sector.UpdatedAt = DateTime.UtcNow;
        var category = _mapper.Map(dto, sector);
        await _applicationRepository.UpdateAsync(sector);

        return _mapper.Map<ApplicationForResultDto>(category);
    }

    public async Task<bool> RemoveAsync(long Id)
    {
        var user = await _applicationRepository.SelectAll()
            .Where(u => u.Id == Id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "Application is not found");

        await _applicationRepository.DeleteAsync(Id);

        return true;
    }

    public async Task<IEnumerable<ApplicationForResultDto>> RetrieveAllAsync()
    {
        var users = await _applicationRepository.SelectAll().ToListAsync();

        return _mapper.Map<IEnumerable<ApplicationForResultDto>>(users);
    }

    public async Task<ApplicationForResultDto> RetrieveByIdAsync(long id)
    {
        var user = await _applicationRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (user is null)
            throw new CorruptionException(404, "Application is not found");

        return _mapper.Map<ApplicationForResultDto>(user);
    }
}
