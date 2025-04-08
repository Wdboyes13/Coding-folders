#include <stdio.h>
#include <string.h>
int main(){
    string name;
    printf("Enter your name: ");
    scanf("%s", name);
    printf("I love %s", name, "balls!");
    return 0;
}