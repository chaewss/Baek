if __name__ == '__main__':
    for _ in range(int(input())):
        c = int(input())

        print(c // 25, end=' ')
        c %= 25
        print(c // 10, end=' ')
        c %= 10
        print(c // 5, end=' ')
        c %= 5
        print(c // 1)
