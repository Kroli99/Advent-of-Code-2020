with open("day3_input.txt", "r") as file:
    day3 = [line.strip().split(" ") for line in file]

    def number_of_trees(right, down):
        encounter = 0
        start = right
        new = []
        for i in range(len(day3)):
            if i != 0 and i % down == 0:
                new.append(day3[i])
        for j in new:
            line_list = list("".join(j))
            if len(line_list) <= start:
                line_list = list("".join((len(line_list) + 1) * line_list))
            if len(line_list) >= start and line_list[start] == "#":
                encounter = encounter + 1
                start = start + right
            elif len(line_list) >= start and line_list[start] == ".":
                start = start + right
        return range(len(new))

    print(number_of_trees(1, 2), number_of_trees(1, 1), number_of_trees(3, 1))