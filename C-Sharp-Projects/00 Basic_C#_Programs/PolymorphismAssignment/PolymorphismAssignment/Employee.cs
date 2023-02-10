using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PolymorphismAssignment
{
    class Employee : Person, IQuittable // inherit the interface and implement Quit() method
    {
        public override void SayName() // implement the SayName() method inside Employee class
        {
            Console.WriteLine("Name: " + firstName + " " + lastName);
        }

        public void Quit()
        {
            Console.WriteLine("This employee QUIT!");
        }
    }
}