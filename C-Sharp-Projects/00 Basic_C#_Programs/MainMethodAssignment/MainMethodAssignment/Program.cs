using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MainMethodAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = 10;
            int AddResult = SimpleMath.Add(num); // instantiate the class and call the one method
            Console.WriteLine("10 + 100: " + AddResult); // display results

            decimal decimalNum = 1.14515627m; 
            int decimalResult = SimpleMath.Add(decimalNum); // instantiate the class and call the one method
            Console.WriteLine("1.14515627 + 100.25: " + decimalResult); // display results

            try
            {
                Console.WriteLine("Give a number to do another math operation on:");
                string stringNum = Console.ReadLine(); // string variable
                int sAddResult = SimpleMath.Add(stringNum);  // instantiate the class and call the one method, set to int variable
                Console.WriteLine("Your number + 100: " + sAddResult); // display results
            }
            catch (FormatException ex) // just in case the input is not a number
            {
                Console.WriteLine(ex.Message);
            }

            Console.ReadLine();
        } 

    }

    class SimpleMath // Create a class
    {
        public static int Add(int num) // create a method
        {
            return (num + 100);
        }

        public static int Add(decimal dnum) // add a second method, same name, takes a decimal, returns an int
        {
            return (Convert.ToInt32(dnum) + 100); // convert dnum, add, return
        }

        public static int Add(string snum) // create a third method, same name, takes a string, returns an int
        {;
            return (Convert.ToInt32(snum) + 100); // convert snum, add, return
        }
    }
}
