# Python:   3.10.7
#
# Author:   Ethan LaRocca
#
# Purpose:  The Portland-based company you work for just 
#           opened two new branches. One is in New York City,
#           the other in London. They need a very simple program 
#           to find out if the branches are open or closed. 
#           The hours of both branches are 9:00 a.m.-5:00 p.m. 
#           in their own time zone.

# importing modules
from datetime import datetime 
from pytz import timezone

format = "%H:%M:%S %Z%z" # time format
time = datetime.now(timezone('UTC')) # variable for base UTC time

portlandBranch = "Portland"
portlandTime = time.astimezone(timezone('US/Pacific')) # timezone for Portland
nycBranch = "New York City"
nycTime = time.astimezone(timezone('US/Eastern')) # timezone for New York City
londonBranch = "London"
londonTime = time.astimezone(timezone('Europe/London')) # timezone for London

# function to check if branch is open or closed
def isOpen(time,branch):
    localHour = time.strftime("%H%M") # converting time to string
    if 900 <= int(localHour) <= 1700: # if the 'time' is between 900 (9am) and 1700 (5pm),
        print("{} Branch Status: OPEN".format(branch)) # print OPEN
    else: # if 'time' is NOT between 9am-5pm,
        print("{} Branch Status: CLOSED".format(branch)) # print CLOSE

isOpen(portlandTime, portlandBranch) # call function, pass portland parameters
isOpen(nycTime, nycBranch) # call function, pass NYC parameters
isOpen(londonTime, londonBranch) # call function, pass london parameters