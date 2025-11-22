using FluentAssertions;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Api.Test.User
{
    [TestClass]
    public class UserGetTest
    {
        [TestMethod]
        public void TrueTest()
        {
            true.Should().BeTrue();
        }
    }
}
