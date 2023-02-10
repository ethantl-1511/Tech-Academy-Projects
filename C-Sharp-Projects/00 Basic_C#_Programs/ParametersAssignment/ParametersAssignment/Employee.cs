using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParametersAssignment
{
    public class Employee<T> // make the employee class take a generic type parameter <T>
    {
        public List<T> Things { get; set; } // add a property called things, data type generic list
    }
}
