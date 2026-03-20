namespace StudyMate.Api.Tests.Build;

public class BoundedContextFolderTests
{
    private static readonly string[] BoundedContexts =
        ["Learning", "Identity", "Curriculum", "Reporting", "Safeguarding"];

    private static string SolutionRoot =>
        Path.GetFullPath(Path.Combine(
            AppContext.BaseDirectory, "..", "..", "..", "..", ".."));

    [Theory]
    [InlineData("StudyMate.Domain")]
    [InlineData("StudyMate.Application")]
    [InlineData("StudyMate.Infrastructure")]
    [InlineData("StudyMate.Api/Endpoints")]
    public void All_BoundedContext_Folders_Exist(string project)
    {
        foreach (var ctx in BoundedContexts)
        {
            var path = Path.Combine(SolutionRoot, project, ctx);
            Assert.True(Directory.Exists(path),
                $"Missing bounded context folder: {project}/{ctx}");
        }
    }
}
