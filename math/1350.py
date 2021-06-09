if __name__ == '__main__':
    n = int(input())
    f_size = list(map(int, input().split()))
    c_size = int(input())

    used = 0
    for i in f_size:
        if i % c_size == 0:
            used += i // c_size
        else:
            used += i // c_size + 1

    print(used * c_size)