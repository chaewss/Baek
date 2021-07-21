if __name__ == '__main__':
    s = input()
    alphabet = list(range(97, 123))

    for i in alphabet:
        print(s.find(chr(i)), end=' ')
