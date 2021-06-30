if __name__ == '__main__':
    x, y, w, s = map(int, input().split())

    # 평행 이동
    straight = (x + y) * w

    # 최대한의 대각선 이동
    if (x + y) % 2 == 0:
        cross = max(x, y) * s
    else:
        cross = (max(x, y) - 1) * s + w

    # 평행이동 + 대각선 이동
    mix = (min(x, y) * s) + ((max(x, y) - min(x, y)) * w)

    print(min(min(straight, cross), mix))
