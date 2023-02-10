using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MethodsAndObjectsAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee testEmployee = new Employee(); // instantiate Employee object "testEmployee"
            testEmployee.FirstName = "Sample"; // first name Sample
            testEmployee.LastName = "Student"; // last name Student
            testEmployee.SayName(); // call superclass method SayName() on Employee object

            Console.ReadLine(); // display console
        }
    }
}
