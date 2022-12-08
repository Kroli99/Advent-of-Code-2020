with open("day2_input.txt", "r") as file:
    day2 = [line.strip().split(" ") for line in file]
    result = 0

    for i in day2:
        count_range = i[0].split("-")
        first_count = int(count_range[0])
        second_count = int(count_range[1])
        password = list(i[2])
        counter = password.count(i[1][0])

        if counter >= first_count and counter < (second_count + 1):
            result = result + 1
        else:
            continue
    print(result)

