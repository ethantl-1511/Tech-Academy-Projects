using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractClassAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee testEmployee = new Employee(); // instantiate Employee object "testEmployee"
            testEmployee.firstName = "Sample"; // first name Sample
            testEmployee.lastName = "Student"; // last name Student
            testEmployee.SayName(); // call abstract superclass method SayName() on Employee object

            Console.ReadLine(); // display console
        }
    }
}
