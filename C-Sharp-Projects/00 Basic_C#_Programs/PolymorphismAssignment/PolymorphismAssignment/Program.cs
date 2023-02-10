using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PolymorphismAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee testEmployee = new Employee(); // instantiate Employee object "testEmployee"
            testEmployee.firstName = "Sample"; // first name Sample
            testEmployee.lastName = "Student"; // last name Student
            testEmployee.SayName(); // call abstract superclass method SayName() on Employee object

            // Using polymorphism to create an object of type IQuittable, calling Quit() method on it.
            IQuittable quitter = new Employee();
            quitter.Quit();

            Console.ReadLine(); // display console
        }
    }
}
