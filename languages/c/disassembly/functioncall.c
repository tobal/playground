int foo(int param)
{
    int varFoo = 2 + param;
    return varFoo;
}

int main(void)
{
    int varMain = 1;
    // prolog
    int ret = foo(varMain);
    // epilog
    return ret;
}
