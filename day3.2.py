with open("day3_input.txt", "r") as file:
    day3 = [line.strip().split(" ") for line in file]

    def number_of_trees(right, down):
        encounter = 0
        for i in day3:
            if i == day3[down - 1]:
                continue
            line_list = list("".join(i))
            if len(line_list) < right:
                line_list = list("".join((len(line_list) + 1) * line_list))
            if len(line_list) >= right and line_list[right] == "#":
                encounter = encounter + 1
                right = right + right
            elif len(line_list) >= right and line_list[right] == ".":
                right = right + right
        print(encounter)

    print(number_of_trees(3,1))