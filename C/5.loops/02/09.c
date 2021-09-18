#include <stdio.h>

int main()
{
    int i = 0;
    while (i < 10)
    {
        printf("%d ", i);
        i++;
    }

    int input;
    do
    {
        printf("Choose a number between 0 and 9: ");
        scanf("%d", &input);
    } while (input < 0 || input > 9);
    
    return 0;
}