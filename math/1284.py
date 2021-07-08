if __name__ == '__main__':
    while True:
        n = input()
        width = 1
        if n == '0':
            break
        for i in n:
            if i == '0':
                width += 4
            elif i == '1':
                width += 2
            else:
                width += 3
            width += 1
        print(width)
