if __name__ == '__main__':
    for _ in range(int(input())):
        blank = input()
        r, c = map(int, input().split())
        candy = 0
        box = []
        for _ in range(r):
            box += input().split()

        # '>o<' 모양의 사탕이 있는지 확인
        for i in range(r):
            for j in range(c - 2):
                if box[i][j:j+3] == '>o<':
                    candy += 1

        # 'vo^' 모양의 사탕이 있는지 확인
        for i in range(r-2):
            for j in range(c):
                vertical = box[i][j] + box[i+1][j] + box[i+2][j]
                if vertical == 'vo^':
                    candy += 1

        print(candy)
