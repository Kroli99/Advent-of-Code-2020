with open("day1_input.txt", "r") as file:
    day2 = []
    result = []
    for line in file:
        day2.append(int(line.strip()))
    for i in day2:
        if i in result:
            break
        for j in day2:
            for l in day2:
                if i + j + l == 2020:
                    result.append(i)
                    result.append(j)
                    result.append(l)
                    break
    print(result[0] * result[1] * result[2])