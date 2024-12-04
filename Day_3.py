from Day_1 import problem_2

with open("DATA_FILE/Day_3", "r") as file:
    data: str = file.read()


def find_end_ind(data: list, ind: int) -> int | None:
    i: int = ind
    first_num: bool = False
    comma: bool = False
    second_num: bool = False
    while True:
        match ord(data[i]):
            case 41:
                if second_num:
                    return i
                else:
                    return None
            case 44:
                if first_num:
                    comma = True
                else:
                    return None
            case num if 48 <= num <= 57:
                if comma:
                    second_num = True
                else:
                    first_num = True
            case _:
                return None
        i += 1


def problem_1(data: str) -> int:
    multiplicity: int = 0
    while True:
        try:
            ind: int = data.index("mul(")
            end_ind: int = find_end_ind(data, ind + 4)
            if end_ind != None:
                multiplicity += int(data[ind + 4:end_ind].split(",")[0]) * int(data[ind + 4:end_ind].split(",")[1])
            data = data[:ind] + data[ind + 1:]
        except:
            break
    return multiplicity


def problem_2(data: str) -> int:
    while True:
        try:
            ind_dont: int = data.index("don't()")
            ind_do: int = data[ind_dont:].index("do()")
            data = data[:ind_dont] + data[ind_do+ind_dont:]
        except:
            break
    multiplicity: int = problem_1(data)
    return multiplicity


# print(problem_1(data))
# print(problem_2(data))
