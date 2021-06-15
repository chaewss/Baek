if __name__ == "__main__":
    n, information = int(input()), input().replace("LL", "L")

    if information.count('L') > 0:
        print(len(information) + 1)
    else:
        print(n)
