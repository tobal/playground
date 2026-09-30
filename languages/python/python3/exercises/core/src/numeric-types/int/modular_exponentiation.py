'''
1.3 Hard: Fast Modular Exponentiation Without Overflow

     * Goal: Implement custom_pow_mod(base: int, exp: int, mod: int) -> int.
     * Description: Compute (base ** exp) % mod using the binary exponentiation algorithm (repeated
       squaring) in $O(log(\text{exp}))$ time complexity, without using Python's built-in 3-argument pow()
       or computing base ** exp directly.
     * Key Takeaway: Large exponents (2 ** 1000000) can consume gigabytes of memory if evaluated before
       modulo. Taking modulo at every intermediate multiplication keeps space complexity $O(1)$ and avoids
       memory exhaustion.
     * Expected Behavior:
          + custom_pow_mod(2, 10, 1000) -> 24
          + custom_pow_mod(7, 256, 13) -> 9
          + Raises ValueError if exp < 0 or mod <= 0.
'''

def custom_pow_mod(base: int, exp: int, mod: int) -> int:
    if exp < 0:
        raise ValueError('Negative exponent')
    if mod <= 0:
        raise ValueError('Modulo not positive')

    if exp == 0:
        return 1

    if exp % 2 == 0:
        result = custom_pow_mod(base, exp // 2, mod)
        return (result * result) % mod 
    else:
        return (base * custom_pow_mod(base, exp - 1, mod) % mod)
