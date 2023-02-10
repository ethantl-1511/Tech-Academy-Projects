using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConstructorAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            const string word = "example"; // const variable
            var integer = 1; // var variable
        }
    }

    public class Example
    {
        public string FirstName;
        public string LastName;

        public Example(string FirstName) : this(FirstName, "Skywalker") // constructor one, chained, passes both params including default value "Skywalker" for second param
        {

        }

        public Example(string FirstName, string LastName) // constructor two
        {
            this.FirstName = FirstName;
            this.LastName = LastName;
        }
    }
}
