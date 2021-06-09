if __name__ == "__main__":
    word = input().upper()
    word_set = list(set(word))

    result = []
    for i in word_set:
        cnt = word.count(i)
        result.append(cnt)

    if result.count(max(result)) > 1:
        print("?")
    else:
        m = result.index(max(result))
        print(word_set[m])
