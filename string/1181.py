if __name__ == '__main__':
    voca_li = []
    for _ in range(int(input())):
        voca = input()
        num = len(voca)
        voca_li.append((num, voca))
    voca_li = list(set(voca_li))

    print(voca_li)
    voca_li.sort(key=lambda x: (x[0], x[1]))

    for voca in voca_li:
        print(voca[1])
