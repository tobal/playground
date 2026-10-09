'''
4.1 Easy: Boolean Subtyping & Explicit Type Verification

     * Goal: Implement count_pure_booleans(items: list[typing.Any]) -> tuple[int, int].
     * Description: Iterate over a list of mixed objects and return (true_count, false_count) counting
       only pure bool instances.
     * Key Takeaway: bool is a direct subclass of int in Python (isinstance(True, int) is True and True +
       True == 2). To distinguish pure booleans from integers, type(x) is bool must be checked instead of
       isinstance(x, int).
     * Expected Behavior:
          + count_pure_booleans([True, 1, 0, False, "True", True]) -> (2, 1)
'''
import typing

def count_pure_booleans(items: list[typing.Any]) -> tuple[int, int]:
    only_bools = [x for x in items if type(x) is bool]
    true_count = only_bools.count(True)
    false_count = len(only_bools) - true_count
    return (true_count, false_count)
