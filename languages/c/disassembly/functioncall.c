int foo(int param)
{
    int varFoo = 2 + param;
    return varFoo;
}

int main(void)
{
    int varMain = 1;
    int ret = foo(varMain);
    return ret;
}
