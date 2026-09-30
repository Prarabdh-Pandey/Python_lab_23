# Write a function remove last(lst) that rmeoves the last elements of list.
# call this function with list and check wheather the original list change outside the function.


def remove_last(lst):
    lst.pop()


numbers = [10, 20, 30, 40, 50]

print("Before function call:", numbers)

remove_last(numbers)

print("After function call:", numbers)

