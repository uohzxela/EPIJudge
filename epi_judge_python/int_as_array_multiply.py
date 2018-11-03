from test_framework import generic_test


def multiply(num1, num2):
    sign = -1 if num1[0] * num2[0] < 0 else 1

    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    res = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            pdt = res[i+j+1] + num1[i] * num2[j]
            res[i+j+1] = pdt % 10
            res[i+j] += pdt // 10

    start = 0
    while start < len(res) - 1 and res[start] == 0:
        start += 1
    res[start] *= sign

    return res[start:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
