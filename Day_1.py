with open("DATA_FILE/Day_1") as file:
    raw_data: [str] = file.readlines()
    data: [[int]] = [[int(raw_data[i].split()[0]) for i in range(raw_data.__len__())],[int(raw_data[i].split()[1]) for i in range(raw_data.__len__())]]


def problem_1(data: [[int]]) -> int:
    dist: int = 0
    while data[0].__len__()>0:
        min_left_ind = data[0].index(min(data[0]))
        min_right_ind = data[1].index(min(data[1]))
        dist += abs(data[0][min_left_ind] - data[1][min_right_ind])
        del data[0][min_left_ind]
        del data[1][min_right_ind]
    return dist

def problem_2(data: [[int]]) -> int:
    hash: dict[str, int] = {}
    similarity =0
    for i in range(data[0].__len__()):
        if str(data[0][i]) in hash:
            similarity += hash[str(data[0][i])]
        else:
            count = data[1].count(data[0][i])
            hash[str(data[0][i])] = count*data[0][i]
            similarity += hash[str(data[0][i])]
    return similarity


# problem_1(data)
print(problem_2(data))
