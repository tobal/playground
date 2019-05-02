#!/usr/bin/env python3
#
# The program does not take command line parameters, just runs
# on the example test data. To feed it with your own data,
# you should use it as a module in your own script. Import
# the function and it's exception class, and put the call
# in a try block to handle any errors.


import sys
from operator import itemgetter


class InputError(Exception):
    pass


def identify_sublist(digit_charlist):
    def same_digit_char_num(digit_charlist):
        overall_sum = sum([ -1 if isinstance(x, int) else 1 for x in digit_charlist])
        return (overall_sum == 0)

    candidate_sublists_and_lengths = [((idx_begin, idx_end), idx_end - idx_begin)
            for idx_begin in range(len(digit_charlist))
            for idx_end in range(idx_begin, len(digit_charlist))
            if same_digit_char_num(digit_charlist[idx_begin:idx_end + 1])]
    if not candidate_sublists_and_lengths:
        raise InputError("No candidate sublists")
    indexes_of_longest_sublist = max(candidate_sublists_and_lengths, key=itemgetter(1))[0]
    return indexes_of_longest_sublist


if __name__ == "__main__":
    test_charlist = [0, 'a', 'c', 4, 1, 2, 'b', 0, 2, 3]
    try:
        (idx_begin, idx_end) = identify_sublist(test_charlist)
    except InputError as exc:
        print(exc)
        sys.exit(1)

    assert idx_begin == 1
    assert idx_end == 6
    sys.exit(0)
