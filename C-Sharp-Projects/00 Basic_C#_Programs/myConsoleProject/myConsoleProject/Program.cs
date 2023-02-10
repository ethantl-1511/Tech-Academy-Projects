using System;

namespace myConsoleProject
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("What is your name?");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, \n" + name + "!");
            Console.Read();
        }
    }
}