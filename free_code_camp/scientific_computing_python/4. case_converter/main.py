"""
List Comprehension is a way to construct a new Python list from an iterable types: lists, tuples, and strings. All without using a for loop or the `.append()` list method.

In this project, you'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.

The project has two phases: first you'll use a for loop to implement the program. Then you'll learn how to use List Comprehension instead of a loop to achieve the same results.
"""

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
           snake_cased_char_list.append(char)