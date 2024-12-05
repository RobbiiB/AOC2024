with open("DATA_FILE/test_input", "r") as file:
    data = file.read().split("\n")

def find_xmas(data: list)->int:
    xmas_counter: int = 0
    for row in data:
        xmas_counter += row.count("XMAS")
        xmas_counter += row.count("SAMX")
    return xmas_counter

def get_diags(data: list) -> list:
    left_45: list = []
    right_45: list = []
    for i in range(2 * data.__len__()):
        left_45.append("")
        right_45.append("")
        for j in range(i + 1):
            try:
                left_45[i] += data[j][i - j]
            except:
                pass
            try:
                right_45[i] += data[j][::-1][i - j]
            except:
                pass
    return left_45, right_45

def problem_1(data: list)->int:
    xmas_counter: int = 0
    transposed_data: list = [''.join(column) for column in zip(*data)]
    left_45, right_45 = get_diags(data)

    xmas_counter += find_xmas(data)
    xmas_counter += find_xmas(transposed_data)
    xmas_counter += find_xmas(left_45)
    xmas_counter += find_xmas(right_45)
    return xmas_counter

def problem_2(data: list)->int:
    x_mas_counter: int = 0
    left_45, right_45 = get_diags(data)
    for row in left_45:
        print(row)
    for row in right_45:
        print(row)

    for i in range(left_45.__len__()):
        check_num = 0b11
        while check_num != 0:
            try:
                ind: int = left_45[i].index("MAS")
                left_45[i][ind+1] = "R"
            except:
                check_num = check_num ^0b10
            try:
                ind: int = left_45[i].index("SAM")
                print(left_45[i])
                left_45[i][ind + 1] = "R"
            except:
                check_num = check_num ^ 0b1
    # for row in left_45:
    #     print(row)

    return x_mas_counter
# print(problem_1(data))

def find_index_rotated_list(data:list, i:int,j:int)->tuple[int,int]:
    x_max = data[0].__len__()
    pivot = (x_max+1)//2



find_index_rotated_list(data, 0,0 )
problem_2(data)
