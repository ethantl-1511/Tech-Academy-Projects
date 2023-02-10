using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PolymorphismAssignment
{
    public abstract class Person // create an abstract class called Person
    {
        public string firstName { get; set; } // string firstName property
        public string lastName { get; set; } // string lastName property

        public abstract void SayName(); // method SayName(), abstract
    }
}