print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def listed(num= int):
    listed = []
    for a in range(1, num+1):
        if num % a == 0:
            listed.append(a)
    return listed
print(listed(14))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factor_of(one = int, two = int):
    new, old = listed(one), listed(two)
    print(new, old)
    for a in new:
        if a in old:
            return True
    for a in old:
        if a in new:
            return True
    return False

print(factor_of(7,4))


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def alpha_index(letter= str) -> str:
    return alphabet.index(letter)

char = input()
print(alpha_index(char))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def find_more_index(name):
    numbers = []
    for char in name:
        numbers.append(alphabet.index(char))
    return ''.join(str(a) for a in numbers)

print(find_more_index(char))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def id_password():
    name = find_more_index()
    total = 0
    for num in name: #'9,13,7,14'
        total += int(num)
    return int(name) - total

print(id_password())

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def is_prime():
    not_integer = True
    number = 0
    while not_integer:
        try:
            print('what prime number would you like to check:')
            number = int(input())
            if type(number) == int:
                not_integer = False
        except ValueError:
            print('enter a integer/number')
            
    prime = True
    if number == 1:
        prime = False
        return prime
    elif number > 1:
        for num in range(2, number):
            if number % num == 0:
                prime = False
                break
        if prime:
            return  prime
        else:
            return prime

print(is_prime())

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:



# -------------------------------------------------------------------------------------- #






