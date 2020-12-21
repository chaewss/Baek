from random import *
from matplotlib import pyplot as plt

hdd = []
for i in range(1, 5001):  # 하드디스크값 1~5000 으로 초기화
    hdd.append(i)
ram = []  # 램
ram_info = {}
L1 = []  # 캐시 L1 5개
L1_info = {}
R1 = 0  # 레지스터 1
R2 = 0  # 레지스터 2
approach_time = 0  # 접근시간
count = 0  # 선입선출을 위한 변수
hit = [0, 0, 0]  # L1, ram, hdd 각각 hit 횟수


def append_data(ln, ln_info, num):  # ln에 num 넣기, ln_info 값 변경
    global count
    ln.append(num)
    count += 1
    ln_info[num] = count


def remove_data(ln, ln_info, num):  # ln의 num 지우기, ln_info 값 지우기
    ln.remove(num)
    del ln_info[num]


def remove_old_data(): # ram 이 꽉 찬 경우 선입선출로 가장 오래된 데이터 값 삭제
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


def search_L1(data):  # L1만 있는 캐시
    global approach_time
    global count
    approach_time = 0
    approach_time += 0.1
    for i1 in range(0, len(L1)+1):
        if data in L1 and i1 < 5:
            print('%d L1 hit!' % data)
            hit[0] = hit[0] + 1
            count += 1
            L1_info[data] = count  # L1_info 리스트에 입력시간 갱신
            return data
        else:
            approach_time += 1  # 캐시에서 찾지 못했기 때문에 램으로 진입. 메모리 접근 시간 1초
            for i2 in range(0, len(ram)+1):
                if data in ram and i2 < 499:
                    print('%d RAM hit!' % data)
                    hit[1] = hit[1] + 1
                    remove_data(ram, ram_info, data)
                    move_cache(L1, L1_info, ram, ram_info)
                    append_data(L1, L1_info, data)
                    append_data(ram, ram_info, data)
                    return data
                elif data in ram and i2 == 499:
                    hit[3] = hit[3] + 1
                    remove_data(ram, ram_info, data)
                    remove_old_data()
                    move_cache(L1, L1_info, ram, ram_info)
                    append_data(L1, L1_info, data)
                    append_data(ram, ram_info, data)
                else:
                    approach_time += 3  # 하드디스크 접근 시간 3초
                    print('%d HDD hit!' % data)
                    hit[2] = hit[2] + 1
                    if len(L1) == 5:
                        if len(ram) == 500:  # ram 이 full 일 때 ram에 제일 먼저 들어온 값 삭제
                            remove_old_data()
                            remove_old_data()  # 캐시에서 내려온 데이터와 hdd에서 새로 올라온 데이터를 저장하기 위해 ram에 있던 오래된 데이터 2개 삭제
                        append_data(ram, ram_info, data)
                        move_cache(L1, L1_info, ram, ram_info)
                        append_data(L1, L1_info, data)
                        return data
                    else:
                        append_data(ram, ram_info, data)
                        append_data(L1, L1_info, data)
                        return data


# SIZE = 10  # 몇번 연산할 것인가

if __name__ == '__main__':
    # L1 캐시
    SIZE = [10]
    hit_ratio_li = []
    miss_ratio_li = []
    approach_time_li = []
    for i in SIZE:
        hit = [0, 0, 0]
        for j in range(0, i):
            # # 사용자에게 입력받을 때
            # print('정수 두 개를 입력하세요. num1: ', end="")
            # num1 = input()
            # print(' num2: ', end="")
            # num2 = input()
            num1 = randint(1, 100)
            num2 = randint(1, 100)
            print(j+1, '번째')
            print('num1: %d \t num2: %d' % (num1, num2))
            R1 = search_L1(num1)
            approach_time1 = approach_time
            print('R1 : ', R1, ', 속도 : ', approach_time)
            R2 = search_L1(num2)
            approach_time2 = approach_time
            print('R2 : ', R2, ', 속도 : ', approach_time)
            print()
            print('L1 : ', L1)
            print('L1_info : ', L1_info)
            print('ram : ', ram)
            print('ram_info : ', ram_info)
            print('뎃셈 결과 : ', R1+R2)
            print()
            print()
            if (i+1) % 10 == 0:
                print('---------------------------------------------------------------------------------')

        total_approach_time = float(approach_time1 + approach_time2)
        print('hit 횟수 L1 : ', hit[0], ', ram : ', hit[1], ',hdd : ', hit[2])
        print('L1 hit 율 : %0.1f,  ram hit 율 : %0.1f, hdd hit 율 : %0.1f'
              % ((hit[0]/(i*2)*100), (hit[1]/(i*2)*100), (hit[2]/(i*2)*100)))
        print()
        print('총 hit 횟수(L1) : %d, 총 hit 율(L1) : %0.3f%%' % (hit[0],(hit[0])/(i*2)*100))
        hit_ratio_li.append(float((hit[0])/(i*2)*100))
        print('miss 횟수(ram + hdd 횟수) : %d, miss 율(ram + hdd 접근율) : %0.3f%%'
              % (hit[1]+hit[2], 100-(hit[0]/(i*2)*100)))
        miss_ratio_li.append(float(100-(hit[0]/(i*2)*100)))
        approach_time_li.append(total_approach_time)

    # print(hit_ratio_li)
    # print(miss_ratio_li)
    # print(approach_time_li)
    plt.plot(SIZE, hit_ratio_li, color='orange', label='hit ratio')
    plt.plot(SIZE, miss_ratio_li, color='blue', label='miss ratio')
    plt.plot(SIZE, approach_time_li, color='purple', label='approach time')
    plt.legend(fontsize='x-large')
    plt.title('L1 only')
    plt.xlabel('Reference count')
    plt.ylabel('Performance indicator')
    # plt.show()
    print('종료')
