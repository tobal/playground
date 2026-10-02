'''
2.3 Hard: Exact Rational Decomposition & Negative Zero Detection

     * Goal: Implement decompose_float(f: float) -> tuple[int, int, bool].
     * Description: Decompose a float into its exact numerator, denominator (as simplified fraction tuple
       n/d), and a boolean flag indicating whether the input float was negative zero (-0.0).
     * Key Takeaway: IEEE 754 floats support dual signed zero (0.0 and -0.0). While 0.0 == -0.0 is True,
       their IEEE bit patterns and behavior in operations like atan2 or division (1.0 / -0.0 -> -inf)
       differ.
     * Expected Behavior:
          + decompose_float(0.75) -> (3, 4, False)
          + decompose_float(-0.0) -> (0, 1, True)
          + decompose_float(0.0) -> (0, 1, False)
'''

from math import copysign

def decompose_float(f: float) -> tuple[int, int, bool]:
    (numerator, denominator) = f.as_integer_ratio()
    return (numerator, denominator, _is_negative_zero(f))


def _is_negative_zero(f: float) -> bool:
    return f == 0.0 and copysign(1.0, f) < 0.0
