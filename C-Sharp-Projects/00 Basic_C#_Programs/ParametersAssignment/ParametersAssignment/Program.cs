using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParametersAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee<string> strings = new Employee<string>(); // instantiate Employee object with "string" as generic
            strings.Things = new List<string>() { "One word", "Two word", "Three word", "Four" }; // assign list of strings to property value of Things

            Employee<int> integers = new Employee<int>(); // instantiate Employee object with "int" as generic
            integers.Things = new List<int>() { 1, 2, 5, 10 }; // assign list of integers to property value of Things

            foreach (string thing1 in strings.Things) // loop to print everything in the string list
            {
                Console.WriteLine(thing1);
            }
            foreach (int thing2 in integers.Things) // loop to print everything in the int list
            {
                Console.WriteLine(thing2);
            }

            Console.ReadLine();
        }

    }
}
