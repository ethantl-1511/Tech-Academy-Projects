using System;
using System.Collections.Generic;
using System.Linq;

namespace IterationAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            // Part One
            Console.WriteLine("Part One");
            string[] array1 = { "One", "The", "Loop", "Create", "And" }; // A one-dimensional array of strings
            Console.WriteLine("Hello. Type something to be added to a array of strings: "); // Ask the user to input some text. 
            string text = Console.ReadLine();

            // A loop that iterates through each string in the array
            for (int i = 0; i < array1.Length; i++)
            {
                array1[i] += text; // adds the user's text input to the end of each string
            }
            // Then create a second loop that prints off each string in the array one at a time.
            for (int j = 0; j < array1.Length; j++)
            {
                Console.WriteLine(array1[j]);
            }
            Console.ReadLine(); // Press Enter to continue


            // Part Two
            Console.WriteLine("Part Two");
            int infiniteLoop = 0;
            // while (infiniteLoop >= 0) // this creates an infinite loop, it will keep adding 1 to infiniteLoop as it is ALWAYS greater than or equal to 0.
            while (infiniteLoop <= 10) // this fixes an infinite loop, as it will be forced to stop looping once it hits 10.
            {
                Console.WriteLine(infiniteLoop);
                infiniteLoop++;
            }
            Console.ReadLine(); // Press Enter to continue


            // Part Three, which is basically Part Two
            Console.WriteLine("Part Three");
            int x = 0;
            int y = 0;
            while (x < 10)
            {
                Console.WriteLine(x); // Will spit out numbers 0-9
                x++;
            }
            Console.WriteLine();
            while (y <= 10)
            {
                Console.WriteLine(y); // Will spit out numbers 0-10
                y++;
            }
            Console.ReadLine(); // Press Enter to continue


            // Part Four
            Console.WriteLine("Part Four");
            string[] array2 = { "list", "the", "loop", "code", "and" }; // A list of strings where each item in the list is unique. 
            Console.WriteLine("Input a word to search for in the array list: "); // Ask the user to input text to search for in the list. 
            string search = Console.ReadLine();
            bool found = false;
            // A loop that iterates through the list-
            for (int j = 0; j < array2.Length; j++)
            {
                if (array2[j].EndsWith(search) == true)
                {
                    Console.WriteLine("\"" + search + "\" was found at index [" + Array.IndexOf(array2, search) + "]"); //  -displays the index of the list item that contains matching text on the screen.
                    found = true;
                    break; // Add code that stops the loop from executing once a match has been found.
                }
            }
            if (!found)
            {
                Console.WriteLine("Your input is not on the list.");
            }
            Console.ReadLine(); // Press Enter to continue


            // Part Five, essentially Part Four just remove break and add iteration value to IndexOf
            Console.WriteLine("Part Five");
            string[] array3 = { "list", "the", "loop", "code", "list" }; // A list of strings that has at least two identical strings in the list.
            Console.WriteLine("Input a word to search for in the array list: "); // Ask the user to input text to search for in the list. 
            string search2 = Console.ReadLine();

            bool found2 = false;
            // Create a loop that iterates through the list and then displays the indices of the items matching the user-selected text.
            for (int k = 0; k < array2.Length; k++)
            {
                if (array3[k].EndsWith(search2) == true)
                {
                    Console.WriteLine("\"" + search2 + "\" was found at index [" + Array.IndexOf(array3, search2, k) + "]");
                    found2 = true;
                }
            }
            if (!found2)
            {
                Console.WriteLine("Your input is not on the list.");
            }
            Console.ReadLine(); // Press Enter to continue


            // Part Six
            Console.WriteLine("Part Six");
            List<string> originalLetters = new List<string> { "A", "B", "C", "D", "C" }; // original list
            List<string> uniqueLetters = new List<string> { }; // list for tracking found letters

            foreach (string original in originalLetters) // iterate through original list
            {
                bool found3 = false; // found is false, we must find it
                foreach (string unique in uniqueLetters) // iterate through unique list
                {
                    if (original == unique) // if the original letter is equal to the unique letter
                    {
                        found3 = true; // found is true
                        break;
                    }
                }
                if (found3 == true) // if found is now true,
                {
                    Console.WriteLine(original + " - this item is a duplicate"); // true means item is a duplicate
                }
                else
                {
                    Console.WriteLine(original + " - this item is unique"); // false means item is unique
                    uniqueLetters.Add(original); // add original letter to unique list
                }
            }
            Console.ReadLine(); // Press Enter to continue
        }
    }
}
