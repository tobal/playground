#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[10];
    int pass = 0;

    printf("Enter password: \n");
    gets(buff);

    if(strcmp(buff, "titkos"))
    {
        printf("Wrong\n");
    }
    else
    {
        printf("Correct\n");
        pass = 1;
    }

    if(pass)
    {
        printf("The system is yours\n");
    }
    return 0;
}
