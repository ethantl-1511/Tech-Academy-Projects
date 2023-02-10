using System;

namespace DailyReport
{
    class Program
    {
        static void Main()
        {
            // Start-up text
            Console.WriteLine("The Tech Academy\nStudent Daily Report\n");

            // Question (A) and string variable answer
            Console.WriteLine("What is your name?");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, " + name + "\n");

            // Question (B) and string variable answer
            Console.WriteLine("What course are you on?");
            string course = Console.ReadLine();
            Console.WriteLine("I see, you are on \"" + course + "\"\n");

            // Question (C) and int conversion variable
            Console.WriteLine("What page number?");
            //string number = Console.ReadLine();
            //int page = Convert.ToInt32(number);
            int page = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Ah, you are on Step: " + page + "\n");

            // Question (D) and bool conversion variable
            Console.WriteLine("Do you need help with anything? Please answer \"true\" or \"false.\"");
            bool help = Convert.ToBoolean(Console.ReadLine());
            Console.WriteLine("You need help? " + help + "\n");

            // Question (E)
            Console.WriteLine("Were there any positive experiences you’d like to share? Please give specifics.");
            string experience = Console.ReadLine();
            Console.WriteLine("You wrote: \"" + experience + "\"\n");

            // Question (F)
            Console.WriteLine("Is there any other feedback you’d like to provide? Please be specific.");
            string feedback = Console.ReadLine();
            Console.WriteLine("Your feedback: \"" + feedback + "\n");

            // Question (G)
            Console.WriteLine("How many hours did you study today? Please write a whole number.");
            uint hours = Convert.ToUInt32(Console.ReadLine());
            Console.WriteLine("You studied for: " + hours + " hours.\n");

            // Final response.
            Console.WriteLine("Thank you for your answers. An Instructor will respond to this shortly. Have a great day!");
            Console.ReadLine();
        }
    }
}
