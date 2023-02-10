using System;
using System.Collections.Generic;

namespace ArrayAssignment
{
    class Program
    {
        static void Main()
        {
            // arrays and list info
            string[] strArray = { "JavaScript", "Python", "C#",}; // string array
            int[] intArray = { 1, 5, 10 }; // integer array
            List<string> intList = new List<string>(); // string list
            intList.Add("Superman");
            intList.Add("Batman");
            intList.Add("Spider-Man");

            // user-input for string array
            Console.WriteLine("Select an item from the string array: (Please type 0, 1, or 2)");
             // try-catch for if the user chooses an index position outside of what is listed
            try
            {
                Console.WriteLine(strArray[Convert.ToInt32(Console.ReadLine())]);
            }
            catch // no exception, we want the user to be able to continue inputs
            {
                Console.WriteLine("Invalid index selected.");
            }

            // user-input for integer array
            Console.WriteLine("Select an item from the integer array: (Please type 0, 1, or 2)");
            // try-catch for if the user chooses an index position outside of what is listed
            try
            {
                Console.WriteLine(intArray[Convert.ToInt32(Console.ReadLine())]);
            }
            catch // no exception, we want the user to be able to continue inputs
            {
                Console.WriteLine("Invalid index selection.");
            }

            // user-input for string list
            Console.WriteLine("Select an item from the string list: (Please type 0, 1, or 2)");
            // try-catch for if the user chooses an index position outside of what is listed
            try
            {
                Console.WriteLine(intList[Convert.ToInt32(Console.ReadLine())]);
            }
            catch // no exception, we want the user to be able to continue inputs
            {
                Console.WriteLine("Invalid index selection.");
            }
            Console.ReadLine();
        }
    }
}
