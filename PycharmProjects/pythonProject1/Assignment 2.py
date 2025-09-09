#1.Write a program which takes single input from user containing first name, last name and age as comma
#separated value and display then in 3 lines in given format below.
#user_input = input("Enter your first name,last name & age: ")
#first_name, last_name, age = user_input.split(',')
#print("First name is ", first_name)
#print("Last name is ", last_name)
#print(first_name, "is",age, "years old.")

#2.Given 2 list as and display the same without using extended method.
#list1 = [1,3,4]
#list2 = [2,4,6]
#combined_list = list1 + list2
#print(combined_list)

#3.Given list list1 = [1,2,3,4,5,6,7,8].Display a new list which contains only odd position index
# values from above list.
#list1 = [1,2,3,4,5,6,7,8]
#odd_position_values = list1[1::2]
#print(odd_position_values)

#4.ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS'].Take a ipl team name as input from user and display
#a list of all elements from that name.
#ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
#team_name = input('Enter ipl team name : ')
#ipl.append(team_name)
#print("updated ipl list : ",ipl)

#5. ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS'].Take a ipl team name as input from user and display
#list of all elements except input one.
#ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
#team_name = input("Enter ipl team name : ")
#team_elements = ipl.copy()
#team_elements.pop(ipl.index(team_name))
#print("updated ipl list : ",team_elements)

#6.ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS'].Take a user input contains 2 comma separated values index,
#new_team.Replace the index element of list with new value and display the same.
#ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
#user_input = input("Enter the index and new team : ")
#index, new_team = user_input.split(',')
#index = int(index)
#ipl[index] = new_team
#print("updated ipl list : ",ipl)

#7. ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']. Take a ipl team name as user input.Display True
#if the team exists else display false.
#ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
#team_input = input("Enter a team name : ")
#print(True if team_input in ipl else False)

#8.ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS'] Take a user input conatins 2 comma separated values index, new_team
#Add the new value at that index in the list.Display the old list, new list, length of original and new list.
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
user_input = input("Enter the index and new team name : ")
index , new_team = user_input.split(',')
index = int(index)
print("old list: ",ipl)
print("length of original list: ",len(ipl))
new_team_list = ipl.insert(index,new_team)
print("New ipl list : ", ipl)
print("Length of new ipl list : ",len(ipl))
