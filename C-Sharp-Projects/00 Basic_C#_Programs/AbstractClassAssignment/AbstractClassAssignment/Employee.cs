using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractClassAssignment
{
    class Employee : Person // create another class called Employee, have it inherit Person class
    {
        public override void SayName() // implement the SayName() method inside Employee class
        {
            Console.WriteLine("Name: " + firstName + " " + lastName);
        }
    }
}
