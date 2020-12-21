from random import *
from matplotlib import pyplot as plt

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
approach_time = 0  # 접근시간
count = 0
hit = [0, 0, 0, 0, 0]  # L1, L2, L3, ram, hdd 각각 hit 횟수


def append_data(ln, ln_info, num):  # ln에 num 넣기, ln_info 값 변경
    global count
    count = 1
    ln.append(num)
    ln_info[num] = count
    ram_info[num] = count


def remove_data(ln, ln_info, num):  # ln의 num 지우기, ln_info 값 지우기
    ln.remove(num)
    del ln_info[num]


def remove_mfrequently_data(): # ram 이 꽉 찬 경우 참조횟수가 많은 데이터 값 삭제: MFU
    max_key = 0  # 참조횟수
    for max_key in ram_info:
        break
    for l_key in ram_info:
        if ram_info[max_key] < ram_info[l_key]:
            max_key = l_key
    remove_data(ram, ram_info, max_key)  # ln1에서 가장 많이 참조된 데이터 지움


def move_cache(ln1, ln1_info, ln2, ln2_info):  # 가장 많이 참조된 데이터 하위 저장장치로 옮기기 ex) L1-> L2, L3->ram
    max_key = 0  # 참조횟수
    for max_key in ln1_info:
        break
    for l_key in ln1_info:
        if ln1_info[max_key] < ln1_info[l_key]:
            max_key = l_key
    remove_data(ln1, ln1_info, max_key)  # ln1에서 가장 많이 참조된 데이터 지움
    append_data(ln2, ln2_info, max_key)  # ln2에 가장 많이 참조됐던 ln1 데이터 넣기


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
            L1_info[data] += 1  # L1_info 참조횟수 갱신
            return data
        else:
            approach_time += 0.1
            for i2 in range(0, len(L2)+1):
                if data in L2 and i2 < 20:
                    hit[1] = hit[1] + 1
                    L2_info[data] += 1
                    # print('%d L2 hit!, count: %d' % (data, count))
                    # 구현) L1 에 있는 것 중 가장 먼저 들어온 데이터, 입력정보 L2로 보내고 L2 에서 있던 데이터 L1으로 넣음.
                    remove_data(L2, L2_info, data)  # L2에서 data 지움
                    move_cache(L1, L1_info, L2, L2_info)
                    append_data(L1, L1_info, data)  # l1에 data 넣기
                    return data  # 반환해서 register 에 넣기
                else:
                    approach_time += 0.1
                    for i3 in range(0, len(L3)+1):
                        if data in L3 and i3 < 200:
                            hit[2] = hit[2] + 1
                            L3_info[data] += 1
                            # print('%d L3 hit!, count: %d' % (data, count))
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
                                    hit[3] = hit[3] + 1
                                    ram_info[data] += 1
                                    # print('%d RAM hit!, count: %d' % (data, count))
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
                                    # 구현) hdd 에서 찾은 데이터 ram과 L1으로 넣음(Write through). L1 에 있는 것 중 가장 먼저 들어온 데이터, 입력정보를 L2로 보냄.
                                    #       L2에서 가장 먼저 있던 데이터 L3으로 보냄. L3에서 가장 먼저 있던 데이터 ram으로 보냄. ram에 가장 먼저 있던 데이터 삭제.
                                    if len(L3) >= 200 and len(L3) == 200:
                                        if len(ram) >= 500 and len(ram) == 500: # ram 이 full 일 때 ram에 제일 먼저 들어온 값 삭제
                                            remove_mfrequently_data()
                                            remove_mfrequently_data()   # 캐시에서 내려온 데이터와 hdd에서 새로 올라온 데이터를 저장하기 위해 ram에 있던 데이터 2개 삭제
                                        append_data(ram, ram_info, data)
                                        move_cache(L3, L3_info, ram, ram_info)
                                        move_cache(L2, L2_info, L3, L3_info)
                                        move_cache(L1, L1_info, L2, L2_info)
                                        append_data(L1, L1_info, data)
                                        return data
                                    elif len(L2) >= 20 and len(L2) == 20:
                                        append_data(ram, ram_info, data)
                                        move_cache(L2, L2_info, L3, L3_info)
                                        move_cache(L1, L1_info, L2, L2_info)
                                        append_data(L1, L1_info, data)
                                        return data
                                    elif len(L1) == 5 and len(L1) == 5:
                                        append_data(ram, ram_info, data)
                                        move_cache(L1, L1_info, L2, L2_info)
                                        append_data(L1, L1_info, data)
                                        return data
                                    else:
                                        append_data(ram, ram_info, data)
                                        append_data(L1, L1_info, data)
                                        return data


if __name__ == '__main__':
    # L1, L2, L3 있는 캐시
    SIZE = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    hit_ratio_li = []
    miss_ratio_li = []
    approach_time_li = []
    for i in SIZE:
        hit = [0, 0, 0, 0, 0]
        # # 사용자에게 입력받을 때
        # print('정수 두 개를 입력하세요. num1: ', end="")
        # num1 = input()
        # print(' num2: ', end="")
        # num2 = input()
        for j in range(0, i):
            num1 = randint(1, 500)
            num2 = randint(1, 500)

            # print(j + 1, '번째')
            # print('num1: %d \t num2: %d' % (num1, num2))
            R1 = search_ln(num1)
            approach_time1 = approach_time
            # print('R1 : ', R1, ', 속도 : ', approach_time)
            R2 = search_ln(num2)
            approach_time2 = approach_time
            # print('R2 : ', R2, ', 속도 : ', approach_time)
            # print('덧셈 결과 : ', R1 + R2)
            # print()
            # print('L1 : ', L1)
            # print('L1_info : ', L1_info)
            # print('L2 : ', L2)
            # print('L2_info : ', L2_info)
            # print('L3 : ', L3)
            # print('L3_info : ', L3_info)
            # print()
            # print()
            # if (i + 1) % 10 == 0:
            #     print('---------------------------------------------------------------------------------')

        hit_ratio = (hit[0]+hit[1]+hit[2])/(i*2)*100
        miss_ratio = float(100-hit_ratio)
        total_approach_time = float(approach_time1+approach_time2)
        print('총 hit 율(L1+L2+L3) %0.1f%%: ' % hit_ratio)
        hit_ratio_li.append(hit_ratio)
        print('miss 율(ram + hdd 접근율) : %0.1f%%' % miss_ratio)
        miss_ratio_li.append(miss_ratio)
        print('접근 시간 : %0.1f\n' % total_approach_time)
        approach_time_li.append(total_approach_time)

    # print(hit_ratio_li)
    # print(miss_ratio_li)
    # print(approach_time_li)
    plt.plot(SIZE, hit_ratio_li, color='orange', label='hit ratio')
    plt.plot(SIZE, miss_ratio_li, color='blue', label='miss ratio')
    plt.plot(SIZE, approach_time_li, color='purple', label='approach time')
    plt.legend(fontsize='x-large')
    plt.title('MFU')
    plt.xlabel('Reference count')
    plt.ylabel('Performance indicator')
    plt.show()
    print('종료')
