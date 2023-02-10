using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LambdaAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            // 2.
            List<Employee> employeeList = new List<Employee>(); // create a list of at least 10 employees
            employeeList.Add(new Employee() { Id = 1, FirstName = "Joe", LastName = "Dirst" }); // at least two have the first name "Joe"
            employeeList.Add(new Employee() { Id = 2, FirstName = "Dak", LastName = "Boid" });
            employeeList.Add(new Employee() { Id = 3, FirstName = "Luke", LastName = "Skywalker" });
            employeeList.Add(new Employee() { Id = 4, FirstName = "Han", LastName = "Solo" });
            employeeList.Add(new Employee() { Id = 5, FirstName = "Jim", LastName = "Jimmyson" });
            employeeList.Add(new Employee() { Id = 6, FirstName = "Bob", LastName = "Ross" });
            employeeList.Add(new Employee() { Id = 7, FirstName = "Joe", LastName = "Gregory" });  // at least two have the first name "Joe"
            employeeList.Add(new Employee() { Id = 8, FirstName = "Manfred", LastName = "Von Karma" });
            employeeList.Add(new Employee() { Id = 9, FirstName = "Greg", LastName = "Yesterson" });
            employeeList.Add(new Employee() { Id = 10, FirstName = "Fred", LastName = "Drummond" });

            //// 3.
            //foreach (var employee in employeeList) // using a foreach loop,
            //{
            //    if (employee.FirstName == "Joe")
            //    {
            //        List<Employee> joeEmployees = new List<Employee>(); // create a new list for all employes with first name "Joe"
            //        joeEmployees.Add(employee); // add them
            //        // foreach to check if the employees are in the new list
            //        foreach (var joeE in joeEmployees)
            //        {
            //            Console.WriteLine("{0}, {1}, {2}", joeE.Id, joeE.FirstName, joeE.LastName);
            //        }
            //    }
            //}

            // 4. Perform the same action again with a lambda expression
            List<Employee> joeEmployees = new List<Employee>();
            joeEmployees = employeeList.Where(employees => employees.FirstName == "Joe").ToList();
            foreach (var joeE in joeEmployees)
            {
                Console.WriteLine("{0}, {1}, {2}", joeE.Id, joeE.FirstName, joeE.LastName);
            }


            // 5. Using a lambda expression, make a list of all employees with an Id number greater than 5.
            List<Employee> IdEmployees = new List<Employee>();
            IdEmployees = employeeList.Where(employees => employees.Id > 5).ToList();
            foreach (var employee in IdEmployees)
            {
                Console.WriteLine("{0}, {1}, {2}", employee.Id, employee.FirstName, employee.LastName);
            }

            Console.ReadLine();
        }
    }
}
