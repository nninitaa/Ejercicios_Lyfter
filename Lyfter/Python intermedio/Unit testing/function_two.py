def reverse_string(text):
    reversed = ""
    for characters in text:
        reversed = characters + reversed
    return reversed

myString = "Hello!"
reversedString = reverse_string(myString)
print("The reversed string is: {}".format(reversedString))