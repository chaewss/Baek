if __name__ == '__main__':
    for _ in range(int(input())):
        repeat, s = input().split()

        for i in range(len(s)):
            for j in range(int(repeat)):
                print(s[i], end='')
        print()
