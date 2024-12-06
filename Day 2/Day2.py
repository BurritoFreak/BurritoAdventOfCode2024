def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        number_lists = [list(map(int, line.split())) for line in lines]
    return number_lists

number_lists = read_numbers_from_file('Day 2\input.txt')
#print(number_lists)

num_safe_reports = 0

for number_list in number_lists:
    issafe = True
    for i in range(len(number_list)-1):
        safechecker = abs(number_list[i] - number_list[i+1])
        if safechecker > 3 or safechecker < 1:
            issafe = False
            break
    if issafe:
        num_safe_reports += 1

print(num_safe_reports)
