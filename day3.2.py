with open("day3_input.txt", "r") as file:
    day3 = [line.strip().split(" ") for line in file]

    def number_of_trees(right, down):
        encounter = 0
        start = right
        new = [day3[i] for i in range(len(day3)) if i != 0 and i % down == 0]
        for j in new:
            line_list = list("".join(j))
            if (len(line_list) - 1) < start:
                start = start - len(line_list)
            if (len(line_list) - 1) >= start and line_list[start] == "#":
                encounter = encounter + 1
                start = start + right
            elif (len(line_list) - 1) >= start and line_list[start] == ".":
                start = start + right
        return encounter

    print(number_of_trees(1, 1) * number_of_trees(3, 1) * number_of_trees(5, 1) * number_of_trees(7, 1) * number_of_trees(1, 2))