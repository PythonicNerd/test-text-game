import os

# Function that clears screen
def clear():
    tmp = os.system('cls')  # For Windows
    tmp = os.system('clear')  # For Linux/OS X

def handle_choices(option1, option2):
    while True:
        print("Do you %s [1], or %s [2] ?" %(option1, option2))

        try:
            choice = int(input("> "))

            if choice == 1:
                return True
            elif choice == 2:
                return False
            else:
                raise("Invalid choice")
        except:
            print("Sorry, that wasn't a correct choice! Please choose either [1] or [2]")
            print('\n')

def lose():
    print("You lose!")
    print("Hit enter to continue!")
    input()
    exit()
# Beginning of the game

name = input("Hello, what's your name?")
money = 0

clear()
print("Greetings %s! It is the year 4000, and the United States has converted to the superior economic system that is communsim. \nAs part of what is now called the \"Marx Tax\", Citizens are now expected to pay $1000 per month in order to support the working class." %(name))
print("\nUnfortunently, money has been been tight this month, and you haven't put any of it towards this month's Marx Tax.")
print("You need to get money, and fast!")
print("You stand outside of your apartment complex.")
street = handle_choices("wander the streets", "go to the Bounty Office to try and find a contract")

clear()

if street:
    print("You explore the city a little bit, until you see a $100 bill blow into the sewers after a hard gust of wind.")
    follow_bill = handle_choices("follow the bill", "keep walking")

elif not street:
    print(
    """
    The man behind the counter gives you the choice of three jobs that pay the whole month's Marx Tax. One is fighting the immortal spirit of a rapper from years past that goes by 'Lil Pump, another is finding a robot that wakes people up at night by playing bass boosted songs at night, and the last job, the one that pays the most is killing an ancient god steve from the minecraft realm, you are warned that although thousands of people have tried to kill him none has even wounded steve, and all that have tried to kill him have failed.
    """
    )
    pump = None
    robot = None
    steve = None

    while True:
        print("Do you %s [1], or %s [2], or %s [3] ?" %("Fight 'Lil Pump", "Beat up the robot", "Destroy STEVE"))

        try:
            choice = int(input("> "))

            if choice == 1:
                pump = True
                robot = False
                steve = False
                break
            elif choice == 2:
                pump = False
                robot = True
                steve = False
                break
            elif choice == 3:

                pump = False
                robot = False
                steve = True
                break
            else:
                raise("Invalid choice")
        except:
            print("Sorry, that wasn't a correct choice! Please choose either [1] or [2]")
            print('\n')
    clear()
    if pump:
        print("After receiving the contract, you walk down the streets, hearing 'Lil Pump yell \"Seventy\" and \"Eskettit\". After following the voices you get a glimpse of 'Lil Pump's muscley stature. You consider different ways to fight him, and think of 2.")
        fight = handle_choices("challenge 'Lil Pump to fist-fight", "challenge 'Lil Pump to a battle of the minds")

        clear()

        if fight:
            print("'Lil Pump is a bit hunkier than you expected! You are promptly kachigga'd by the Pump's insase physical prowess")
            lose()
