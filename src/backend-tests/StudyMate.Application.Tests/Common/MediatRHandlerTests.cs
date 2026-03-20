using FluentValidation;
using MediatR;
using Microsoft.Extensions.DependencyInjection;
using StudyMate.Application.Common.Behaviours;

namespace StudyMate.Application.Tests.Common;

// Minimal in-test handler fixture
public record PingQuery : IRequest<string>;

public class PingQueryHandler : IRequestHandler<PingQuery, string>
{
    public Task<string> Handle(PingQuery request, CancellationToken ct) =>
        Task.FromResult("pong");
}

public record ValidatedCommand(string Name) : IRequest<Unit>;

public class ValidatedCommandValidator : AbstractValidator<ValidatedCommand>
{
    public ValidatedCommandValidator() =>
        RuleFor(x => x.Name).NotEmpty().WithMessage("Name is required.");
}

public class ValidatedCommandHandler : IRequestHandler<ValidatedCommand, Unit>
{
    public Task<Unit> Handle(ValidatedCommand request, CancellationToken ct) =>
        Task.FromResult(Unit.Value);
}

public class MediatRHandlerTests
{
    private static IServiceProvider BuildServiceProvider()
    {
        var services = new ServiceCollection();
        var assembly = typeof(MediatRHandlerTests).Assembly;

        services.AddMediatR(cfg =>
        {
            cfg.RegisterServicesFromAssembly(assembly);
            cfg.AddBehavior(typeof(IPipelineBehavior<,>), typeof(ValidationBehaviour<,>));
        });
        services.AddValidatorsFromAssembly(assembly);

        return services.BuildServiceProvider();
    }

    [Fact]
    public async Task MediatR_Can_Resolve_And_Send_Request()
    {
        var sp = BuildServiceProvider();
        var mediator = sp.GetRequiredService<IMediator>();

        var result = await mediator.Send(new PingQuery());

        Assert.Equal("pong", result);
    }

    [Fact]
    public async Task ValidationBehaviour_Is_Registered_And_Throws_When_Invalid()
    {
        var sp = BuildServiceProvider();
        var mediator = sp.GetRequiredService<IMediator>();

        await Assert.ThrowsAsync<ValidationException>(() =>
            mediator.Send(new ValidatedCommand(Name: "")));
    }

    [Fact]
    public async Task ValidationBehaviour_Passes_Through_When_Valid()
    {
        var sp = BuildServiceProvider();
        var mediator = sp.GetRequiredService<IMediator>();

        var result = await mediator.Send(new ValidatedCommand(Name: "StudyMate"));

        Assert.Equal(Unit.Value, result);
    }
}
