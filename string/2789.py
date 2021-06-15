if __name__ == "__main__":
    word = input()

    for i in "CAMBRIDGE":
        word = word.replace(i, "")
    print(word)
