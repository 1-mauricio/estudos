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

int main()
{
    bool end1 = false;
    bool continue2 = true;

    while (!end1)
    {
        printf("Input some number to calculate its square and cube (0 to stop): ");
        int x;
        scanf("%d", &x);
        if (x == 0)
        {
            end1 = true;
        } else
        {
            int xSquare = square(x);
            int xCube = cube(x);
            
            printf("%d Square is %d\n", x, xSquare);
            printf("%d Cube is %d\n", x, xCube);
        }
    }

    printf("");

    while (continue2)
    {
        printf("Now input some other number(0 to stop): ");
        int y;
        scanf("%d", &y);
        if (y == 0)
        {
            continue2 = false;
        } else
        {
            printf("Great! What about the exponent? ");
            int exponent;
            scanf("%d", &exponent);

            int result = power(y, exponent);
            int resultRecursive = recursivePower(y, exponent);

            printf("%d^%d is %d\n", y, exponent, result);
            printf("Recursive: %d^%d is %d\n", y, exponent, resultRecursive);
        }
    }

    return 0;
}