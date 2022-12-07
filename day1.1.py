with open("day1_input.txt", "r") as file:
    day1 = []
    for line in file:
        day1.append(int(line.strip()))
    for i in day1:
        for j in day1:
            if j + i > 2020 or j + i < 2020:
                continue
            elif j + i == 2020:
                print(j*i)
                break