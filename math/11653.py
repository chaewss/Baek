if __name__ == '__main__':
    n = int(input())

    i = 2
    while n != 1:
        if n % i == 0:
            n /= i
            print(i)
            i = 2
            continue
        i += 1

