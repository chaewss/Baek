if __name__ == '__main__':
    wave = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
    while True:
        n = input()
        if n == '#':
            break

        result = 0
        for i in range(len(n)):
            result += wave[n[i]] * 8 ** (len(n)-i-1)
        print(result)
