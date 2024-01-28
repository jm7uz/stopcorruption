using StopCorruption.Data.IRepositories;
using StopCorruption.Data.Repositries;
using StopCorruption.Service.Interfaces;
using StopCorruption.Service.Services;
using StopCorruption.Services;

namespace StopCorruption.Api.Extensions;

public static class ServiceExtensions
{
    public static void AddCorruptionService(this IServiceCollection services)
    {
        services.AddScoped(typeof(IRepository<>), typeof(Repository<>));

        services.AddScoped<IUserService, UserService>();
        services.AddScoped<IUserRepository, UserRepository>();

        services.AddScoped<IApplicationRepository, ApplicationRepository>();
        services.AddScoped<IApplicationService, ApplicationService>();

        services.AddScoped<ISectorRepository, SectorRepository>();
        services.AddScoped<ISectorService, SectorService>();

        services.AddScoped<IChatMessageRepository, ChatMessageRepository>();
        services.AddScoped<IChatMessageService, ChatMessageService>();

        services.AddScoped<IStatisticService, StatisticService>();

    }
}
