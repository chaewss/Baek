if __name__ == '__main__':
    n = int(input())
    total = 0
    for i in range(1, n):
        total += n * i + i
    print(total)
