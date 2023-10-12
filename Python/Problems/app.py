# Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.

numbers=[1,20,30,40,60,100,3,6]

sum=sum(numbers)
    # print(sum) 260

avg=sum/(len(numbers)) # 32.5

print(f"Sum:{sum}, Avg:{avg}") #Output Sum:260, Avg:32.5


# Write a Python function that takes a string and returns the string in reverse order.

str="thisisrace"

def reverse(input):
    revStr=input[::-1]
    return revStr

result=reverse(str)
print(result) # ecarsisiht

# Write a Python program that counts the number of vowels in a given string.

str="asdfeiddoucbd"
count=0
for i in str:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
print(count)



vcount=0
def count_vowels(input):
    global vcount # use the global variable vcount
    vowels=["a","e","i","o","u"]
    for char in input.lower():
        if char in vowels:
            vcount += 1
count_vowels(str)
print(f"Number of vowels:{vcount}") # Number of vowels:5


# Write a Python function that checks whether a given number is a prime number.

num=13

def checkPrime(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return  False
    return True

if checkPrime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")



## Write a Python function that calculates the factorial of a number.

def getFactorial(number):
    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        sum=1
        for i in range(1,number+1):
            sum*=i
        return sum

result=getFactorial(5)
print(result) # 120


# Use list comprehension to create a list of the squares of the numbers from 1 to 10.

def genSquares(number):
    sqares=[]

    for i in range(1,number+1):
        res=i*i
        sqares.append(res)
    return sqares

print(genSquares(10))


# Explain me  Fibonacci sequence , and Write a Python function that generates the first n numbers in the Fibonacci sequence.

def genFabionacci(n):
    fibSeq=[]
    # The first two numbers in the seqience
    a,b=0,1

    # special case: if n is 1, return [0]
    if n==1:
        return [0]
    
    # generate
    for _ in range(n):
        fibSeq.append(a)
        a,b=b ,a+b
    return fibSeq

print(genFabionacci(5)) # [0, 1, 1, 2, 3]

## Write a program to print the following number pattern using a loop.                                                             
#1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5   

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


##  **Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)


## Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.                                               # s1 = "Ault"
#s2="Kelly"                                         output : AuKellylt

s1 = "Ault"
s2 = "Kelly"

middle_index = len(s1) // 2
s3 = s1[:middle_index] + s2 + s1[middle_index:]

print(s3)


## Arrange string characters such that lowercase letters should come first**
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.                                     str=PyNaTive                          output: yaivePNT

str1 = "PyNaTive"

lowercase_chars = []
uppercase_chars = []

for char in str1:
    if char.islower():
        lowercase_chars.append(char)
    else:
        uppercase_chars.append(char)

arranged_str = ''.join(lowercase_chars + uppercase_chars)

print(arranged_str)


## *Concatenate two lists index-wise**
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.                                                                                               
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]                       output: ['My', 'name', 'is', 'Kelly']
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []

# Determine the length of the smaller list
min_length = min(len(list1), len(list2))

# Iterate through the common indices
for i in range(min_length):
    new_list.append(list1[i] + list2[i])

# Add any leftover elements
if len(list1) > len(list2):
    new_list.extend(list1[min_length:])
else:
    new_list.extend(list2[min_length:])

print(new_list)


## Concatenate two lists in the following order                             
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]                   
# output:['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

new_list = []

# Iterate through the elements of list1
for item1 in list1:
    # Iterate through the elements of list2
    for item2 in list2:
        # Concatenate the elements and add to new_list
        new_list.append(item1 + item2)

print(new_list)



## Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.                                             list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]                                         Output:                      
# 10 400
# 20 300
# 30 200
# 40 100

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Reverse the order of list2
list2_reversed = list2[::-1]

# Iterate through both lists simultaneously using zip
for item1, item2 in zip(list1, list2_reversed):
    print(item1, item2)



## Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.                                                                                            employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}                                                                                                 output: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_dict = {employee: defaults for employee in employees}

print(employee_dict)


## ### **Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.                                                                                                            sample_dict = {
    #"name": "Kelly",
    # "age": 25,
    # "salary": 8000,
    # "city": "New york"} 
# Keys to extract
# keys = ["name", "salary"]                                                                                                             output: {'name': 'Kelly', 'salary': 8000}                                                                                                                

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)


## Modify the tuple
# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222                                                                                                           
# tuple1 = (11, [22, 33], 44, 55)                                                                                                                   output : tuple1: (11, [222, 33], 44, 55)


tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list to modify the nested list
list1 = list(tuple1)
list1[1][0] = 222

# Convert the modified list back to a tuple
tuple1 = tuple(list1)

print("tuple1:", tuple1)

# Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
    # - Input: [("John", 25), ("Jane", 30)]
    # - Output: "John is 25 years old. Jane is 30 years old.

people = [("John", 25), ("Jane", 30)]

for name, age in people:
    print(f"{name} is {age} years old.")


## Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
    # - Input: Add "John": 25, Update "John": 26, Delete "John"
    # - Output: "{}, {'John': 26}, {}"


def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Create an empty dictionary
people = {}

# Add a new name-age pair
add_person(people, "John", 25)
print(people)

# Update the age of a name
update_age(people, "John", 26)
print(people)

# Delete a name from the dictionary
delete_person(people, "John")
print(people)


## Two Sum Problem: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
    # - Input: [2, 7, 11, 15], target = 9
    # - Output: "[0, 1]"


def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

    return []

# Test the function
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)


##  Palindrome Check: Write a Python function that checks whether a given word or phrase is a palindrome.
    # - Input: "madam"
    # - Output: "The word madam is a palindrome."

def is_palindrome(word):
    word = word.lower()  # Convert the word to lowercase
    reversed_word = word[::-1]  # Reverse the word

    if word == reversed_word:
        return True
    else:
        return False

# Test the function
word = "madam"

if is_palindrome(word):
    print("The word", word, "is a palindrome.")
else:
    print("The word", word, "is not a palindrome.")


## Selection Sort: Implement the selection sort algorithm in Python.
    # - Input: [64, 25, 12, 22, 11]
    # - Output: "[11, 12, 22, 25, 64]"

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Test the function
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)


##. Implement Stack using Queue: Use Python's queue data structure to implement a stack.
    # - Input: push(1), push(2), pop(), push(3), pop(), pop()
    # - Output: "1, None, 3, None, None"

from queue import Queue

class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, value):
        self.queue.put(value)

    def pop(self):
        if self.queue.empty():
            return None

        size = self.queue.qsize()

        # Remove and store all elements except the last one
        for _ in range(size - 1):
            self.queue.put(self.queue.get())

        # Remove and return the last element (top of the stack)
        return self.queue.get()

# Test the Stack class
stack = Stack()

stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: None


## FizzBuzz: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
    # - Input: None
    # - Output: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


## File I/O: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
    # - Input: A text file named "input.txt" with the content "Hello world"
    # - Output: A text file named "output.txt" with the content "Number of words: 2"

# Read the input file
with open('input.txt', 'r') as file:
    content = file.read()

# Count the number of words
word_count = len(content.split())

# Write the count to the output file
with open('output.txt', 'w') as file:
    file.write(f"Number of words: {word_count}")


## Exception Handling Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
    # - Input: 5, 0
    # - Output: "Cannot divide by zero."

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Example usage
num1 = 5
num2 = 0
division_result = divide_numbers(num1, num2)
print(division_result)

# stack and Queue in Python

# Stack operations 
# push()
# pop()
# peek()
# display()

#Qouue Operations


