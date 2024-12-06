import re

def extract_mul_expressions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    matches = re.findall(pattern, content)
    
    return matches

def evaluate_mul_expressions(mul_expressions):
    results = []
    for expression in mul_expressions:
        numbers = re.findall(r'\d+', expression)
        result = int(numbers[0]) * int(numbers[1])
        results.append(result)
    return results

def check_first_four_characters(terms):
    results = []
    addToList = True
    for term in terms:
        if term[:4] == "do()":
            addToList = True
        elif term[:5] == "don't":
            addToList = False
        if term[:3] == "mul" and addToList:
            results.append(term)
    return results

def add_results(results):
    total = 0
    for result in results:
        total += result
    return total

mul_expressions = extract_mul_expressions('Day 3\input.txt')
print(mul_expressions[9][:4])

new_mul_expressions = check_first_four_characters(mul_expressions)
print(new_mul_expressions)

results = evaluate_mul_expressions(new_mul_expressions)
print(results)

total = add_results(results)
print(total)