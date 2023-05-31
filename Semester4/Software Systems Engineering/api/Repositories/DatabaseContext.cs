using Microsoft.EntityFrameworkCore;
using api.Models;

namespace api.Repositories
{
    public class DatabaseContext : DbContext
    {
        public DatabaseContext() {}
        public DatabaseContext(DbContextOptions<DatabaseContext> options) : base(options) { }

        public virtual DbSet<User> Users { get; set; } = null!;
        public virtual DbSet<Destination> PublicDestinations { get; set; } = null!;
        public virtual DbSet<PrivateDestination> PrivateDestinations { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder) 
        {
            // modelBuilder.Entity<Destination>().ToTable("destinations");
            // modelBuilder.Entity<PrivateDestination>().ToTable("privatedestinations");

            // Set username to be unique
            modelBuilder.Entity<User>()
                .HasIndex(u => u.Username)
                .IsUnique();
        }
    }
}