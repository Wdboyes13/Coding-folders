#include <iostream>
 #include <map>
  #include <string>
   using namespace std;
    int main() {
         map<string, float> rates;
         rates["BC"] = 0.12; 
         rates["AB"] = 0.05; 
         rates["SK"] = 0.11; 
         rates["MN"] = 0.12; 
         rates["ON"] = 0.13;
         rates["QC"] = 0.14975; 
         rates["NL"] = 0.15; 
         rates["NS"] = 0.15; 
         rates["PEI"] = 0.15;
         rates["NB"] = 0.15; 
         rates["YT"] = 0.05; 
         rates["NU"] = 0.05; 
         rates["NT"] = 0.05; 
         string prov; 
         cout << "Enter the 2-digit province code: ";
         cin >> prov; float amount; 
         cout << "Enter your amount: "; 
         cin >> amount;
         float total = rates[prov]*amount+amount; 
         cout << total << '\n';
         return 0; 
        }
