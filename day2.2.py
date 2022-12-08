with open("day2_input.txt", "r") as file:
    day2 = [line.strip().split(" ") for line in file]
    result = 0

    for i in day2:
        count_range = i[0].split("-")
        first_character = int(count_range[0]) - 1
        second_character = int(count_range[1]) - 1
        password = list(i[2])

        if i[1][0] != password[first_character] and i[1][0] == password[second_character]:
            result = result + 1
        elif i[1][0] == password[first_character] and i[1][0] != password[second_character]:
            result = result + 1
        else:
            continue

print(result)
