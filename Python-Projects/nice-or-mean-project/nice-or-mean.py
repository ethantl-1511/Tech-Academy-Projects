##   Python: 3.10.7
##
##   Author: Ethan LaRocca
##
##   Purpose: Tech Academy project
##

def start(nice = 0, mean = 0, name = ""):
    # get user name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    # Check if user enters a name.
    if name != "":
        print("\nThank you for playing, {}!".format(name))
    else:
        stop = True
        while stop == True:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop == True:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M):\n>>> ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nquickly walks by...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # passes the 3 variables to score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored from nice_mean()
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else: # if neither nice nor mean conditions are met, run nice_mean() again
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name) # function to play game again

def lose(nice,mean,name):
    print("\nGame over. \nCongratulations {}, you're a jerk and no one loves you.".format(name))
    again(nice,mean,name) # function to play game again

def again(nice,mean,name):
    stop = True
    while stop == True:
        choice = input("\nDo you want to play again? (Y/N):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nThank you for playing!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Note: name variable is not reset because the same user has elected to play again
    start(nice,mean,name)

if __name__ == "__main__":
    start()