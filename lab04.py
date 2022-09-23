########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again():
    answer = input("Do you want to play again? ") 
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    print (answer)
    if (answer == "yes" or answer == "y"):
        return True
        
    elif(answer == "no" or answer == "n"):
        return False
    else:
        print("Please enter yes or no")
        play_again()

def get_wager(bank : int):
    wager = input("How much do you want to wager?")
    wager = int(wager)
    if(wager <= 0 or wager > bank):
        print("Please enter a valid amount ")
    else:
        return wager

def get_slot_results() -> tuple:
    ran1 = random.randint(1,10)
    ran2 = random.randint(1,10)
    ran3 = random.randint(1,10)
    ''' Returns the result of the slot pull '''
    return ran1,ran2,ran3
 
def get_matches(reela, reelb, reelc) -> int:
    if(reela == reelb == reelc):
         return 3

    elif(reela == reelb or reelb == reelc or reela == reelc):
        return 2

    else:
        return 0

def get_bank() -> int:
    print("How many chips do you want to start with? ")
    startamount = input()
    startamount = int(startamount)
    if(startamount > 0 and startamount < 101):
        return startamount
    else:
        print("Please enter a valid number.")
        get_bank()

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times 
the wager if 2 match, and negative wager if 0 match '''
    if(matches == 3):
        return (wager * 10)- wager
    elif(matches == 2):
        return (wager * 3) - wager
    else:
        return wager * -1
    
if __name__ == "__main__":
    playing = True
    while playing:
        bank = get_bank()
        while True:  # Replace with condition for if they still have money.
            
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
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()