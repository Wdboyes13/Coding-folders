package main

import "fmt"

func main() {
	var prov string
	var amount int
	fmt.Print("Enter your provinces 2 digit code in lowercase: ")
	fmt.Scan(&prov)
	fmt.Print("Enter your amount: ")
	fmt.Scan(&amount)
	var rates = map[string]float32{
		"ab": 0.05, "bc": 0.12, "mn": 0.12,
		"nb": 0.15, "nl": 0.15, "ns": 0.15, "nu": 0.05,
		"on": 0.13, "qc": 0.14975, "pei": 0.15, "nt": 0.05,
		"sk": 0.11, "yt": 0.05}
	var total int = amount*int(rates[prov]) + amount
	fmt.Print(total)
	fmt.Print("Ignore the percent sign")

}
