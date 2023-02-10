using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ExceptionAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int> { 5, 4, 3, 2, 1 }; // List of numbers, backwards for better understanding in console

            Console.WriteLine("Enter a number to divide a list of numbers by: "); // User input request
            try
            {
                int choice = Convert.ToInt32(Console.ReadLine()); // User input request set as an int variable

                foreach (int number in numbers) // foreach loop of list of numbers
                {
                    Console.WriteLine(number / choice); // number divided by choice
                }
            }
            catch (FormatException ex) // format exception
            {
                Console.WriteLine(ex.Message + " | Please enter a whole number.");
            }
            catch (DivideByZeroException ex) // divide by zero exception
            {
                Console.WriteLine(ex.Message + " | You cannot divide by zero.");
            }
            Console.ReadLine();
        }
    }
}
