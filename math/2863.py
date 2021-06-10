if __name__ == "__main__":
    table = []
    table += map(int, input().split())
    table += list(map(int, input().split()))[::-1]

    result = []
    for i in range(4):
        s = table[0] / table[3] + table[1] / table[2]
        result.append(s)
        table = [table[-1]] + table[:-1]
    print(result.index(max(result)))
