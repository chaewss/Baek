if __name__ == '__main__':
    a, b = map(int, input().split())
    sequence = []
    for i in range(b//2+2):
        sequence += [i] * i

    print(sum(sequence[a-1:b]))
