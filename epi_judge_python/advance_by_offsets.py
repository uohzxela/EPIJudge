from test_framework import generic_test


def can_reach_end(A):
    max_pos = 0
    for i in range(len(A)):
        if i > max_pos:
            return False
        max_pos = max(A[i] + i, max_pos)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
