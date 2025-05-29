using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lp_4_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Package must not exceed 27 kilograms, and 100,000 cubic centimeters.");
            Console.WriteLine("Enter weight in kilograms: ");
            int weight = int.Parse(Console.ReadLine());
            if (weight > 27)
            {
                Console.WriteLine("To Heavy");
                Console.ReadLine();
            }
            else
            {
                Console.WriteLine("Enter length in centemeters: ");
                int length = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter width in centemeters: ");
                int width = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter height in centemeters: ");
                int height = int.Parse(Console.ReadLine());
                if (width * length * height > 100000) { Console.WriteLine("To large"); }
                else
                {
                    Console.WriteLine("Your package can be sent.");
                    Console.ReadLine();
                }
                
            }
        }
    }
}
