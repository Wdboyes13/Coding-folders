var prov = prompt("Enter your provinces 2-Digit code in all caps: ");
var amount = prompt("Enter your amount: ");
var rates = {
    "BC": 0.12, "AB": "0.05", "MN": 0.12, "NB": 0.15,
    "NL":0.15, "NT": 0.05, "NS": 0.15, "NU": 0.05,
    "ON": 0.13, "QC": 0.14975, "PEI": 0.15, "SK": 0.11, "YT": 0.05
};
total = String(parseFloat(amount) * rates[prov] + parseFloat(amount));
document.getElementById("1").innerHTML = "Total is: " + total;