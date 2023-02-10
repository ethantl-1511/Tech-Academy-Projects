using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace InputAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please input a number."); //Asks the user for a number.
            int log = Convert.ToInt32(Console.ReadLine());
            File.WriteAllText(@"[your path here]", Convert.ToString(log)); // Logs that number to a text file.
            Console.WriteLine(File.ReadAllText(@"[file path]")); // Prints the text file back to the user.
            Console.Read();

        }
    }
}
