if __name__ == '__main__':
    s = int(input())
    cnt = 0
    sum_num = 0

    while True:
        cnt += 1
        sum_num += cnt
        if sum_num > s:
            break
    print(cnt - 1)
