if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        if i < x:
            print(i, end=" ")
