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

    public ApplicationService(IMapper mapper, IApplicationRepository applicationRepository)
    {
        _mapper = mapper;
        _applicationRepository = applicationRepository;
    }

    public async Task<ApplicationForResultDto> AddAsync(ApplicationForCreationDto dto)
    {
        var mappedApplication = _mapper.Map<Application>(dto);
        mappedApplication.CreatedAt = DateTime.UtcNow;
        var createdApplication = await _applicationRepository.InsertAsync(mappedApplication);

        return _mapper.Map<ApplicationForResultDto>(createdApplication);
    }

    public async Task<ApplicationForResultDto> ModifyAsync(long id, ApplicationForUpdateDto dto)
    {
        var application = await _applicationRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (application is null)
            throw new CorruptionException(404, "User is not found");

        application.UpdatedAt = DateTime.UtcNow;
        var applicant = _mapper.Map(dto, application);
        await _applicationRepository.UpdateAsync(application);

        return _mapper.Map<ApplicationForResultDto>(applicant);
    }

    public async Task<bool> RemoveAsync(long Id)
    {
        var application = await _applicationRepository.SelectAll()
            .Where(u => u.Id == Id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (application is null)
            throw new CorruptionException(404, "User is not found");

        await _applicationRepository.DeleteAsync(Id);

        return true;
    }

    public async Task<IEnumerable<ApplicationForResultDto>> RetrieveAllAsync()
    {
        var applications = await _applicationRepository.SelectAll().ToListAsync();

        return _mapper.Map<IEnumerable<ApplicationForResultDto>>(applications);
    }

    public async Task<ApplicationForResultDto> RetrieveByIdAsync(long id)
    {
        var application = await _applicationRepository.SelectAll()
            .Where(u => u.Id == id)
            .AsNoTracking()
            .FirstOrDefaultAsync();

        if (application is null)
            throw new CorruptionException(404, "User is not found");

        return _mapper.Map<ApplicationForResultDto>(application);
    }
}
