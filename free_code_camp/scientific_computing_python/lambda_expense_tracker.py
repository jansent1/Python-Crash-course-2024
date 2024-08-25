# Lists contain fields with data. my_list[1, 2, 3] would be a list of numbers
# Dictionaries contain records with key: value pairs. my_dict{'key1': value, 'key2': value}
# Lambda functions are brief, anonymous functions in Python, ideal for simple, one-time tasks. They are defined by the lambda keyword.  test = lambda x: x * 2

# test = lambda x: x * 2
# print(list(map(test, [2, 3, 5, 8])))

# replace the list function with the sum() to get the total amount of expenses:
# test = lambda x: x * 2
# print(sum(map(test, [2,3,5,8])))

def add_expense(expenses, amount, category):
    expenses.append({ 'amount': amount, 'category': category })

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass    # see lambda functions!

expenses = []