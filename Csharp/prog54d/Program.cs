using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog54d
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Leg 1: ");
            int num1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Leg 2: ");
            int num2 = int.Parse(Console.ReadLine());
            double area = (num1 * num2) / 2;
            double hypo = Math.Sqrt((num1 * num1) + (num2 * num2));
            Console.WriteLine("area: " + area);
            Console.WriteLine("Hypotnuse: " + hypo);
            Console.ReadKey();
        }
    }
}
