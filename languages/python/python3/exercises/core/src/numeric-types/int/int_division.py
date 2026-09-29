'''
1.1 Easy: Integer Division & Type Coercion

     * Goal: Implement a function divide_integer_modes(a: int, b: int) -> tuple[int, float, int].
     * Description: Compute exact integer floor division, true float division, and modulo in a single
       tuple.
     * Key Takeaway: True division (/) always returns a float even when the quotient is an exact integer,
       whereas floor division (//) preserves integer typing when given integers.
     * Expected Behavior:
          + Input: (10, 3) -> Output: (3, 3.3333333333333335, 1)
          + Input: (10, 2) -> Output: (5, 5.0, 0)
          + Raises ZeroDivisionError if b == 0.
'''

def divide_integer_modes(a: int, b: int) -> tuple[int, float, int]:
    return (a // b, a / b, a % b)
