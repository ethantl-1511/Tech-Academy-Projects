using System;

namespace InsuranceApproval
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("What is your age?");
            int age = Convert.ToInt32(Console.ReadLine()); // Convert string number to integer.

            Console.WriteLine("Have you ever had a DUI?");
            bool DUI = Convert.ToBoolean(Console.ReadLine()); // Convert string to bool.

            Console.WriteLine("How many speeding tickets do you have?");
            int tickets = Convert.ToInt32(Console.ReadLine()); // Convert string number to integer.

            Console.WriteLine("Qualified?");
            Console.WriteLine(age > 15 && DUI == false && tickets < 3); // Check if input for age and DUI and tickets match criteria for qualification
            Console.ReadLine();
        }
    }
}
