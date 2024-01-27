using StopCorruption.Data.IRepositories;
using StopCorruption.Data.Repositries;
using StopCorruption.Service.Interfaces;
using StopCorruption.Service.Services;

namespace StopCorruption.Api.Extensions;

public static class ServiceExtensions
{
    public static void AddCorruptionService(this IServiceCollection services)
    {
        services.AddScoped<IUserService, UserService>();
        services.AddScoped<IUserRepository, UserRepository>();
        services.AddScoped(typeof(IRepository<>), typeof(Repository<>));

        services.AddScoped<IApplicationService, ApplicationService>();
        services.AddScoped<IApplicationRepository, ApplicationRepository>();

        services.AddScoped<ISectorService, SectorService>();
        services.AddScoped<ISectorRepository, SectorRepository>();

        services.AddScoped<IChatMessageService, ChatMessageService>();
        services.AddScoped<IChatMessageRepository, ChatMessageRepository>();

        services.AddScoped<IStatisticService, StatisticService>();
        services.AddScoped<IStatisticRepository, StatisticRepository>();

    }
}
