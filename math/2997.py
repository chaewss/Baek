import sys

if __name__ == '__main__':
    temp = sorted(list(map(int, sys.stdin.readline().split())))
    first_d = temp[1] - temp[0]
    second_d = temp[2] - temp[1]

    if first_d == second_d:
        print(temp[2] + second_d)
    elif first_d < second_d:
        print(temp[2] - min(first_d, second_d))
    else:
        print(temp[1] - min(first_d, second_d))