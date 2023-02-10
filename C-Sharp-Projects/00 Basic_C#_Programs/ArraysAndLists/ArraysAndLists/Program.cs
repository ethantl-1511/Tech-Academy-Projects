using System;
using System.Collections.Generic;

namespace ArraysAndLists
{
    class Program
    {
        static void Main()
        {
            //ARRAYS
            //One method of creating an array
            int[] numArray = new int[5]; // This constrains you to 5 array variables.
            numArray[0] = 5;
            numArray[1] = 2;
            numArray[2] = 10;
            numArray[3] = 200;
            numArray[4] = 5000;

            //Another method of creating an array
            int[] numArray1 = new int[] { 5, 2, 10, 200, 5000 }; // once you set the length, that's the [#]

            //Third method, best method
            int[] numArray2 = { 5, 2, 10, 200, 5000 };

            Console.WriteLine(numArray1[3]);
            Console.ReadLine();

            // LISTS
            List<string> intList = new List<string>();
            intList.Add("Hello");
            intList.Add("Jesse");
            intList.Remove("Jesse");
            
            Console.WriteLine(intList[0]);
            Console.ReadLine();

            byte[] byteArray = new byte[5000];
        }
    }
}
