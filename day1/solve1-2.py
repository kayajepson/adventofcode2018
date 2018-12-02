text_file = open("input1.txt")
list1 = text_file.readlines()
total = sum(map(int, list1))
print(total)
