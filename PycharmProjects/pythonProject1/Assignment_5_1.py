#1.Write a python function which takes a positive number as input and return the factorial of the number.
def factorial(n):
    if n<0:
        return "Input must be a positive number."
    elif n==0 or n==1:
        return 1
    else:
        result = 1
        for i in range(2,n+1):
            result *=i
        return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")

#2.Write a python function that accepts a string and counts the number of upper and lower case letters.
def count_upper_lower(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

string = 'Hello World!'
upper,lower = count_upper_lower(string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")


#3. write a python function that takes a list and returns a new list with distinct elements from the first list.
def distinct_elements(lst):
    return list(set(lst))

original_list = [1,2,2,3,4,4,5]
new_list = distinct_elements(original_list)
print(f"Original list: {original_list}")
print(f"List with distinct elements: {new_list}")


#4.Write a python function that checks whether a passed string is a palindrome or not.
def is_palindrome(s):
    s = s.replace(" "," ").lower()
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#5.Write a python program that accepts a hyphen-separated sequence of words as input and prints the words in a
#hyphen-separated sequence after sorting them alphabetically.
def sort_hyphenated_words(sequence):
    words = sequence.split('-')
    words.sort()
    return '-'.join(words)

input_sequence = input("Enter a hyphen-separated sequence of words: ")
sorted_sequence = sort_hyphenated_words(input_sequence)
print(f"Sorted sequence: {sorted_sequence}")


#6.Write a python function that accepts a string and prints the count of occurence of each characters
def count_letters(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1


    for char,count in char_count.items():
        print(f"{char}: {count}")

input_string = "Hello World"
count_letters(input_string)

#7.Write a function called is_prime that takes an integer as an argument and
# returns True if it is a prime number, and False otherwise.
def is_prime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 ==0 or number % 3 ==0:
        return False

    i = 5
    while i*i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i +=6
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"The number is prime.")
else:
    print(f"The number is not prime.")

#8.Write a function called generate_fibonacci that takes an
# integer n as input and returns a list of the first n Fibonacci numbers.
def generate_fibonacci(n):
    if n <= 0:
        return[]
    elif n == 1:
        return [0]
    fibonacci_sequence = [0,1]

    for i in range(2,n):
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_number)

# Example usage:
n = 10
fibonacci_numbers = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers: {fibonacci_numbers}")

#9.Write a function called capitalized_odd_letters that takes a string as input
# and returns the same string with the odd-indexed letters capitalized.
def capitalized_odd_letters(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 1:
            result += s[i].upper()
        else:
            result += s[i]
    return result

input_string = "Hello World"
output_string = capitalized_odd_letters(input_string)
print(f"Original String: {input_string}")
print(f"Modified String: {output_string}")

#10.Write a function called find_common_elements that takes two lists and returns a new
#list containing the common elements between the two lists.

def find_common_elements(list1,list2):
    common_elements = list(set(list1).intersection(list2))
    return common_elements

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common = find_common_elements(list1,list2)
print(f"Common elements: {common}")
