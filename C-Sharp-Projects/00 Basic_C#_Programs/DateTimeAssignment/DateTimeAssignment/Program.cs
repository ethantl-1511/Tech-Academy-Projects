using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DateTimeAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("It is currently: " + DateTime.Now); // prints current date and time to the console

            Console.Write("Please enter a number: "); // asks user for a number
            int userInput = Convert.ToInt32(Console.ReadLine());

            var newTime = DateTime.Now.AddHours(userInput); 
            Console.WriteLine("We shall add " + userInput + " hours to the current time, the new time is: " + newTime); // prints new time based on user input
            Console.Read();
        }
    }
}
