using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StingInterveiw16
{
    class Program
    {
        static bool searchText(string text, string search)
        {
            int tLen = text.Length;
            int sLen = search.Length;

            if (sLen > tLen) return false;

            for (int i = 0; i <= tLen - sLen; i++)
                if (text.Substring(i, sLen) == search) return true;
            return false;
        }
        static void Main(string[] args)
        {
            Console.Write("Etner a string:");
            string text = Console.ReadLine();
            Console.Write("enter a substring to search for: ");
            string word = Console.ReadLine();
            bool result = searchText(text, word);
            Console.WriteLine("does \"{0}\" contain \"{1}\"?: {2}", text, word, result);
            Console.ReadLine();
        }
    }
}
