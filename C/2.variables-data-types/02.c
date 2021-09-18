#include <stdio.h>
#include <stdbool.h>

int main()
{
    int a = 10;

    double b = 10.5; //64-bits = 8 bytes
    printf("%d\n", sizeof(b));

    float c = 10.5; //32-bits = 4 bytes
    printf("%d\n", sizeof(c));

    char d = 'a'; // one letter

    char e[] = "char array"; // aka a string

    bool f = false;

    int cats; //different
    int CATS;
    int caTs;

    int zero = .99999999;
    printf("zero is %d\n", zero);

    int slices = 17;
    int people = 2;
    double slicesPerPerson = slices / people; // 8
    printf("%lf\n", slicesPerPerson);

    slicesPerPerson = (double) (slices) / people; // 8.55
    printf("%lf\n", slicesPerPerson);

    double test1 = (25 / 2) * 2; // 24.0
    double test2 = (25 / 2) * 2.0; // 24.0
    double test3 = 25.0 / 2 * 2; // 25.0
    double test = (double) 25 / 2 * 2.0; //25.0
    return 0; 
}