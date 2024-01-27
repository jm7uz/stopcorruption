using Microsoft.EntityFrameworkCore;
using StopCorruption.Domain.Entities;

namespace StopCorruption.Data.DbContexts;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
    { }

    public DbSet<Application> Application { get; set; }
    public DbSet<User> User { get; set; }
    public DbSet<Statistic> Statistics { get; set; }
    public DbSet<ChatMessage> ChatMessages { get; set; }
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Application>()
    .HasOne(a => a.User)
    .WithMany()
    .HasForeignKey(a => a.UserId);

    }
}
