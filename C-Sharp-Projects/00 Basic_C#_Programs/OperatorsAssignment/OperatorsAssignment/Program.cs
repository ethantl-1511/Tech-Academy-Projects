using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OperatorsAssignment
{
    class Program
    {
        static void Main(string[] args)
        {

            Employee Individual1 = new Employee(); // instantiate two objects
            Employee Individual2 = new Employee(); // instantiate two objects

            // assign values to their properties
            Individual1.ID = 1;
            Individual1.FirstName = "John";
            Individual1.LastName = "Doe";

            Individual2.ID = 2;
            Individual2.FirstName = "Jane";
            Individual2.LastName = "Pro";

            // compare the objects using the overloaded operators, display results
            Console.WriteLine("Is Individual 1's ID == to Individual 2's ID? " + (Individual1 == Individual2)); // Should return False
            Console.WriteLine("Is Individual 1's ID != to Individual 2's ID? " + (Individual1 != Individual2)); // Should return True

            Console.ReadLine();
        }
    }
}
