using StudyMate.Domain.SeedWork;

namespace StudyMate.Application.Tests.Common;

// Minimal domain fixtures for invariant tests
public class ProductName : ValueObject
{
    public string Value { get; }

    public ProductName(string value)
    {
        if (string.IsNullOrWhiteSpace(value))
            throw new DomainException("Name cannot be empty.");
        Value = value;
    }

    protected override IEnumerable<object> GetEqualityComponents()
    {
        yield return Value;
    }
}

public class DomainInvariantTests
{
    [Fact]
    public void ValueObject_With_Invalid_State_Throws_DomainException()
    {
        Assert.Throws<DomainException>(() => new ProductName(""));
    }

    [Fact]
    public void ValueObject_Equality_Is_Structural_Not_Referential()
    {
        var a = new ProductName("StudyMate");
        var b = new ProductName("StudyMate");
        var c = new ProductName("Other");

        Assert.Equal(a, b);
        Assert.NotEqual(a, c);
        Assert.True(a == b);
        Assert.True(a != c);
    }

    [Fact]
    public void ValueObject_Two_Instances_Same_Value_Have_Same_HashCode()
    {
        var a = new ProductName("StudyMate");
        var b = new ProductName("StudyMate");

        Assert.Equal(a.GetHashCode(), b.GetHashCode());
    }
}
