namespace StudyMate.Domain.SeedWork;

public interface IDomainEvent
{
    DateTime OccurredOn { get; }
}
