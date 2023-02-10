using System;

namespace SimpleMath
{
    class Program
    {
        static void Main()
        {
            // Takes an input from the user, multiplies it by 50, then prints the result to the console.
            Console.WriteLine("Please give a number to be multiplied by 50.");
            int multiplication = Convert.ToInt32(Console.ReadLine()) * 50;
            Console.WriteLine("Answer: " + multiplication + "\n");

            // Takes an input from the user, adds 25 to it, then prints the result to the console.
            Console.WriteLine("Please give a number to have 25 added to it.");
            int addition = Convert.ToInt32(Console.ReadLine()) + 25;
            Console.WriteLine("Answer: " + addition + "\n");

            // Takes an input from the user, divides it by 12.5, then prints the result to the console.
            Console.WriteLine("Please give a number to have divided by 12.5.");
            double division = Convert.ToDouble(Console.ReadLine()) / 12.5;
            Console.WriteLine("Answer: " + division + "\n");

            //Takes an input from the user, checks if it is greater than 50, then prints the true / false result to the console.
            Console.WriteLine("Please give a number to see if it is greater than 50.");
            bool boolCheck = Convert.ToInt32(Console.ReadLine()) > 50;
            Console.WriteLine("Answer: " + boolCheck + "\n");

            //Takes an input from the user, divides it by 7, then prints the remainder to the console
            Console.WriteLine("Please give a number to have it be divided by 7 and see the remainder.");
            int remainder = Convert.ToInt32(Console.ReadLine()) % 7;
            Console.WriteLine("Answer: " + remainder + "\n");
            Console.ReadLine();
        }
    }
}
