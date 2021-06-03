if __name__ == '__main__':
    n = int(input())
    student_li = []

    for i in range(n):
        weight, height = map(int, input().split())
        student_li.append((weight, height))

    print(student_li)
    for i in student_li:
        rank = 1
        for j in student_li:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        print(rank, end=" ")
