with open("DATA_FILE/Day_2", "r") as file:
    data: [] = file.readlines()
    file.close()
    for i in range(data.__len__()):
        data[i]: [] = list(map(int, data[i].split()))

def is_save(row: list)->bool:
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
    print(save_floor_num)
    return save_floor_num

def problem_2(data: int) -> int:
    save_floor_num: int = 0
    for row in data:
        if is_save(row):
            save_floor_num += 1
        else:
            for i in range(row.__len__()):
                row_copy = row.copy()
                del row_copy[i]
                if is_save(row_copy):
                    save_floor_num += 1
                    break
                pass
    print(save_floor_num)
    return save_floor_num
    pass


problem_1(data)
problem_2(data)
