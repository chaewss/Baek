import math

if __name__ == '__main__':
    d, h, w = map(int, input().split())

    x = math.sqrt(d ** 2 / (h ** 2 + w ** 2))
    height = math.floor(h * x)
    width = math.floor(w * x)

    print(height, width)
