using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lp4_5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter grade percentage");
            double grade = double FileStyleUriParser(Console.ReadLine());
            char letgrade = ' ';
            if(grade >= 90) {
                letgrade = 'A';
            } else if (grade >= 80) {
                letgrade = 'B';
            } else if (grade >= 70) {
                letgrade = 'C';
            } else if (grade >= 60) {
                letgrade = 'D';
            } else {
                letgrade = 'F';
            }
            Console.WriteLine(letgrade);
        }
    }
}
