using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OperatorsAssignment
{
    public class Employee
    {
        public int ID { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public static bool operator== (Employee employee1, Employee employee2)
        {
            return employee1.ID.Equals(employee2.ID);
        }

        public static bool operator!= (Employee employee1, Employee employee2)
        {
            return !employee1.ID.Equals(employee2.ID);
        }
    }
}
