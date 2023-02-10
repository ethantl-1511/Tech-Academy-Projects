using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StructAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Number num1; // create an object of data type Number
            num1.Amount = 1.2m; // assign an amount to it

            Console.WriteLine(num1.Amount); // print the amount to console
            Console.ReadLine();
        }
    }
}
