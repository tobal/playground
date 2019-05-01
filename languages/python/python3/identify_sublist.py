#!/usr/bin/env python3
#
# The program does not take input parameters, just runs
# on the example test data. To feed it with your own data,
# you should use it as a module in your own script, like so:
#
# from identify_sublist import identify_sublist
# 

import sys
from operator import itemgetter


def identify_sublist(digit_charlist):
    def same_digit_char_num(digit_charlist):
        overall_sum = sum([ -1 if isinstance(x, int) else 1 for x in digit_charlist])
        return (overall_sum == 0)

    candidate_sublists_and_lengths = [((idx_begin, idx_end), idx_end - idx_begin)
            for idx_begin in range(len(digit_charlist))
            for idx_end in range(idx_begin, len(digit_charlist))
            if same_digit_char_num(digit_charlist[idx_begin:idx_end + 1])]
    if not candidate_sublists_and_lengths:
        print("No candidate sublists")
        sys.exit(1)
    indexes_of_longest_sublist = max(candidate_sublists_and_lengths, key=itemgetter(1))[0]
    return indexes_of_longest_sublist

    # Here is the same code which I wrote first, but wanted to get rid of the
    # state variables. This one is easier to read though
    #max_begin = max_end = 0
    #for idx_begin in range(len(digit_charlist)):
    #    for idx_end in range(len(digit_charlist)):
    #        if same_digit_char_num(digit_charlist[idx_begin:idx_end + 1]):
    #            if ((idx_end - idx_begin) > (max_end - max_begin)):
    #                max_begin = idx_begin
    #                max_end = idx_end
    #return (max_begin, max_end)


if __name__ == "__main__":
    test_charlist = [0, 'a', 'c', 4, 1, 2, 'b', 0, 2, 3]
    (idx_begin, idx_end) = identify_sublist(test_charlist)
    assert idx_begin == 1
    assert idx_end == 6
    sys.exit(0)
