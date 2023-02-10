using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MethodAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Give two numbers to do a math operation on. Second input is optional, default value is 100."); // ask the user to input two numbers one at a time
            int num1 = Convert.ToInt32(Console.ReadLine()); // first input is converted to int
            string optionalS = Console.ReadLine(); // second input is kept as a string to determine if the user skipped the second input
            if (optionalS == "") // if the input is blank, the user skipped giving a second input, therefore
            {
                Console.WriteLine(num1 + " + 100 = " + SimpleMath.Add(num1)); // instantiate class/call the method for the one parameter, ignoring the optionalS variable
            }
            else // if the user did NOT put in blank, convert string to int and instantiate class/call method for both parameters
            {
                int optionalN = Convert.ToInt32(optionalS);
                Console.WriteLine(num1 +" + " + optionalN + " = " + SimpleMath.Add(num1, optionalN));
            }
            Console.ReadLine(); // read results
        }
    }

    class SimpleMath
    {
        public static int Add(int num1, int num2 = 100) // optional parameter num2 has a default value of 100
        {
            return (num1 + num2);
        }
    }
}
