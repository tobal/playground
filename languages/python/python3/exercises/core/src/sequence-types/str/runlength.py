'''
1.2 Medium: Run-Length Encoding with Validation

     * Goal: Implement run_length_encode(s: str) -> str.
     * Description: Compress run lengths of consecutive identical characters into "Ccount" format (e.g.,
       "AAABBC" -> "A3B2C1"). Raise ValueError if the input string contains any numeric digits.
     * Key Takeaway: String concatenation in loops can incur $O(N^2)$ copying costs unless collected in
       list buffers or built via generators. Input validation prevents parsing ambiguity during decoding.
     * Expected Behavior:
          + run_length_encode("AAABBC") -> "A3B2C1"
          + run_length_encode("a") -> "a1"
          + run_length_encode("") -> ""
          + Raises ValueError for "A2B".
'''
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass


def run_length_encode(s: str) -> str:
    # there has to be a better way of doing this
    if any(c.isdigit() for c in s):
        raise ValueError
    d = OrderedCounter(s)
    s_out = ""
    for k, v in d.items():
        s_out += k
        s_out += str(v)
    return s_out
