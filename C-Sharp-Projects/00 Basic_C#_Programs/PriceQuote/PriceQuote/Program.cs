using System;

namespace PriceQuote
{
    class Program
    {
        static void Main()
        {
            // Intro and first question for weight
            Console.WriteLine("Welcome to Package Express. Please follow the instructions below.");
            Console.WriteLine("What is the weight of your package? Please give a whole number rounded up.");
            int packageWeight = Convert.ToInt32(Console.ReadLine());

            if (packageWeight > 50) // If the weight is too heavy, program will end
            {
                Console.WriteLine("Package is too heavy to be shipped via Package Express. Have a good day.");
                Console.ReadLine();
            }
            else { // Since the weight is not too heavy, continue with width/height/length questions.
                Console.WriteLine("What is the width of your package? Please give a whole number rounded up.");
                int packageWidth = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("What is the height of your package? Please give a whole number rounded up.");
                int packageHeight = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("What is the length of your package? Please give a whole number rounded up.");
                int packageLength = Convert.ToInt32(Console.ReadLine());

                if (packageWidth + packageHeight + packageLength > 50) // If the sum of width/height/length is larger than 50, program will end
                {
                    Console.WriteLine("Package is too big to be shipped via Package Express. Have a good day.");
                    Console.ReadLine();
                }
                else { // Since sum of the package dimensions is smaller than 50, continue with priceQuote calculation
                    float priceQuote = (packageHeight * packageWidth * packageLength) * packageWeight / 100;
                    Console.WriteLine("Your estimated total for shipping this package is: $" + priceQuote + ".00\nThank you!");
                    Console.ReadLine();
                }
            }
        }
    }
}
