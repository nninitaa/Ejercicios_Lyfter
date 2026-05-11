#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def secondFunction():
    print("Hello from the second function!")

def firstFunction():
    print("Hello from the first function!")
    secondFunction()

firstFunction()

#Experimente con el concepto de scope:
#Intente acceder a una variable definida dentro de una función desde afuera.
def myFunction():
    myVariable = "Hello from inside the function!"
    print(myVariable)

myFunction()
#print -> Esto dará un error si intentamos acceder a myVariable desde fuera de la función, ya que está definida dentro del scope de myFunction.

#Intente acceder a una variable global desde una función y cambiar su valor.
myGlobalVariable = 0

def changeGlobalVariable():
    global myGlobalVariable
    myGlobalVariable = myGlobalVariable + 1
    print("Inside the function: {}".format(myGlobalVariable))

print("Before calling the function: {}".format(myGlobalVariable))
changeGlobalVariable()
print("After calling the function: {}".format(myGlobalVariable))

#Cree una función que retorne la suma de todos los números de una lista.
def sumList(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

myList = [1, 2, 3, 4, 5]
result = sumList(myList)
print("The sum of the list is: {}".format(result))

#Cree una función que le dé la vuelta a un string y lo retorne.
def reverseString(text):
    reversed = ""
    for characters in text:
        reversed = characters + reversed
    return reversed

myString = "Hello!"
reversedString = reverseString(myString)
print("The reversed string is: {}".format(reversedString))

#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
def countLetters(text):
    uppercaseCount = 0
    lowercaseCount = 0
    for character in text:
        if character.isupper():
            uppercaseCount += 1
        elif character.islower():
            lowercaseCount += 1
    print("Uppercase letters: {}".format(uppercaseCount))
    print("Lowercase letters: {}".format(lowercaseCount))

myText = "I want to visit Korea!"
countLetters(myText)

#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
def sortWords(text):
    word = text.split("-")
    word.sort()
    return "-".join(word)

myText = "python-variable-function-computer-monitor"
sortedText = sortWords(myText)
print("The sorted string is: {}".format(sortedText))

# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeNumbers = get_primes(myNumbers)
print("The prime numbers in the list are: {}".format(primeNumbers))