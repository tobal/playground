'''
** 3.1 Easy: Conjugate & Polar Magnitude
- *Goal*: Implement ~analyze_complex(z: complex) -> tuple[float, float, complex]~.
- *Description*: Given a complex number ~z~, return a tuple containing its real part, imaginary part, and complex conjugate.
- *Key Takeaway*: Complex numbers in Python are built-in primitives (~3 + 4j~). Conjugates (~z.conjugate()~) flip the imaginary sign, essential for computing magnitude squared ~$z \\cdot \\bar{z} = a^2 + b^2$~.
- *Expected Behavior*:
  - ~analyze_complex(3 + 4j)~ -> ~(3.0, 4.0, (3-4j))~
  - ~analyze_complex(5.0)~ -> ~(5.0, 0.0, (5+0j))~
'''

def analyze_complex(z: complex) -> tuple[float, float, complex]:
    return (z.real, z.imag, z.conjugate())
