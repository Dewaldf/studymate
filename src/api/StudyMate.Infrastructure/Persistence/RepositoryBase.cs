using Microsoft.EntityFrameworkCore;
using StudyMate.Domain.SeedWork;

namespace StudyMate.Infrastructure.Persistence;

public abstract class RepositoryBase<T>(ApplicationDbContext dbContext)
    : IRepository<T> where T : Entity
{
    protected readonly DbSet<T> DbSet = dbContext.Set<T>();

    public async Task<T?> FindByIdAsync(Guid id, CancellationToken cancellationToken = default) =>
        await DbSet.FindAsync([id], cancellationToken);

    public void Add(T entity) => DbSet.Add(entity);
    public void Update(T entity) => DbSet.Update(entity);
    public void Remove(T entity) => DbSet.Remove(entity);
}
