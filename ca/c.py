hdd = []
for i in range(1, 5001):  # 하드디스크값 1~5000 으로 초기화
    hdd.append(i)
ram = []  # 램
ram_info = {}
L1 = []  # 캐시 L1 5개
L1_info = {}
L2 = []  # 캐시 L2 20개
L2_info = {}
L3 = []  # 캐시 L3 200개
L3_info = {}
R1 = 0  # 레지스터 1
R2 = 0  # 레지스터 2
R3 = 0
a = 0
b = 0
approach_time = 0  # 접근시간
count = 0
hit = [0, 0, 0, 0, 0]  # L1, L2, L3, ram, hdd 각각 hit 횟수
approach_time1 = 0
approach_time2 = 0
approach_time3 = 0
c = 0

def append_data(ln, ln_info, num):  # ln에 num 넣기, ln_info 값 변경
    global count
    ln.append(num)
    count += 1
    ln_info[num] = count


def remove_data(ln, ln_info, num):  # ln의 num 지우기, ln_info 값 지우기
    ln.remove(num)
    del ln_info[num]


def remove_old_data():  # ram 이 꽉 찬 경우 선입선출로 가장 오래된 데이터 값 삭제
    min_key = 0  # 가장 먼저 들어온 데이터
    for min_key in ram_info:
        break
    for ram_key in ram_info:
        if ram_info[min_key] > ram_info[ram_key]:
            min_key = ram_key
    remove_data(ram, ram_info, min_key)  # ram의 가장 먼저 들어온 데이터 지움


def move_cache(ln1, ln1_info, ln2, ln2_info):  # 가장 먼저 들어온 데이터 하위 저장장치로 옮기기 ex) L1-> L2, L3->ram
    min_key = 0  # 가장 먼저 들어온 데이터
    for min_key in ln1_info:
        break
    for l_key in ln1_info:
        if ln1_info[min_key] > ln1_info[l_key]:
            min_key = l_key
    remove_data(ln1, ln1_info, min_key)  # ln1에서 ln1의 가장 먼저 들어온 데이터 지움
    append_data(ln2, ln2_info, min_key)  # ln2에 가장 먼저 들어온 ln1 데이터 넣기


def search_ln(data):  # L1, L2, L2가 있는 캐시
    global approach_time
    global count
    approach_time = 0
    approach_time += 0.1
    # 구현) len()의 초기값이 0이라 처음에는 받은 data 다 넣어야됨 => 메모리까지 내려가서 검색 후 캐시에 넣기?
    for i1 in range(0, len(L1)+1):
        if data in L1 and i1 < 5:
            # print('%d L1 hit!' % data)
            hit[0] = hit[0] + 1
            count += 1
            L1_info[data] = count  # L1_info 리스트에 입력시간 갱신
            return data
        else:
            approach_time += 0.1
            for i2 in range(0, len(L2)+1):
                if data in L2 and i2 < 20:
                    # print('%d L2 hit!' % data)
                    hit[1] = hit[1] + 1
                    # 구현) L1 에 있는 것 중 가장 먼저 들어온 데이터, 입력정보 L2로 보내고 L2 에서 있던 데이터 L1으로 넣음.
                    remove_data(L2, L2_info, data)  # L2에서 data 지움
                    move_cache(L1, L1_info, L2, L2_info)
                    append_data(L1, L1_info, data)  # l1에 data 넣기
                    return data  # 반환해서 register 에 넣기
                else:
                    approach_time += 0.1
                    for i3 in range(0, len(L3)+1):
                        if data in L3 and i3 < 200:
                            # print('%d L3 hit!' % data)
                            hit[2] = hit[2] + 1
                            # 구현) 데이터 L1으로 넣음. L1 에 있는 것 중 가장 먼저 들어온 데이터, 입력정보를 L2로 보냄. L2에서 가장 먼저 있던 데이터 L3으로 보냄.
                            remove_data(L3, L3_info, data)
                            move_cache(L2, L2_info, L3, L3_info)
                            move_cache(L1, L1_info, L2, L2_info)
                            append_data(L1, L1_info, data)
                            return data
                        else:
                            approach_time += 1  # 캐시에서 찾지 못했기 때문에 램으로 진입. 메모리 접근 시간 1초
                            for i4 in range(0, len(ram)+1):
                                if data in ram and i4 < 500:
                                    # print('%d RAM hit!' % data)
                                    hit[3] = hit[3] + 1
                                    # 구현) ram 에서 찾은 데이터 L1으로 넣음. L1 에 있는 것 중 가장 먼저 들어온 데이터, 입력정보를 L2로 보냄.
                                    #      L2에서 가장 먼저 있던 데이터 L3으로 보냄. L3에서 가장 먼저 있던 데이터 ram 으로 보냄.
                                    remove_data(ram, ram_info, data)
                                    move_cache(L3, L3_info, ram, ram_info)
                                    move_cache(L2, L2_info, L3, L3_info)
                                    move_cache(L1, L1_info, L2, L2_info)
                                    append_data(L1, L1_info, data)
                                    return data
                                else:
                                    approach_time += 3  # 하드디스크 접근 시간 3초
                                    # print('%d HDD hit!' % data)
                                    hit[4] = hit[4] + 1
                                    # 구현) hdd 에서 찾은 데이터 ram과 L1으로 넣음(Write through).
                                    # L1 에 있는 것 중 가장 먼저 들어온 데이터, 입력정보를 L2로 보냄.
                                    # L2에서 가장 먼저 있던 데이터 L3으로 보냄. L3에서 가장 먼저 있던 데이터 ram으로 보냄. ram에 가장 먼저 있던 데이터 삭제.
                                    if len(L3) == 200:
                                        if len(ram) == 500:  # ram 이 full 일 때 ram에 제일 먼저 들어온 값 삭제
                                            remove_old_data()  # 캐시에서 내려온 데이터와 hdd에서 새로 올라온 데이터를 저장하기 위해
                                            remove_old_data()  # ram에 먼저 들어왔던 데이터 2개 삭제
                                        append_data(ram, ram_info, data)
                                        move_cache(L3, L3_info, ram, ram_info)
                                        move_cache(L2, L2_info, L3, L3_info)
                                        move_cache(L1, L1_info, L2, L2_info)
                                        append_data(L1, L1_info, data)
                                        return data
                                    elif len(L2) == 20:
                                        append_data(ram, ram_info, data)
                                        move_cache(L2, L2_info, L3, L3_info)
                                        move_cache(L1, L1_info, L2, L2_info)
                                        append_data(L1, L1_info, data)
                                        return data
                                    elif len(L1) == 5:
                                        append_data(ram, ram_info, data)
                                        move_cache(L1, L1_info, L2, L2_info)
                                        append_data(L1, L1_info, data)
                                        return data
                                    else:
                                        append_data(ram, ram_info, data)
                                        append_data(L1, L1_info, data)
                                        return data


class ArrayStack:  # 스택 사용 함수들
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(expr_Str):  # 수식 후위 표현식으로 변경
    tokens = []
    val = 0
    val_processing = False

    for cc in expr_Str:
        if cc == ' ':
            continue
        if cc in '0123456789':
            val = val * 10 + int(cc)
            val_processing = True
        else:
            if val_processing:
                tokens.append(val)
                val = 0
            val_processing = False
            tokens.append(cc)

    if val_processing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):  # 스택을 사용해 계산
    prec = {
        '*': 3, '/': 3,
        '+': 2, '-': 2,
        '(': 1,
    }
    opStack = ArrayStack()
    postfixList = []
    for ch in tokenList:
        if ch in prec:
            if not opStack.isEmpty():
                if ch != '(' and prec[ch] <= prec[opStack.peek()]:
                    postfixList.append(opStack.pop())
            opStack.push(ch)

        elif ch == ')':
            while True:
                temp = opStack.pop()
                if temp == '(':
                    break
                postfixList.append(temp)

        else:
            postfixList.append(ch)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):  # 사칙연산 계산
    global a, b
    temp = ArrayStack()
    for x in tokenList:
        if type(x) == int:
            temp.push(x)
        else:
            a = temp.pop()
            b = temp.pop()
        if x == '+':
            temp.push(a + b)
        elif x == '-':
            temp.push(b - a)
        elif x == '*':
            temp.push(a * b)
        elif x == '/':
            temp.push(b / a)
    answer = temp.pop()
    return answer


def solution(expr):   # main 에서 이걸로 호출, 수식 바꾸고 숫자 찾고 레지스터에 넣고 계산 
    global R1, R2, R3
    tokens = splitTokens(expr)
    global c, approach_time1, approach_time2, approach_time3
    c = 0
    n = 0
    for r in tokens:
        if r not in ['+', '*', '-', '/', '(', ')', ' ']:
            if c == 0:
                r = int(r)
                R1 = search_ln(r)
                c = c + 1
                tokens[n] = R1
                approach_time1 = approach_time
            elif c == 1:
                R2 = search_ln(int(r))
                c = c + 1
                tokens[n] = R2
                approach_time2 = approach_time
            else:
                R3 = search_ln(int(r))
                c = c + 1
                tokens[n] = R3
                approach_time3 = approach_time
        n = n + 1
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    tokens.clear()
    return val


if __name__ == '__main__':
    # L1, L2, L3 있는 캐시
    SIZE = [5]
    hit_ratio_li = []
    miss_ratio_li = []
    approach_time_li = []
    print('==================================사칙연산 계산기==================================')
    for i in SIZE:
        ram.clear()
        ram_info.clear()
        L1.clear()
        L1_info.clear()
        L2.clear()
        L2_info.clear()
        L3.clear()
        L3_info.clear()
        for j in range(0, i):
            print(j + 1, '번째')
            print('계산할 식 입력 : ', end="")  # 수의 범위 1~15
            expression = input()
            print('연산 결과 : %0.2f' % solution(expression))
            print('R1 : ', R1, ', 속도 : ', approach_time1)
            print('R2 : ', R2, ', 속도 : ', approach_time2)
            if c != 2:
                print('R3 : ', R3, ', 속도 : ', approach_time3)

            print()
            print('L1 : ', L1)
            print('L1_info : ', L1_info)
            print('L2 : ', L2)
            print('L2_info : ', L2_info)
            print('L3 : ', L3)
            print('L3_info : ', L3_info)
            print('ram : ', ram)
            print('ram_info : ', ram_info)
            print()
            print()
        print('-----------------------------------------------------------------------------')
        print()
        hit_ratio = (hit[0]+hit[1]+hit[2])/(i*2)*100
        miss_ratio = int(100-hit_ratio)
        print('총 hit 율(L1+L2+L3) %0.1f%%: ' % hit_ratio)
        hit_ratio_li.append(hit_ratio)
        print('miss 율(ram + hdd 접근율) : %0.1f%%' % miss_ratio)
        miss_ratio_li.append(miss_ratio)
        print()
        print('=====================================종료=====================================')
