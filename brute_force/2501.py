import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    divisor = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)

    if len(divisor) < k:
        print(0)
    else:
        print(divisor[k-1])
