using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StringAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            string string1 = "This is ";
            string string2 = "a string for ";
            string string3 = "concatenating purposes.";
            string fullString = (string1 + string2 + string3).ToUpper();
            Console.WriteLine(fullString);

            StringBuilder newString = new StringBuilder();
            newString.Append("This is ");
            newString.Append("for StringBuilder ");
            newString.Append("purposes.");
            Console.WriteLine(newString);
            Console.Read();
        }
    }
}
