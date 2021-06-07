if __name__ == '__main__':
    n = int(input())
    time_li = [int(x) for x in input().split()]

    ys = 0
    ms = 0
    for i in time_li:
        ys += (i//30 + 1) * 10
        ms += (i//60 + 1) * 15

    if ys < ms:
        print("Y", ys)
    elif ys == ms:
        print("Y M", ms)
    else:
        print("M", ms)