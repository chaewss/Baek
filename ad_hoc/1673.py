import sys

if __name__ == '__main__':
    for i in sys.stdin.readlines():
        n, k = map(int, i.strip().split())
        chicken = n

        while n // k:
            chicken += n // k
            n = n // k + n % k

        print(chicken)
