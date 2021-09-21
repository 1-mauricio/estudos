#include <stdio.h>
#include "libraries.h"

int main()
{
    int size = 7;
    int ages[] = {1,4,53,23,23,9,52};
    printf("%d\n", oldestValue(ages, size));
    return 0;
}