# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    m1 = -1
    t1 = -1
    m2 = -1
    for first in range(n):
        if m1 < numbers[first]:
            m1 = numbers[first]
            t1 = first
    for second in range(n):
            if (second != t1) and numbers[second] > m2:
                m2 = numbers[second]
    return (m1 * m2)


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
