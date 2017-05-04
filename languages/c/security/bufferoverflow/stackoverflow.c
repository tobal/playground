#pragma check_stack(off)

#include <string.h>
#include <stdio.h>

void foo(const char* input)
{
    char buf[10];

    printf("Stack:\n%p\n%p\n%p\n%p\n%p\n%p\n\n");
    strcpy(buf, input);
    printf("%s\n", buf);
    printf("Stack:\n%p\n%p\n%p\n%p\n%p\n%p\n\n");
}

void bar(void)
{
    printf("Secret function called\n");
}

int main(int argc, char* argv[])
{
    printf("&foo = %p\n", foo);
    printf("&bar = %p\n", bar);
    if (argc != 2)
    {
        printf("Supply a string as argument\n");
        return -1;
    }
    foo(argv[1]);
    return 0;
}
