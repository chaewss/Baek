if __name__ == "__main__":
    a, b = map(str, input().split())

    min_v = int(a.replace('6', '5')) + int(b.replace('6', '5'))
    max_v = int(a.replace('5', '6')) + int(b.replace('5', '6'))

    print(min_v, max_v)