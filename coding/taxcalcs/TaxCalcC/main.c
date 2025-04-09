#include <stdio.h>
#include <string.h>
int main() {

	char in[] = "";
	int amount;

	printf("Enter your 2 letter province code in all caps: ");
	scanf("%s", in);

	printf("Enter the amount: ");
	scanf("%d", &amount);


	double BC = 0.12;
	double AB = 0.05;
	double MN = 0.12;
	double NB = 0.15;
	double NL = 0.15;
	double NT = 0.05;
	double NS = 0.15;
	double NU = 0.05;
	double ON = 0.13;
	double QC = 0.14975;
	double PEI = 0.15;
	double SK = 0.11;
	double YT = 0.05;


	int isbc = strcmp(in, "BC");
	int isab = strcmp(in, "AB");
	int ismn = strcmp(in, "MN");
	int isnb = strcmp(in, "NB");
	int isnl = strcmp(in, "NL");
	int isnt = strcmp(in, "NT");
	int isns = strcmp(in, "NS");
	int isnu = strcmp(in, "NU");
	int ison = strcmp(in, "ON");
	int isqc = strcmp(in, "QC");
	int ispei = strcmp(in, "PEI");
	int issk = strcmp(in, "SK");
	int isyt = strcmp(in, "YT");


	int total;

	if (isbc == 0) {
		total = amount*BC+amount;
		printf("Total is: %d\n", total);
		}

	if (isab == 0) {
			total = amount*AB+amount;
			printf("Total is: %d\n", total);
		}

	if (ismn == 0) {
			total = amount*MN+amount;
			printf("Total is: %d\n", total);
		}

	if (isnb == 0) {
			total = amount*NB+amount;
			printf("Total is: %d\n", total);
		}

	if (isnl == 0) {
			total = amount*NL+amount;
			printf("Total is: %d\n", total);
		}

	if (isnt == 0) {
			total = amount*NT+amount;
			printf("Total is: %d\n", total);
		}

	if (isns == 0) {
			total = amount*NS+amount;
			printf("Total is: %d\n", total);
		}

	if (isnu == 0) {
			total = amount*NU+amount;
			printf("Total is: %d\n", total);
		}

	if (ison == 0) {
			total = amount*ON+amount;
			printf("Total is: %d\n", total);
		}

	if (isqc == 0) {
			total = amount*QC+amount;
			printf("Total is: %d\n", total);
		}
	if (ispei == 0) {
			total = amount*PEI+amount;
			printf("Total is: %d\n", total);
		}
	if (issk == 0) {
			total = amount*SK+amount;
			printf("Total is: %d\n", total);
		}
	if (isyt == 0) {
			total = amount*YT+amount;
			printf("Total is: %d\n", total);
		}

}
