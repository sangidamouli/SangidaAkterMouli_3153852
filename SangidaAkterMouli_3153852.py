import random

#defining function to generate random nunmber between start and end (Inclusive)
def rand(start,end):
    number=random.randint(start,end+1)
    return number

#calling the fuction
rand_number=rand(1,100)

#declaring and assigning variables
attempts=0
guess=500

#running loop while condition is met
while(guess != attempts):
    guess=input("Enter a number between 1 and 100 to guess: (Enter 0 to quit)")
    #fixing error for empty input
    if(guess==""):
        continue
    #Setting Condition when guess number is higher than rnadom number
    elif(int(guess)>rand_number):
        print("Too High!")
        attempts+=1
        #Setting Condition when guess number is lower than rnadom number
    elif(int(guess)<rand_number):
        print("Too Low!")
        attempts+=1
        #Setting Condition when guess number matches the  rnadom number
    elif(int(guess)==rand_number):
        print("Correct guess!")
        attempts+=1
        break
    #Giving option to exit the game
    elif(int(guess)==0):
        print("Game Over!")
        break

print(f"The number of attempts is : {attempts}")



