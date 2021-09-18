#include <stdio.h>

int main()
{
    int size = 10;
    int ages[] = {12, 43, 545, 3, 4, 54, 6, 7, 87, 12};
    int calculatesSize = sizeof(ages) / sizeof(ages[0]);

    for (int i = 0; i < size; i++)
    {
        printf("ages[%d] = %d\n", i, ages[i]);
    }

    for (int i = 0; i < 10; i++)
    {
        for (int j = i; j >= 0; j--)
        {
            printf("%d ", j);
        }
        printf("\n");
    } 
    return 0;
}