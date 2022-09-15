#printing 'Welcome to the Flarsheim Guesser!' message
print('Welcome to the Flarsheim Guesser!')
print()
play_again = 'Y'
#While loop until the user states 'N' or 'n'
while (play_again == 'Y' or play_again == 'y'):
#Asking user to think of a number between 1 and 100
    print('Please think of a number between and including 1 and 100.')
    print()
#Asking users input on remainder after number is divided by 3
    divide_three = int(input('What is the remainder when your number is divided by 3 ?'))
#while loop to repeat until user gives an input between 0-2
    while (divide_three <0 or divide_three >=3):
        if (divide_three >=3):
#Error message if users input is greater than or equal to 3
            print('The value entered must be less than 3')
        elif (divide_three <0):
#Error message if users input is less than 0
            print('The value entered must be 0 or greater')
        divide_three = int(input('What is the remainder when your number is divided by 3 ?'))
#Asking users input on remainder after number is divided by 5
    divide_five = int(input('What is the remainder when your number is divided by 5 ?'))
#while loop to repeat until user gives an input between 0-5
    while (divide_five <0 or divide_five >=5):
        if (divide_five >=5):
#Error message if users input is greater than or equal to 5
            print('The value entered must be less than 5')
        elif (divide_five <0):
#Error message if users input is less than 0
            print('The vaule entered must be 0 or greater')
        divide_five = int(input('What is the remainder when yout number is divided by 5 ?'))
#Asking users input on remainder after number is divided by 7
    divide_seven = int(input('What is the remainder when your number is divided by 7 ?'))
#While loop to repeat until user gives an input between 0-7
    while (divide_seven <0 or divide_seven >=7):
        if (divide_seven >=7):
#Error message if users input is greater than or equal to 7
            print('The value entered must be less than 7')
        elif (divide_seven <0):
#Error message if users input is less than 0
            print('The value entered must be 0 or greater')
        divide_seven = int(input('What is the remainder when your number is divided by 7 ?'))
#Calculating users number based on remainder inputs
    for i in range(1,101):
        if(i%3 == divide_three and i%5 == divide_five and i%7 == divide_seven):
            print('Your number was', i)
            print('How amazing is that?')
    print()
#Asking user id they would like to play again
    play_again = (input('Do you want to play again? Y to continue, N to quit ==>'))
#While loop to repeat message until player gives a response of 'Y', 'y', 'N', or 'n'
    while (play_again != 'Y' and play_again != 'y' and play_again != 'N' and play_again != 'n'):
        play_again = (input('Do you want to play again? Y to continue, N to quit ==>'))
