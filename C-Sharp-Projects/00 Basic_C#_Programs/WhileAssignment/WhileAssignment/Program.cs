using System;

namespace WhileAssignment
{
    class Program
    {
        static void Main()
        {
            // boolean comparison using while
            bool check = true; // the bool is true
            do // do-while
            {
                Console.WriteLine("Is the check true or false?");
                bool answer = Convert.ToBoolean(Console.ReadLine()); // answer becomes a new bool to compare
                if (answer == check) // compare bool to bool, if they are equal...
                {
                    Console.WriteLine("The check is true!");
                    Console.ReadLine();
                    break;
                }
                else // otherwise, try again
                {
                    Console.WriteLine("The check is not true. Try again.");
                }
            }
            while (check); // while check = true
        }
    }
}
