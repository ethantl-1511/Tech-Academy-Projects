using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassAssignment
{
    static class SecondClass // declare a class to be static
    {
        public static string StaticMethod(string message)
        {
            Console.WriteLine("This is a test.");
            return message;
        }
    }
}
