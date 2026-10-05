'''
** 3.2 Medium: Manual String Parsing of Complex Literals
- *Goal*: Implement ~parse_complex_str(s: str) -> complex~.
- *Description*: Parse strings formatted as ~"a+bj"~, ~"a-bj"~, ~"bj"~, ~"a"~, or ~"-bj"~ into native Python ~complex~ objects without using ~eval()~ or the built-in ~complex()~ constructor.
- *Key Takeaway*: Python uses ~j~ or ~J~ for the imaginary unit (engineering convention), not ~i~. Parsing complex input manually requires handling optional signs for both real and imaginary components.
- *Expected Behavior*:
  - ~parse_complex_str("3+4j")~ -> ~3 + 4j~
  - ~parse_complex_str("-2.5-1.5j")~ -> ~-2.5 - 1.5j~
  - ~parse_complex_str("-4j")~ -> ~-4j~
  - ~parse_complex_str("10.5")~ -> ~10.5 + 0j~
'''

import re


def parse_complex_str(s: str) -> complex:
    """Manually parses complex string numbers without using complex(str) or eval()."""
    # 1. Clean whitespace and normalize engineering 'i'/'I' to 'j'
    cleaned = "".join(s.split()).replace("i", "j").replace("I", "j").lower()

    # 2. Match optional real part and/or optional imaginary part ending in 'j'
    pattern = re.compile(
        r"^(?:(?P<real>[+-]?\d+(?:\.\d+)?)(?![0-9.j]))?(?P<imag>[+-]?(?:\d+(?:\.\d+)?)?j)?$"
    )
    match = pattern.match(cleaned)

    if not match or not cleaned or (match.group("real") is None and match.group("imag") is None):
        raise ValueError(f"Invalid complex string: {s}")

    real_str = match.group("real")
    imag_str = match.group("imag")

    # 3. Parse real component
    real = float(real_str) if real_str else 0.0

    # 4. Parse imaginary component
    if imag_str is None:
        imag = 0.0
    else:
        imag_num = imag_str[:-1]  # Strip trailing 'j'
        if imag_num in ("", "+"):
            imag = 1.0
        elif imag_num == "-":
            imag = -1.0
        else:
            imag = float(imag_num)

    # 5. Construct using pure float primitives
    return complex(real, imag)
