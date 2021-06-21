if __name__ == '__main__':
    for _ in range(int(input())):
        location, voca = input().split()
        location = int(location)
        print(voca[0:location - 1] + voca[location:])
