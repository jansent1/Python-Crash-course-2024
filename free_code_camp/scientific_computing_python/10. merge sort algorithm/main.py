"""
The merge sort algorithm mainly performs three actions:

- Divide an unsorted sequence of items into sub-parts
- Sort the items in the sub-parts
- Merge the sorted sub-parts
The above happens recursively until the sub-parts are merged into the complete sorted sequence.
"""
def merge_sort(array):
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

