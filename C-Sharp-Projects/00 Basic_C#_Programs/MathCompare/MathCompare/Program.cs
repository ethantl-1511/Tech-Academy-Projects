using System;

namespace MathCompare
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Anonymous Income Comparison Program\n");

            // Person 1 variables
            string person1 = "Person 1";
            Console.WriteLine(person1);
            Console.WriteLine("Hourly Rate: ");
            double p1Hours = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Hours worked per week: ");
            double p1totalHours = Convert.ToDouble(Console.ReadLine());

            // Person 2 variables
            string person2 = "Person 2";
            Console.WriteLine("\n" + person2);
            Console.WriteLine("Hourly Rate: ");
            double p2Hours = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Hours worked per week: ");
            double p2totalHours = Convert.ToDouble(Console.ReadLine());

            // Math to get annual salary of Person 1 and Person 2
            double p1annualSalary = p1Hours * p1totalHours * 52;
            double p2annualSalary = p2Hours * p2totalHours * 52;
            Console.WriteLine("\n" + "Person 1's annual salary: " + p1annualSalary);
            Console.WriteLine("Person 2's annual salary: " + p2annualSalary + "\n");

            // Comparison of salaries
            bool salaryCompare = p1annualSalary > p2annualSalary;
            Console.WriteLine("Does Person 1 make more money than Person 2?\n" + salaryCompare);
            Console.ReadLine();
        }
    }
}
