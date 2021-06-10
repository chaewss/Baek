if __name__ == '__main__':
    number = [int(input()) for _ in range(10)]

    print(round(sum(number) / 10))
    print(max(number, key=number.count))