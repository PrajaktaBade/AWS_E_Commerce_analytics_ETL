#weight = int(input('Enter your weight:'))
#height = int(input('Enter your height:'))
#BMI = weight/(height*height)
#print(BMI)

#2.Write a program which takes the name of the user as input and replace all the o
# ccurence of character 'a' in the name to 'b' and print it.
# name = input("Enter your name: ")
#name1 = name.replace("a", "b")
#print(name1)

#3.Write a program which takes 2 inputs from user as principle amount(int) and
# rate of annual interest(float) and print the expected total amount after 2 years.
#principle = int(input("Enter the principle: "))
#rate = float(input("Enter the rate: "))
#year = 2
#amount = principle*rate*year
#print(amount)

#4Write a program which takes city name from user input irrespective of in which
# case user enters the city name,print the city name in camel meaning first letter
# should be capital and rest in small.
#city = input("Enter the city: ")
#city1 = city.capitalize()
#print(city1)

#5.Write a program which takes the name of the user as input and print the index of character 'a'
#in the string.If 'a' is not there then return -1.
#name = input("Enter the name: ")
#indexes = [i for i, char in enumerate(name) if char == 'a']
#if indexes:
#   print(f"Indexes of 'a':{indexes}")
#else:
#    print("Character 'a' not found")

#6.Display the number of letters in the below string
#my_word = "antidisestablishmentarianism"
#print(len(my_word))

#7.Take 3 inputs from user: first name,last name and age.Display the information in below format
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
#age = int(input("Enter your age: "))
#print(f"My name is {first_name} {last_name}, and I am {age} years old.")

#8.Take 3 inputs from user : first name, last name and company name.
#Create the email alias for the user and display it.Email alias is first 2 letters of first name,
#last 3 letters of last name and @company.com
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
company_name = input("Enter your company name: ")
print(f"{first_name[0:2]}{last_name[-3:]}@{company_name}.com")







