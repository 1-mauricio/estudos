#include <stdio.h>
#include <stdbool.h>

int square(int input)
{
    return input * input;
}

int cube (int input)
{
    int x = input * input * input;
    return x;
}

int power(int input, int exponent)
{
    int total = 1;
    for (int i = 0; i < exponent; i++)
    {
        total *= input;
    }
    return total;    
}

int recursivePower (int input, int exponent)
{
    return input * recursivePower(input, exponent - 1);
}

// void functions can't return
void changeVal(int *input)
{
    *input = 900000;
}
int main()
{
    int x = 5;
    changeVal(&x);
    printf("%d\n", x);

    return 0;
}