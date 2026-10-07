'''
3.3 Hard: Robust Complex Division Guarding Overflow

     * Goal: Implement safe_complex_div(z1: complex, z2: complex) -> complex.
     * Description: Implement complex division $\frac{a+bi}{c+di} = \frac{(ac+bd) + (bc-ad)i}{c^2+d^2}$
       manually using Smith's scaled division algorithm to prevent intermediate numeric overflow when
       $|c|$ or $|d|$ is very large.
     * Key Takeaway: Naively computing $c^2 + d^2$ can overflow float limits ($> 1.79  10^308$) even when
       the overall quotient is well within representable float bounds.
     * Expected Behavior:
          + safe_complex_div(1 + 2j, 3 + 4j) -> (0.44 + 0.08j)
          + safe_complex_div(1 + 1j, 1e200 + 1e200j) -> (1e-200 + 0j)
          + Raises ZeroDivisionError if z2 == 0j.
'''

def safe_complex_div(z1: complex, z2: complex) -> complex:
    # naive implementation
    #nominator_real = (z1.real*z2.real + z1.imag*z2.imag) 
    #nominator_imag = (z1.imag*z2.real - z1.real*z2.imag)
    #denominator = z2.real * z2.real + z2.imag * z2.imag
    #ret_real = nominator_real / denominator
    #ret_imag = nominator_imag / denominator
    #return complex(ret_real, ret_imag)
    a, b = z1.real, z1.imag
    c, d = z2.real, z2.imag
    if d == 0:
        raise ZeroDivisionError
    if abs(d) <= abs(c):
        r = d / c
        denominator = c + d*r
        x = (a + b*r) / denominator
        y = (b - a*r) / denominator
    else:
        r = c / d
        denominator = c*r + d
        x = (a*r + b) / denominator
        y = (b*r - a) / denominator
    return complex(x, y)
