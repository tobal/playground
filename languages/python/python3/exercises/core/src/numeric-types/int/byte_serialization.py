'''
1.2 Medium: Arbitrary Precision & Byte Serialization

     * Goal: Implement two conversion functions: int_to_signed_bytes(n: int) -> bytes and
       signed_bytes_to_int(b: bytes) -> int.
     * Description: Convert an arbitrary precision integer into its minimal big-endian signed
       two's-complement byte representation, and back.
     * Key Takeaway: Python integers have unlimited precision (bounded only by available RAM), but
       low-level/binary interactions require explicit byte sizing via n.to_bytes() and int.from_bytes().
     * Expected Behavior:
          + int_to_signed_bytes(0) -> b'\x00'
          + int_to_signed_bytes(-128) -> b'\x80'
          + int_to_signed_bytes(1000) -> b'\x03\xe8'
          + Round-trip constraint: signed_bytes_to_int(int_to_signed_bytes(n)) == n for any integer n.
'''

def int_to_signed_bytes(n: int) -> bytes:
    length = (n.bit_length() + 8) // 8
    return n.to_bytes(length, signed=True)


def signed_bytes_to_int(b: bytes) -> int:
    return int.from_bytes(b, signed=True)
