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



    }
}
