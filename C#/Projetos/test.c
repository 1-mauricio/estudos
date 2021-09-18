#include <stdio.h>

int main() {
    int aux = 5;
    for (int i = 0; i < aux; i++) {
        if (i % 2 == 0){
            printf("%i é Par\n", i);
        } else {
            printf("%i é impar\n", i);
        }
    }
    return 0;
}