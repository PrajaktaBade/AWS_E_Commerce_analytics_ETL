#1. given a list of numbers,Write a program to find the mean of the numbers in list.
#num = [1,2,3,4,5]
#mean = sum(num)/len(num)
#print(mean)

# 2.Given a list of numbers unsorted , Write a program to find the median of the numbers in list.
#num1 = [5,1,3,2,4]
#num1.sort()
#length = len(num1)
#if length % 2 == 0:
#    median = num1[length//2]
#else:
#    median = (num1[length//2 - 1] + num1[length//2])/2
#print("Median : ", median)

#3.From a list of numbers create 2 list,one containing only the even numbers and other
# only the odd numbers.
#num = [1,2,3,4,5,6]
#num_even = []
#num_odd = []
#for num in num:
#  if num % 2 == 0 :
#    num_even.append(num)
#  else :
#    num_odd.append(num)

#print("Even Numbers list: ", num_even)
#print("Odd Numbers list: ", num_odd)

#4.Create a dictionary to store following attribute of CSK
#key "CSK"; attributes : team full name, captain,playing 11 for each (name of players),
# opponent name(assume there are 3 matches only against MI, RCB,GT) and result won/loss.
#CSK = {
#    "team_name" : "Chennai Super Kings",
#    "Captain" :"MS Dhoni",
#    "Playing_11":[
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"],
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"],
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"]
#    ],
#    "Opponents" : ["MI","RCB","GT"],
#    "result" : ["Won","Loss","Won"]
#}


# 5.In the previous dictionary add one more item for RCB.You can choose any 3 opponents.
#IPL = {"CSK" : {
#    "team_name" : "Chennai Super Kings",
#    "Captain" :"MS Dhoni",
#    "Playing_11":[
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"],
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"],
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"]
#    ],
#    "Opponents" : ["MI","RCB","GT"],
#    "result" : ["Won","Loss","Won"]
#},
#"RCB" : {
#    "team_name" : "Royal Challengers Banglore",
#    "Captain" :"Virat Kohali",
#    "Playing_11":[
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"],
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"],
#        ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6", "Player 7","Player 8","Player 9","Player 10","Player 11"]
#    ],
#    "Opponents" : ["MI","CSK","GT"],
#    "result" : ["Loss","Loss","Loss"]
#}
#}
#print(IPL)

#6.write a program to take a positive number as input from user.If the user enters negative number then keep
#promting him to enter positive number until he enters the positive number and then print the same:
#number = int(input("Enter a positive number: "))
#while number < 0:
#    print("Invalid input please enter a positive number")
#    number = int(input("Enter a positive number: "))
#print("The positive number you entered is :", number)

#7.Consider the below list contains following information:
#universities = [
#    ['California Institute of Technology',2175,37704],
#    ['Harvard',19627,39849],
#    ['Massachusetts Institute of technology',10566,40732],
#    ['Princeton',7802,37000],
#    ['Rice',5879,35551],
#    ['Stanford',19535,40569],
#    ['Yale',11701,40500]
#]

#Write a program to print following information:
#1.a list of all the universities
#2.Total number of student enrolled in all the universities together
#3.Mean of tuition fees

#universities_names = []
#for university in universities:
#    universities_names.append(university[0])
#print("List of all universities:",universities_names)

#total_students = 0
#for university in universities:
#    total_students = total_students + university[1]
#print("Total number of students enrolled in all universities:",total_students)

#tuition_fees = []
#for university in universities:
#    tuition_fees.append(university[2])
#mean_tuition = sum(tuition_fees)/len(tuition_fees)
#print("Mean tuition of all universities:",mean_tuition)

#8.Write a program to convert above universities list to a dictionary.The keys should be the
# name of the university.
#universities_dict ={}
#for university in universities:
#    name = university[0]
#    attributes ={
#     "total_students":university[1],
#    "tuition_fees": university[2]
#    }
#    universities_dict[name] = attributes

#9.Write a program that reverses a given string.For example,if the input is "Hello" from user, the output should be "olleH"
#user_input =  input("Enter a string: ")
#reversed_string = user_input[::-1]
#print(reversed_string)

#10.write a program that finds the largest number in a list(unsorted) of integers without
#using sort/sorted method.
numbers = [12,45,37,48,90,12,57]
largest_number = max(numbers)
print(largest_number)
