#include <stdio.h>

int main()
{
    printf("Hello World\n");

    int x = 50;
    int y; //declaration
    y = 10; //initialization

    printf("%s World\n", "Hello");

    printf("The value of x is %d\n", x);

    printf("X: %d, Y: %d\n", x, y);

    printf("Give me a radius: ");
    int radius;
    scanf("%d", &radius); //address-of-operator (pointer)

    printf("You chose the value %d\n", radius);

    char name[20]; //char array of 20 characters. '\0' takes one spot
    scanf("%19s", name);

    printf("Your name: %s\n", name);
    return 0;
}