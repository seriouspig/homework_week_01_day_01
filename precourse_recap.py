print("Guess the number I'm thinking from 1 to 10, What do you think it is?")
guessing = True
number_list = [1,2,3,4,5,6,7,8,9,10]
import random
selected_number = random.choice(number_list)

while guessing == True:
    answer = int(input('Pick a number from 1 to 10: '))  

    if answer == selected_number:
        print("Great, you must be a psychic!")
        guessing = False
        break
    elif answer < selected_number:
        print("No, my number is higher, try again")
    elif answer > selected_number:
        print("No, my number is lower, try again")