using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParsingEnumsAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            try // wrap in try/catch block
            {
                DayOfTheWeek today;
                Console.WriteLine("Enter the current day of the week."); // prompt user to enter current day of the week.
                string response = Console.ReadLine();

                if (!Char.IsDigit(response,0)) // checking to see if user doesn't input digit, if they do throw exception.
                {
                    today = (DayOfTheWeek)Enum.Parse(typeof(DayOfTheWeek), response, true); // parse reseponse with enum, assign to enum type variable.
                    Console.WriteLine(today);
                }
                else
                {
                    throw new FormatException();
                }

            }
            catch // print if an error occurs
            {
                Console.WriteLine("Please enter an actual day of the week.");
            }
            Console.ReadLine();
        }
    }

    public enum DayOfTheWeek // create an enum for the days of the week
    {
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday
    }
}
