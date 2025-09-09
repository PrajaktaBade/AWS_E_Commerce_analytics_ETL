#1.Create a text file and put 4-5 lines.Now create another file from the previous file and
#at the end of each line put the count of words.
#file = open("File1.txt","w")
#file.write("This is namaste sql course.\n"
#           "This is python course.\n"
#           "This assignment is part of day 4 lecture.")
#file.close()

#with open("File1.txt","r") as file1,open("file2.text",'w') as file2:
#    for line in file1:
#        line = line.strip()
#        word_count = len(line.split())
#        file2.write(line+":" + str(word_count)+"\n")

#2.Given below dictionaries of states and their capital:
#capitals_dict = {
#    'Alabama' : 'Montgomery',
#    'Alaska' : 'Juneau',
#    'Arizona' : 'Phoenix',
#    'Arkansas' : 'Little Rock',
#    'California' : 'Sacramento',
#    'Colorado' : 'Denver',
#    'Connecticut' : 'Hartford',
#    'Delware' : 'Dover',
#    'Florida' : 'Tallahassee',
#    'Georgia' : 'Atlanta'
#}

#Pick a state from above dictionary and ask user to enter the capital of the state.If the user
#answers incorrectly, then repeatedly ask them for the capital until they either enter the correct answer or type 'exit'.
#If the user answers correctly , then display "correct" and end the program.However, if the user exists without guessing
#correctly, display the correct answer and the word "Goodbye".

# Ask the user for the state
#state = input("Enter the name of the state: ")

# Check if the state exists in the dictionary
#if state in capitals_dict:
    # Ask the user for the capital
#    user_input = input(f"What is the capital of {state}? ")

    # Compare the user's input with the actual capital (case-insensitive)
#    if user_input.strip().lower() == capitals_dict[state].lower():
#        print("Correct!")
#    else:
#        print(f"Incorrect! The capital of {state} is {capitals_dict[state]}.")
#else:
#    print("State not found in the dictionary.")

#3.Write a program to take state as input from user and print the capital of the state using above dictionary.
#If the state is not there in dictionary then print "Sorry,Information not available"
#capitals_dict = {
#    'Alabama' : 'Montgomery',
#    'Alaska' : 'Juneau',
#    'Arizona' : 'Phoenix',
#    'Arkansas' : 'Little Rock',
#    'California' : 'Sacramento',
#    'Colorado' : 'Denver',
#    'Connecticut' : 'Hartford',
#    'Delware' : 'Dover',
#    'Florida' : 'Tallahassee',
#    'Georgia' : 'Atlanta'
#}
#state = input("Enter the name of the state: ")
#if state in capitals_dict:
#    print (f"The capital of {state} is {capitals_dict[state]}.")
#else:
#    print("State not found in the dictionary.")


#4.Let say you have one 100 cats. One day,you decide to arrange all your cats in a giant circle.
#Initially,none of your cats has a hat on.You walk around the circle a 100 times, always starting with the first cat(cat#1).
#Each time you stop at a cat, you check if it has a hat on.If it doesn't,then you put a hat on it.If it does, then you take
#the hat off.
#1.The first round,you stop at every cat,placing a hat on each one.
#2.The second round, you stop only at every second cat(#2,#4,#6,#8,and so on).
#3.The third round,you stop only at every third cat(#3,#6,#9,#12,and so on).
#4.You continue this process until you've made one hundred rounds around the cats.On the last round, you stop only at cat #100.

#Write a program that simply outputs which cats have hats at the end.

cats = [False] * (100+1)
cats_with_hats_on = []
for num in range(1,100+1):
    for cat in range(1,100+1):
        if cat % num == 0:
            if array_of_cats[cat] is True:
                array_of_cats[cat] = False
            else:
                array_of_cats[cat] = True
for cat in range(1,100+1):
    if array_of_cats[cat] is True:
        cats_with_hats_on.append(cat)

print(get_cats_with_hats(cats))