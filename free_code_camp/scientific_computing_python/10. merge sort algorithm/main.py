"""
The merge sort algorithm mainly performs three actions:

- Divide an unsorted sequence of items into sub-parts
- Sort the items in the sub-parts
- Merge the sorted sub-parts
The above happens recursively until the sub-parts are merged into the complete sorted sequence.
"""
def merge_sort(array):
    middle_point = len(array) // 2
    # slice each half and assign to a var:
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    # recursifly call merge_sort on each half:
    merge_sort(left_part)
    merge_sort(right_part)
    # Create the vars to sort the parts
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    #  compare an element in left_part to an element in right_part, and merge the smaller element to the main array list:
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
