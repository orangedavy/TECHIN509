"""

Program: Calorie_Counter_Davy.py
Author: Shucheng Guo
Date-Written: 10/6/2022
Description: This program helps calculate calories one burns
             based on his gender, age, weight, heart rate and time of movement.

Variables Used:

itn1 - the intention of users to use the program
gender - user's gender
age - user's age
weight - user's weight
heartRate - user's heart rate after movement
time - user's time of movement
clr_burnt - the calories user has burnt
itn2 - the intention of users to calculate calories again
ttl_clr_burnt - total calories user has burnt
count - numbers user has used the calculation
avr_clr_burnt - average calories user has burnt one time

"""

# checks user's intention to calculate

itn1 = input("Would you like to compute calories burnt? (Y/N)").upper()

if itn1 == "Y":
    pass
    print("Here we go!")
else:
    print("Goodbye!")
    exit()


def cb():

    # prompts for user inputs of their data
    gender = input("Please enter your gender: (M/F)").upper()
    age = int(input("Please enter your age: (in years)"))
    weight = float(input("Please enter your weight: (in pounds)"))
    heart_rate = int(input("Please enter your heart rate: (in beats per minute)"))
    time = float(input("Please enter your time of movement: (in minutes)"))

    # uses a gender-specific algorithm to calculate calories
    if gender == "M":
        clr_burnt = ((age * 0.2017) - (weight * 0.09036) + (heart_rate * 0.6309) - 55.0969) * time / 4.184
    elif gender == "F":
        clr_burnt = ((age * 0.074) - (weight * 0.05741) + (heart_rate * 0.4472) - 20.4022) * time / 4.184
    else:
        print("Wrong Gender.")
        exit()

    # reports error if no effective calories burnt
    if clr_burnt <= 0:
        print("Oops! You haven't burnt any calories, try harder!")
        exit()

    return clr_burnt


# prints and defaults in the first process

clr_burnt = round(cb(), 2)
print("You've burnt ", clr_burnt if clr_burnt > 0 else 0, " calories.")

ttl_clr_burnt = clr_burnt
count = 1

# checks intention again whether to calculate another calorie count

itn2 = input("Would you like to do another calculation? (Y/N)")

while itn2.upper() == "Y":
    clr_burnt = round(cb(), 2)
    print("You've burnt ", clr_burnt, " calories.")
    count += 1
    ttl_clr_burnt += clr_burnt
    avr_clr_burnt = ttl_clr_burnt / count
    itn2 = input("Would you like to do another calculation? (Y/N)")
    continue

# ends processing if users enters no

if itn2 == "N":
    print("Your average calories burnt is: ", avr_clr_burnt, " calories.")
    print("Your total calories burnt is: ", ttl_clr_burnt, " calories.")
    exit()
else:
    print("Wrong Answer.")
    exit()
