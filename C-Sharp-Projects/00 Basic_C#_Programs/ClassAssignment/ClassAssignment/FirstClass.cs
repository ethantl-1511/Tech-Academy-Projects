using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassAssignment
{
    class FirstClass // create a class
    {
        public void cAssignment(int someData) // create a void method that outputs an integer
        {
            int methodDivide = someData / 2; // Have the method divide the data passed to it by 2.
            Console.WriteLine("Your number / 2 = " + methodDivide);
        }

        public void cAssignment(out int otherData) // create a method with output parameters, overload a method
        {
            otherData = 100;
        }
    }
}
