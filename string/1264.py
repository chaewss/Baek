if __name__ == '__main__':
    vowels = ['a', 'e', 'i', 'o', 'u']
    while True:
        sentence = input().lower()
        if sentence == '#':
            break

        cnt = 0
        for i in sentence:
            if i in vowels:
                cnt += 1
        print(cnt)
