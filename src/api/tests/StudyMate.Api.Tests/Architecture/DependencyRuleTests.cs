using NetArchTest.Rules;
using StudyMate.Api;

namespace StudyMate.Api.Tests.Architecture;

public class DependencyRuleTests
{
    private static readonly System.Reflection.Assembly ApiAssembly =
        typeof(Program).Assembly;

    [Fact]
    public void Api_Should_Not_Reference_Domain_Directly()
    {
        var directRefs = ApiAssembly.GetReferencedAssemblies()
            .Select(a => a.Name);

        Assert.DoesNotContain("StudyMate.Domain", directRefs);
    }

    [Fact]
    public void Api_Should_Reference_Application()
    {
        var directRefs = ApiAssembly.GetReferencedAssemblies()
            .Select(a => a.Name);

        Assert.Contains("StudyMate.Application", directRefs);
    }

    [Fact]
    public void Api_Types_Should_Not_HaveDependencyOn_Domain_Namespace()
    {
        var result = Types.InAssembly(ApiAssembly)
            .ShouldNot()
            .HaveDependencyOn("StudyMate.Domain")
            .GetResult();

        Assert.True(result.IsSuccessful,
            $"Api types with illegal Domain dependency: {string.Join(", ", result.FailingTypeNames ?? [])}");
    }

    [Fact]
    public void Domain_Should_Have_No_External_Nuget_Dependencies()
    {
        var domainAssembly = typeof(StudyMate.Domain.SeedWork.Entity).Assembly;
        var refs = domainAssembly.GetReferencedAssemblies().Select(a => a.Name ?? "").ToList();

        var allowed = new[] { "System", "Microsoft", "mscorlib", "netstandard", "StudyMate" };
        var forbidden = refs.Where(r => !allowed.Any(prefix => r.StartsWith(prefix))).ToList();

        Assert.Empty(forbidden);
    }

    [Fact]
    public void Infrastructure_Should_Reference_Domain_And_Application()
    {
        var infraAssembly = typeof(StudyMate.Infrastructure.DependencyInjection).Assembly;
        var directRefs = infraAssembly.GetReferencedAssemblies().Select(a => a.Name).ToList();

        Assert.Contains("StudyMate.Domain", directRefs);
        Assert.Contains("StudyMate.Application", directRefs);
    }
}
