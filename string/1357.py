if __name__ == '__main__':
    x, y = input().split()
    plus = int(str(int(x[::-1]) + int(y[::-1]))[::-1])
    print(plus)
