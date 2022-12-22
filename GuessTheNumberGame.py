import random
print("Welcome to guess the number game!!")
print("You will only be given 9 chances to figure outwhat the number is")
ActualNumber=random.randint(0,100)
i=0

while(i<9):
    displaynum1=i+1
    displaynum2=8-i
    USer_Input=int(input(f"Enter your number {displaynum1} guess: "))
    if(USer_Input==ActualNumber):
        print("Yeah you got that right\nYOU WON")
        print(f"No. of turns left {displaynum2}")
        break
    
    elif(USer_Input>ActualNumber):
        print("Your guess is greater than the actual number")

    elif(USer_Input<ActualNumber):
        print("Your guess is lesser than the actual number")

    print(f"No of Turns left {displaynum2}")

    i=i+1

if(USer_Input!=ActualNumber):
    print("YOU LOST!")

print(f"Number of guesses you took to finish the game is: {displaynum1}")