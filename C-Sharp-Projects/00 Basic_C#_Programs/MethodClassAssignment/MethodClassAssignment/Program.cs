using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MethodClassAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            int number1 = 100; // first integer to pass
            int number2 = 5; // second integer to pass
            VoidClass.vClass(number1, number2); // instantiate class/call method, passing in two numbers
            VoidClass.vClass(pNum2: number1, pNum1: number2); // instantiate class/call method, passing in two numbers by name (reversed for fun)
            Console.ReadLine(); // should print 5 for first pass, should print 100 for second pass
        }
    }
    
    class VoidClass
    {
        public static void vClass(int pNum1, int pNum2) // public void class, takes two integers as paramaters
        {
            int someMath = pNum1 + 100; // first integer gets a math operation
            //Console.WriteLine(someMath); // display someMath to ensure it works... it does
            Console.WriteLine(pNum2); // second integer gets displayed to the screen
        }
    }
}
