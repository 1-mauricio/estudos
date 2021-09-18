#include <stdio.h>
#include <stdbool.h>

int main()
{
    int age = 17;
    double money = 30000;
    bool isGraduated = true; 
    if ((age > 17 && money > 2500) || isGraduated) // ! - && - ||
    {
        printf("This is true\n");
    }
    if (age > 17 && (money > 2500 || isGraduated))
    {
        printf("This is true");
    }
    else
    {
        printf("This is false\n");
    }
    return 0;
}