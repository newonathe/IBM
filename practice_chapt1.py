# Variables in Python - NO 'var', NO semicolons, NO type declarations
name = "Ethan"
age = 22
gpa = 3.85
is_student = True
nothing = None

# You can print any variable
print(name)
print(age)
print(gpa)
print(is_student)
print(nothing)
print(type(age))

# Variable names: use lowercase + underscores (snake_case)

first_name = "Ethan"
last_name = "Taruc"
full_name = first_name + " " + last_name #concatenation
print(full_name)

# You can reassign a variable anytime
x = 5
print(x) # Output: 5
x = "Hello"
print(x) # Output: Hello

# You can print multiple things (comma-separated, adds space between)
print("Name:", "Ethan")

# f-strings (formatted string literals)
print(f"Name: {full_name}, Age: {age}, GPA: {gpa}")

# Print with sep (custom separator)
print(1, 2, 3, sep="-") # Output: 1-2-3
print(1, 2, 3, sep =", ")

# Print with end (custom end character)
print("Hello", end=" ")
print("World")

# Print nothing = blank line
print()

# Read N then read N numbers
nums = list(map(int, input().split()))
print(nums) # Output: [1, 2, 3] if user input is "1 2 3"
print(sum(nums)) # Output: 6

# Read a string and convert to uppercase/lowercase
s= input("Enter a string: ")
print(s.upper()) # Output: "HELLO" if user input is "hello"
print(s.lower()) # Output: "hello" if user input is "HELLO"

#Converting types
x = "42"
y = int(x)
z = float(x)

# The reverse
num = 99
text = str(num)

# Why this matters on HackerRank:
user_input = input()    # input() ALWAYS returns a string
number = int(user_input)  # You MUST convert if you want to do math

#Multiple value on one line

a, b = map(int,input().spilit())
print(a + b)

n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total += num
print(total)


s = input()
print(len(s))
print(s[::-1])
print(s.upper())

a = 17
b = 5

print(a //b ) #floor division (drops the decimal)
print (a % b) #modulo (remainder)
print(a ** b) #exponentiation (a to the power of b)

# The % (modulo) operator is KEY in coding problems:
# - Check if a number is even: n % 2 == 0
# - Check if divisible by 3: n % 3 == 0
# - Get last digit: n % 10
# - Wrap around (circular indexing): index % length

print(10 % 2)  # 0 → 10 is even
print(9 % 2)   # 1 → 9 is odd
print(123 % 10)  # 3 → last digit is 3

a, b = 10, 5

print(a == b) # False
print(a != b) # True
print(a > b)  # True
print(a < b)  # False
print(a >= b) # True
print(a <= b) # False

# Chained comparisons (Python special feature!)
x = 5
print(1 < x < 10)    # True — x is between 1 and 10

# Logical operators
print(True and False) # False
print(True or False)  # True

# Not operator
print(not True) # False

# Membership operator
print(5 in [1, 2, 3, 4, 5]) # True
print(5 not in [1, 2, 3, 4, 5]) # False

# Identity operator
print(5 is 5) # True
print(5 is not 5) # False

age = 20
has_id = True

print(age >= 18 and has_id) # True
print(age>=18 and not has_id) # False
print(age < 18 or has_id) # True

n = int(input())
for i in range(1, n):
    if n % 3 == 0  and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else: 
        print("indivisible by 3 and 5")

n = int(input())
if x < 0:
    x = -x
print(x)

a, b = map(int, input().split())
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Equal")


n = int(input())
for i in range(n):
    star_space = " " * (n - i - 1)
    stars = "*" * (i + 1)
    print(star_space + stars)


nums = [3, 1, 4, 1, 5, 9, 2, 6]
words = ["hello", "world", "python"]
mixed = [1, "two", 3.0, True]
empty = []

print(nums[0:3])
print(nums[2:])
print(nums[:4])
print(nums[::-1])

print(len(nums))
print(sum(nums))
print(max(nums))
print(min(nums))
print(9 in nums)
print(sorted(nums))

nums.apped(17)
nums.insert(0, 21)
nums.remove(17)
nums.pop()
nums.pop(0)
nums.sort()
nums.reverse()

for n in nums:
    print(n)

squares = [x**3 for x in range(10)]
print(squares) # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

evens = [x for x in range (20) if x % 2 == 0]
print(evens) # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

s = "hello world"
print(s.startswith("hello"))
print(s.endswith("world"))
print(s.found("hello")) # Output: True
print(s.count("o")) # Output: 2

print(s.replace("world", "python")) # Output: "hello python"
print(s.strip()) # Output: "hello world"
print(s.split(" ")) # Output: ["hello", "world"]
print(" ".join(["a", "b", "c"])) # Output: "a b c, not "abc, it adds the space in between the words"

name = "IBM"
score = 98.5

print(f"Company: {name}, Score: {score:.1f}") # Output: "Company: IBM, Score: 98.5, :.1f means 1 decimal place"
print(f"{'hi':>10}") # Output: "        hi" (right-aligned in a 10-character field)

person = {
    "name": "Ethan",
    "age": 21,
    "major": "ComputerScience",
    "gpa": 3.85,
    "is_student": True
}

person["university"] = "Ateneo de Manila"
person["age"] = 22

del person["is_student"]

person.pop("university")

for key, value in person.items(): # items() returns a list of (key, value) pairs
    print(f"{key}: {value}")

print(person.keys()) # outputs: dict_keys(['name', 'age', 'major', 'gpa'])
print(person.values()) # dict_values(['Ethan', 22, 'ComputerScience', 3.85])
print(person.items()) # dict_items([('name', 'Ethan'), ('age', 22), ('major', 'ComputerScience'), ('gpa', 3.85)])

s = "mississippi"
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print (freq)

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1 #get() returns the value for the key if it exists, otherwise returns the default value (0 in this case)
print (freq)

from collections import Counter
freq = Counter(s) # Counter() returns a Counter object, which is a dictionary subclass that counts the frequency of each element in the iterable (s in this case)
print (freq)

