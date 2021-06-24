if __name__ == '__main__':
    room_num = input().replace('9', '6')
    frequent = [0] * 9  # 0부터 8까지

    for i in room_num:
        frequent[int(i)] = room_num.count(i)
    frequent[6] = frequent[6] // 2 + frequent[6] % 2

    print(max(frequent))
