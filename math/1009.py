if __name__ == '__main__':
    t = int(input())
    results = []

    for i in range(t):
        a, b = map(int, input().split())

        if a % 10 == 0:
            results.append(10)
        else:
            n = b % 4 + 4
            data = str(a ** n)[-1]
            results.append(data)

    for result in results:
        print(result)