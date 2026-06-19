def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

myList = [1, 2, 3, 4, 5]
result = sum_list(myList)
print("The sum of the list is: {}".format(result))

