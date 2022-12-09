with open("day3_input.txt", "r") as file:
    day3 = [line.strip().split(" ") for line in file]

    start = 3
    encounter = 0

    for i in day3:
        if i == day3[0]:
            continue
        line_list = list("".join(i))
        if len(line_list) < start:
            line_list = list("".join((len(line_list)+1) * line_list))
        if len(line_list) >= start and line_list[start] == "#":
            encounter = encounter + 1
            start = start + 3
        elif len(line_list) >= start and line_list[start] == ".":
            start = start + 3

    print(encounter)
