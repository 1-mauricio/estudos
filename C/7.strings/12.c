#include <stdio.h>
#include <string.h>

int main()
{
    printf("What is your name? ");
    char name[20]; // '\0'
    scanf("%19s", name);

    int letter = 0;
    while (name[letter] != '\0')
    {
        letter++;
    }

    printf("Size of name is %d\n", letter);

    printf("Size of name is %lu\n", strlen(name));

    if(strcmp(name, "Mauricio") == 0) // checks if two strings are the same
    {
        printf("You get access!\n");
    }

    char copy[20];
    strcpy(copy, name);
    printf("Copy of name is: %s\n", copy);

    char lasName[] = " Curry";
    strcat(copy, lasName);
    printf("Full name: %s\n", copy);

    return 0;
}