using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MethodAssignment
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Give a number to do math operations on:"); // user-input
            int num = Convert.ToInt32(Console.ReadLine()); // int variable used for parameter
            int AddResult = SimpleMath.Add(num); // calls the class.method(parameter) for add
            int SubResult = SimpleMath.Subtract(num); // calls the class.method(parameter) for subtract
            int MulResult = SimpleMath.Multiply(num); // calls the class.method(parameter) for multiply

            // console results
            Console.WriteLine("Your number + 100: " + AddResult);
            Console.WriteLine("Your number - 100: " + SubResult);
            Console.WriteLine("Your number * 100: " + MulResult);
            Console.ReadLine();
        }
    }
}
