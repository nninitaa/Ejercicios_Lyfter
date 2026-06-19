def sort_words(text):
    word = text.split("-")
    word.sort()
    return "-".join(word)

myText = "python-variable-function-computer-monitor"
sortedText = sort_words(myText)
print("The sorted string is: {}".format(sortedText))