if __name__ == '__main__':
    n, k = map(int, input().split())
    measures = list(map(int, input().split()))

    max_v = -987654321
    for i in range(n - k + 1):
        sum_v = 0
        for j in range(k):
            sum_v += measures[i + j]
        max_v = max(sum_v, max_v)
    print(max_v)
