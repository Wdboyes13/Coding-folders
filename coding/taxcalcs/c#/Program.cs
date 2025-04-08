using System;
using System.ComponentModel;
namespace Program
{
    public class Program {
        public static void Main(string[] args) {
            Console.WriteLine("Enter 2-Digit province code: ");
            string prov = Console.ReadLine();
            Console.WriteLine("Enter Amount: ");
            Double amount = Convert.ToDouble(Console.ReadLine());
            
            SortedDictionary<string, double> rates = new SortedDictionary<string, double>();
            rates.Add("BC", 0.12);
            rates.Add("AB", 0.05);
            rates.Add("SK", 0.11);
            rates.Add("MN", 0.12);
            rates.Add("ON", 0.13);
            rates.Add("QC", 0.14975);
            rates.Add("NL", 0.15);
            rates.Add("PEI", 0.15);
            rates.Add("NS", 0.15);
            rates.Add("NB", 0.15);
            rates.Add("YT", 0.05);
            rates.Add("NT", 0.05);
            rates.Add("NU", 0.05);

            Double total = rates[prov] * amount + amount; 
            Console.WriteLine(total);
        }
    }
}