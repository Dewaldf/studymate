namespace StudyMate.Domain.SeedWork;

public interface IRepository<T> where T : Entity
{
    Task<T?> FindByIdAsync(Guid id, CancellationToken cancellationToken = default);
    void Add(T entity);
    void Update(T entity);
    void Remove(T entity);
}
