with open('input1.txt') as file_object:
    total = 0
    for line in file_object:
        total += int(line)
    print(total)
