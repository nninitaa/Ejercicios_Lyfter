#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
def count_characters(text, character):
    counter = 0
    for letter in text:
        if letter == character: 
            counter += 1
    return counter

text = "Programming is fun!"
character = "o"

result = count_characters(text, character)
print("The character '{}' appears {} times in the text.".format(character, result)) 

#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
def filter_words_by_length(words, n):
    filtered_words = []
    for word in words:
        if len(word) > n:
            filtered_words.append(word)
    return filtered_words

word_list = ["apple", "banana", "cherry", "pineapple", "berry"]
n = 5

result = filter_words_by_length(word_list, n)
print("Words with more than {} letters: {}".format(n, result))

#Cree una función que reciba un string y retorne cuántas vocales contiene
def count_vowels(text):
    counter = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in text:
        if letter in vowels:
            counter += 1
    return counter

text = "The sky is blue and the sun is bright."
result = count_vowels(text)
print("The text contains {} vowels.".format(result))