using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog54c
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter : ");
            int num1 = int.Parse(Console.ReadLine());
            double area = 3.14159 * (num1 * num1);
            double curc = 3.14159 * 2 * num1;
            Console.WriteLine("Area: " + area);
            Console.WriteLine("circumference: " + curc);
            Console.ReadKey();
        }
    }
}
