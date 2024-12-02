from os import times

with open("DATA_FILE/Day_2", "r") as file:
    data: [] = file.readlines()
    file.close()
    for i in range(data.__len__()):
        data[i]: [] = list(map(int, data[i].split()))

def is_save(row: list)->bool:
    if  sorted(row)==row or sorted(row)==row[::-1]:
        for i in range(row.__len__()-1):
            diff: int = abs(row[i+1]-row[i])
            if 0==diff or 3<diff:
                return False
        return True
    else:
        return False

def is_save_2(row: list)->bool:
    count: int = 0
    for i in range(row.__len__()-1):
        if 0>row[i]-row[i+1] and -3<=row[i]-row[i+1]:
            count-=1
        elif 0<row[i]-row[i+1] and 3>=row[i]-row[i+1]:
            count+=1
        else:
            break
    if row.__len__()-1==abs(count):
        return True
    else:
        # print(row)
        return False


def problem_1(data: list) -> int:
    save_floor_num: int = 0
    for row in data:
        if is_save(row):
            save_floor_num += 1
    return save_floor_num

def problem_2(data: int) -> int:
    save_floor_num: int = 0
    for row in data:
        print(row)
        if is_save(row):
            print("no removal")
            save_floor_num += 1
        else:
            for i in range(row.__len__()):
                row_copy = row.copy()
                del row_copy[i]
                if is_save(row_copy):
                    print(f"remove {row[i]}")
                    save_floor_num += 1
                    break
                pass
    print(save_floor_num)
    return save_floor_num
    pass

from random import randint
from time import time
from matplotlib import pyplot as plt

lengths = 100000
max_length=100

times_sorted=[]
times_sorted2=[]

for i in range(max_length):
    test_data = [[randint(-20,40) for _ in range(max_length+2)] for _ in range(lengths)]

    t1=time()
    for row in test_data:
        flag = is_save(row)
    t2=time()
    t3=time()
    for row in test_data:
        flag = is_save_2(row)
    t4=time()
    times_sorted.append(t2-t1)
    times_sorted2.append(t4-t3)

plt.figure()
plt.plot(times_sorted,label="is_save func")
plt.plot(times_sorted2, label="is_save_2 func")
plt.legend()
plt.ylabel("time in seconds")
plt.xlabel("list size")
plt.show()

