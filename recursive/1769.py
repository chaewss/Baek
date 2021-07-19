if __name__ == '__main__':
    x = input()

    if x == '0' or x == '3' or x == '6' or x == '9':
        print(0)
        print("YES")
        exit()

    cnt = 0
    while True:
        conversion = 0
        for i in x:
            conversion += int(i)
        x = str(conversion)
        cnt += 1
        if len(x) == 1:
            break

    print(cnt)
    if int(x) % 3 == 0:
        print("YES")
    else:
        print("NO")