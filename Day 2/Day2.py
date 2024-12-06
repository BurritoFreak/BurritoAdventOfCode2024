def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        number_lists = [list(map(int, line.split())) for line in lines]
    return number_lists

number_lists = read_numbers_from_file('Day 2\input.txt')
#print(number_lists)

num_safe_reports = 0

def safe_report_tester(number_list):
    for i in range(len(number_list)-1):
        safechecker = abs(number_list[i] - number_list[i+1])
        if safechecker > 3 or safechecker < 1:
            return False
            break
    for i in range(len(number_list)-1):
        if number_list[i] > number_list[i+1]:
            inorder = True
        else:
            inorder = False
            break
    if not(inorder):
        for i in range(len(number_list)-1):
            if number_list[i] < number_list[i+1]:
                inorder = True
            else:
                inorder = False
                break
    if not(inorder):
        return False
    return True

for number_list in number_lists:
    issafe = safe_report_tester(number_list)
    if not(issafe):
        for i in range(len(number_list)):
            templist = number_list.copy()
            templist.pop(i)
            print(templist)
            issafe = safe_report_tester(templist)
            if issafe:
                break
    if issafe:
        num_safe_reports += 1

print(num_safe_reports)
