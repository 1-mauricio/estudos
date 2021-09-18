#include <stdio.h>

int main() {
    int size = 8;
    int ages[] = {1, 4, 60, 43, 54, 3, 90, 21};
    for (int i = 0; i < size; i++)
    {
        printf("%d ", ages[i]);
    }

    printf("\n");
    ages[3] = 60;
    for (int i = 0; i < size; i++)
    {
        printf("%d ", ages[i]);
    }

    return 0;
}