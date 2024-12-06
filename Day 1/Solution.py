def read_columns_to_lists(file_path):
    list1 = []
    list2 = []
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                col1, col2 = line.split()
                list1.append(int(col1))
                list2.append(int(col2))
    
    return list1, list2

list1, list2 = read_columns_to_lists('D:\Coding\BurritoAdventOfCode2024\Day 1\input.txt')

#sort the lists
list1.sort()
list2.sort()

cumulative_sum = 0

#compare each element of the two lists and add the absolute difference to the cumulative sum
for i, j in zip(list1, list2):
        cumulative_sum += abs(i-j)

print(cumulative_sum)

# Count number of of times each number appears in the two lists
comlist = []
for i in list1:
    comcounter = 0
    for j in list2:
        if i == j:
            comcounter += 1
    comlist.append(comcounter)

new_sum = 0
for i, j in zip(list1, comlist):
        new_sum += abs(i*j)
print(new_sum)
