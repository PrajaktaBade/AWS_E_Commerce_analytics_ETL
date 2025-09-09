#Day 3
#Given a list of numbers, write a program to find the mean of the numbers in list.
#def calculate_mean(values):
#    return sum(values)/len(values)

#values = [1,2,3,4,5]
#mean = calculate_mean(values)
#print("Mean:",mean)


#Given a list of numbers unsorted,write a program to find the median of the numbers in list.
def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)

    if n % 2 ==1:
        return sorted_values[n//2]
    else:
        middle1 = sorted_values[n//2 - 1]
        middle2 = sorted_values[n//2]
        return (middle1 + middle2)/2

values = [7,2,1,6,5,3]
median = calculate_median(values)
print("Median:",median)


#From a list of numbers create 2 list, one containing only the even numbers and other only the odd numbers.

def separate_even_odd(numbers):
    even_list = []
    odd_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    return even_list, odd_list

numbers = [7,2,1,6,5,3,8,10,9]
even_list, odd_list = separate_even_odd(numbers)

#Create a dictionary to store following attributes of CSK
#key "CSK" ; attributes : team full name, captain, playing 11 for each match(name of players)
#opponent name(assume there are 3 matches only against MI,RCB,GT) and result won/loss
def create_csk_info(team_name,captain,match_details):
    csk_info = {
        team_name: {
            "team_full_name": team_name,
            "captain":captain,
            "match_details": []
        }
    }

    for match in match_details:
        match_info = {
            "match_number": match["match_number"],
            "opponent": match["opponent"],
            "playing_11": match["playing_11"],
            "result": match["result"],
        }
        csk_info[team_name]["matches"].append(match_info)

    return csk_info
matches = [
    {
        "match_number": 1,
        "opponent": "MI",
        "playing_11": ["MS Dhoni", "Ravindra Jadeja", "Deepak Chahar", "Ruturaj Gaikwad",
                       "Moeen Ali", "Shivam Dube", "Dwayne Bravo", "Ambati Rayudu",
                       "Devon Conway", "Mukesh Choudhary", "Dwaine Pretorius"],
        "result": "won"
    },
    {
        "match_number": 2,
        "opponent": "RCB",
        "playing_11": ["MS Dhoni", "Ravindra Jadeja", "Deepak Chahar", "Ruturaj Gaikwad",
                       "Moeen Ali", "Shivam Dube", "Dwayne Bravo", "Ambati Rayudu",
                       "Devon Conway", "Mukesh Choudhary", "Chris Jordan"],
        "result": "loss"
    },
    {
        "match_number": 3,
        "opponent": "GT",
        "playing_11": ["MS Dhoni", "Ravindra Jadeja", "Deepak Chahar", "Ruturaj Gaikwad",
                       "Moeen Ali", "Shivam Dube", "Dwayne Bravo", "Ambati Rayudu",
                       "Devon Conway", "Mukesh Choudhary", "Simarjeet Singh"],
        "result": "won"
    }
]

# Creating the dictionary
csk_details = create_csk_info("Chennai Super Kings", "MS Dhoni", matches)
print(csk_details)