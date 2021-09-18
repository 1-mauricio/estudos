#include <stdio.h>

int main()
{
    int menuChoice;
    printf("Chose your option: ");
    scanf("%d", &menuChoice);

    switch (menuChoice)
    {
    case 0:
        printf("Case 0\n");
        break;
    
    case 1:
        printf("Case 1\n");
        break;

    case 2:
        printf("Case 2\n");
        break;
    
    case 3:
        printf("Case 3\n");
        break;
    
    default:
        printf("Default case\n");
        break;
    }
    
}