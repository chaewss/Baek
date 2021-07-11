if __name__ == '__main__':
    n = int(input())
    room = []
    for _ in range(n):
        room += [input() + 'X']
    room.append('X' * (n+1))

    row_seat, col_seat = 0, 0
    for i in range(n + 1):
        row_cnt, col_cnt = 0, 0
        for j in range(n + 1):
            # 가로
            if room[i][j] == '.':
                row_cnt += 1
            elif room[i][j] == 'X':
                if row_cnt >= 2:
                    row_seat += 1
                row_cnt = 0
            # 세로
            if room[j][i] == '.':
                col_cnt += 1
            elif room[j][i] == 'X':
                if col_cnt >= 2:
                    col_seat += 1
                col_cnt = 0
    print(row_seat, col_seat)
