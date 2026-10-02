'''
2.1 Easy: Safe Float Equality Comparison

     * Goal: Implement is_float_close(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 0.0) ->
       bool.
     * Description: Determine if two floating-point numbers are effectively equal given relative and
       absolute tolerances, without using math.isclose().
     * Key Takeaway: Due to IEEE 754 binary representation limitations, simple arithmetic like 0.1 + 0.2
       == 0.3 evaluates to False (0.30000000000000004). Direct float equality == should almost never be
       used in production algorithms.
     * Expected Behavior:
          + is_float_close(0.1 + 0.2, 0.3) -> True
          + is_float_close(1e-9, 2e-9, abs_tol=1e-8) -> True
          + is_float_close(1.0, 1.001, rel_tol=1e-4) -> False
'''
def is_float_close(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 0.0) -> bool:
    difference = abs(a - b)
    scaled_relative_tolerance = rel_tol * max(abs(a), abs(b))
    return difference <= max(scaled_relative_tolerance, abs_tol)
