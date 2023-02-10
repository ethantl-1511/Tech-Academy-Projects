using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MethodsAndObjectsAssignment
{
    public class Person // create a class called Person, give it two properties, data type string
    {
        public string FirstName { get; set; } //one called FirstName
        public string LastName { get; set; } // second called LastName

        // give this class a void method called SayName(), simply writes person's full name to console
        public void SayName()
        {
            Console.WriteLine("Name: [" + FirstName + " " + LastName + "]"); // format "Name: [full name]"
        }
    }
}