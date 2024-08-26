def arithmetic_arranger(problems, show_answers=False):

    # 1. Check the length of the parameter problems:
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # 2. Check the operant:
    operators = []
    for problem in problems:
        array = problem.split()
        operators.append(array[1])
    for operator in operators:
        if operator in ['*', '/']:
            return "Error: Operator must be '+' or '-'."
    # 3. Check for non-digits:
    numbers = []
    for problem in problems:
        array = problem.split()
        numbers.append(array[0])
        numbers.append(array[2])
        # print(numbers)

    for number in numbers:
        if not number.isdigit():
            return 'Error: Numbers must only contain digits.'
    # 4. Check max-digits of the operands:
        elif len(number) > 4:
            'Error: Numbers cannot be more than four digits.'
 

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')