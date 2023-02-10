using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TryCatchAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                int year = DateTime.Now.Year; // current year
                int age = 1; // age will be 1 by default, we don't want zeroes

                bool validNumber = false; // validAnswer will be false
                while (!validNumber) // while-loop to do checks, we want positive numbers only.
                {
                    Console.Write("Please input your age: ");
                    string check = Console.ReadLine(); // gets user input and sets to string
                    validNumber = int.TryParse(check, out age); // checks if string is a valid number
                    int number = Convert.ToInt32(check); // convert string to int
                    if (number < 0) // check if int number is < 0
                    {
                        throw new Exception(); // if it is, throw exception
                    }
                    Console.WriteLine(year - age); // otherwise, do math
                }
            }
            catch (Exception) // general exception
            {
                Console.WriteLine("Something went wrong. Try putting in a whole number."); 
            }
            Console.ReadLine();
        }
    }
}
