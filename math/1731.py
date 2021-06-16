if __name__ == "__main__":
    num = []
    for _ in range(int(input())):
        num.append(int(input()))

    if num[1] - num[0] == num[2] - num[1]:
        print(num[len(num) - 1] + (num[1] - num[0]))
    elif num[1] // num[0] == num[2] // num[1]:
        print(num[len(num) - 1] * (num[1] // num[0]))
