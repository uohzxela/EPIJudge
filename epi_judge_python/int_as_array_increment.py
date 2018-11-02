from test_framework import generic_test


def plus_one(A):
    carry = 1
    for i in range(len(A) - 1, -1 , -1):
        if carry == 0:
            break
        A[i] += carry
        carry = A[i] // 10
        A[i] %= 10
    if carry:
        A.append(0)
        A[0] = 1
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
