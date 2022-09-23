########################################################################
##
## CS 101 Lab
## Program #4
## Name: James Buehlmann
## Email: jjbpn5@mail.umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Import Random Module
##      2. Asking the user how many chips they would like to start with. Repeats until user's input is between 1-100
##      3. Asking the user how many chips they would like to wager. Repeats until wager is greater than 0 and less or equal to their bank
##      4. Generating 3 random integers
##      5. Determining how many of the reels match
##      6. Calculating the user's payout depending on how many reels match
##      7. Asking the user if they would like to play again. Repeats until user inputs a valid input
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed

import random #Importing random module
def play_again() -> bool: 
    user_play_again = "." #Setting a placeholder for user_play_again
    while (user_play_again != "YES" or user_play_again != "Y" or user_play_again != "NO" or user_play_again != "N"): #Creating a loop that will repeat until user says YES, Y, NO, or N
        user_play_again = input("Do you want to play again? ==> ") #Asking user for an input on if they would like to play again
        user_play_again = user_play_again.upper() #Turns entire string uppercase
        if (user_play_again == "YES" or user_play_again == "Y"): #Creating outcome if user inputs YES or Y
            return True #Game plays again
        elif (user_play_again == "NO" or user_play_again == "N"): #Creating outcome if user inputs NO or N
            return False #Game ends
        else:
            print("You must enter Y/Yes/N/No to continue. Please try again")#Error message if user inputs an invalid input
            continue #Restarts loop
        


     
def get_wager(bank : int) -> int:
    user_wager = int(input("How many chips do you want to wager? ==> ")) #Asking for user input on how many chips they would like to wager
    while (user_wager <=0 or user_wager > bank): #Creating A loop that will repeat until user inputs a a valid wager
        if (user_wager <=0): #Checks if user inputs a wager less than or equal to 0
            print("The wager must be greater than 0. Please enter again.") #Error message if user input is less than or equal to 0
        elif (user_wager > bank): #Checks if user inputs a wager greater than what remains in their bank
            print("The wager cannot be greater than what you have. ", bank) #Error message if user input is greater than their bank
        user_wager = int(input("How many chips do you want to wager? ==> ")) #Restart loop
    return user_wager #Returns users wager

                    
          

def get_slot_results() -> tuple:
    a = (random.randint(1,10)) #Generates a number between 1-10
    b = (random.randint(1,10)) #Generates a number between 1-10
    c = (random.randint(1,10)) #Generates a number between 1-10
    return (a, b, c) #Returns slots results
    ''' Returns the result of the slot pull '''

def get_matches(reela, reelb, reelc) -> int:
    if (reela == reelb and reela == reelc and reelb == reelc): #Creating an outcome if all reels are the same
        return 3 #If all reels are the same 3 is returned
    if (reela == reelb and reela != reelc and reelb != reelc): #Creating an outcome if only reela and reelb match
        return 2 #If only reela and reelb match then 2 is returned
    if (reela != reelb and reela == reelc and reelb != reelc): #Creating an outcome if only reela and reelc match
        return 2 #If only reela and reelc match then 2 is returned
    if (reela != reelb and reela != reelc and reelb == reelc): #Creating an outcome if only reelb and reelc match
        return 2 #If only reelb and reelc match then 2 is returned
    if (reela != reelb and reela != reelc and reelb != reelc): #creating an outcome if no reels match
        return 0 #If no reels match 0 is returned
    

def get_bank() -> int:
    user_bank = 0 #Setting a placeholder for user_bank
    while (user_bank <=0 or user_bank >100): #Creating a loop until user inputs a starting chip amount betwee 1-100
        user_bank = int(input("How many chips do you want to start with? ==> ")) #Askinf user's input on how many chips they would like to start with
        if (user_bank <=0): #Creating an outcome is user inputs a starting chip amount less than or equal to 0
            print("Too low a value, you can only choose 1 - 100 chips") #Error message if input is less than or equal to 0
        elif (user_bank >100): #Creating an outcome if user inputs a starting chip amount greater than 100
            print("Too high a value, you can only choose 1 - 100 chips") #Error message if input is greater than 100
            continue #Restarts loop
    return (user_bank) #Returns users starting chip amount
                

def get_payout(wager, matches):
    if (matches == 3): #Creating an outcome if all 3 numbers match
        profit = wager *10 - wager #Users profit is their wager times 10 minus their wager
    elif (matches == 2): #Creating an outcome if only 2 numbers match
        profit = wager *3 - wager #Users profit is their wager time 3 minus their wager
    elif (matches == 0): #Creating an outcome if no number match
        profit = wager * -1 #Users profit is minus their wager
    return profit #Returns users profit



if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:  #Created a loop to repeat until bank is 0
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
  
        print("You lost all", 0, "in", 0, "spins") #I couldn't figure out how to get my code to calculate the number of spins, I tried different methods I found online but none worked
        print("The most chips you had was", 0) #I couldn't figure out how to get my code to determine the most chips the user had, I tried different methods I found online but none worked
        playing = play_again()
