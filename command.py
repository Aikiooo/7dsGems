import datetime
from datetime import timedelta
import os
import json
import sys

# Get today's date
now = datetime.datetime.today()
today = now.date()

dayRewardMonthly = None
dayRewardWeekly = None

gemsPvP = 0
gemsLogin = 0
gemsEventLogin = 0
gemsWeeklyBundle = 0
gemsMonthlyBundle = 0
gemsDailies = 0
gemsMaintenance = 0
gemsEventContent = 0
gemsKnighthood = 0
pvp = None
options = {
    "Champion1": 60,
    "Champion2": 56,
    "Champion3": 54,
    "Champion4": 52,
    "Champion5": 50,
    "Master1": 50,
    "Master2": 48,
    "Master3": 46,
    "Master4": 44,
    "Master5": 42,
    "Platinium1": 42,
    "Platinium2": 40,
    "Platinium3": 38,
    "Platinium4": 36,
    "Platinium5": 34,
    "Gold1": 34,
    "Gold2": 32,
    "Gold3": 30,
    "Gold4": 28,
    "Gold5": 26,
    "Silver1": 26,
    "Silver2": 24,
    "Silver3": 22,
    "Silver4": 20,
    "Silver5": 18,
    "Bronze1": 18,
    "Bronze2": 16,
    "Bronze3": 14,
    "Bronze4": 12,
    "Bronze5": 10,
}

curDir = os.path.dirname(os.path.realpath(__file__))
file_name = "inputs"
path = f"{curDir}\{file_name}.json"

doWeekly = False
doMonthly = False
boolLogin = False
useFile = False

if os.path.exists(path):
    yorn = input("A json file already exist, want to use this one (y/n)? : ")
    if yorn == "y" or yorn == "Y" or yorn == "Yes":
        useFile = True
        f = open(path)
        data = json.load(f)
        date = datetime.datetime.strptime(data['Date'], "%Y-%m-%d")
        date = date.date()
        dateDiff = today - date
        days_difference = dateDiff.days
        if "BuyWeekly" in data:
            if data["BuyWeekly"]:
                dayRewardWeekly = data['Weekly'] + days_difference
                doWeeklyFile = True
            else:
                doWeeklyFile = False
        else:
            raise Exception("Something is missing in your json file, you cannot not use it")
        if "BuyMonthly" in data:
            if data["BuyMonthly"]:
                dayRewardMonthly = data['Monthly'] + days_difference
                doMonthlyFile = True
            else:
                doMonthlyFile = False
        else:
            raise Exception("Something is missing in your json file, you cannot not use it")   
        if "DayLogin" in data:
            dayLogin = int(data['DayLogin'])
            boolLogin = True
        else:
            raise Exception("Something is missing in your json file, you cannot not use it")
        if "PvP" in data:
            pvp = str(data['PvP'])
        else:
            raise Exception("Something is missing in your json file, you cannot not use it")
        
        boolScript = True

def eventLogin(days):
    fileEvent = "events"
    pathEvent = f"{curDir}\{fileEvent}.json"
    g = open(pathEvent)
    data2 = json.load(g)
    date = datetime.datetime.strptime(data2['start'][0], "%Y-%m-%d")
    date = date.date()
    dateDiffEvent = date - today
    daysDifferenceEvent = abs(365 + dateDiffEvent.days) -1
    negativeValue = -daysDifferenceEvent
    count = negativeValue + days

    if count >= 0 and count <=27:
        total = int(data2['loginEvent'][count])
        return total
    else:
        return 0

def eventContent(days):
    fileEvent = "events"
    pathEvent = f"{curDir}\{fileEvent}.json"
    g = open(pathEvent)
    data2 = json.load(g)
    date = datetime.datetime.strptime(data2['start'][0], "%Y-%m-%d")
    date = date.date()
    dateDiffEvent = date - today
    daysDifferenceEvent = abs(365 + dateDiffEvent.days) -1
    negativeValue = -daysDifferenceEvent
    count = negativeValue + days
    
    if count == 0:
        total = int(data2["freeSumonEquivalent"][0]) + int(data2["eventBoss"][0]) + int(data2["fromMissions"][0])
        return total
    else:
        return 0
    
def weeklyCalc(boolWeekly, days, startingDayWeekly):
    if not boolWeekly:
        return 0
    
    if boolWeekly:
        gemsFromWeekly = 0
        iterations = 0
        day = startingDayWeekly
        
        while iterations < days:
            gemsFromWeekly += 7
            day += 1
            if day > 7:
                gemsFromWeekly += 10
                day = 1
            iterations += 1
        return gemsFromWeekly
    
def monthlyCalc(boolMontly, days, startingDayMonthly):
    if not boolMontly:
        return 0
    
    if boolMontly:
        gemsFromMonthly = 0
        iterations = 0
        day = startingDayMonthly
        
        while iterations < days:
            gemsFromMonthly += 5
            day += 1
            if day > 28:
                gemsFromMonthly += 30
                day = 1
            iterations += 1
        return gemsFromMonthly

def rewardPvP():
    while True:
        try:
            rankPvP = input("Please select an option: Champion (1), Master (2), Platinum (3), Gold (4), Silver (5), Bronze (6): ")
            rankPvP = int(rankPvP)

            if rankPvP in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

    if rankPvP == 1:
        print("You selected Champion.")
        rankPvP = "Champion"
    elif rankPvP == 2:
        print("You selected Master.")
        rankPvP = "Master"
    elif rankPvP == 3:
        print("You selected Platinum.")
        rankPvP = "Platinium"
    elif rankPvP == 4:
        print("You selected Gold.")
        rankPvP = "Gold"
    elif rankPvP == 5:
        print("You selected Silver.")
        rankPvP = "Silver"
    elif rankPvP == 6:
        print("You selected Bronze.")
        rankPvP = "Bronze"
        
    while True:
        try:
            divisionPvP = input("What division are you in ? Division 1 (1), Division 2 (2), Division 3 (3), Division 4 (4), Division 5 (5): ")
            divisionPvP = int(divisionPvP)

            if divisionPvP in [1, 2, 3, 4, 5]:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
                
    print(f'You selected {rankPvP} {divisionPvP}')
    pvp = rankPvP+str(divisionPvP)
    return(pvp)

def printWhatEarned(earnedLocation, textEarnedLocation):
    return(f"You\'ve earned: {earnedLocation} from {textEarnedLocation}")

def isTrue(response):
    response = response.lower()
    if response == "no" or response == "n":
        return False
    elif response == "Yes" or response == "y":
        return True
    else:
        print("Invalid response. Expected answer (y/n)")
        return isTrue(input())

def get_integer(sentence):
    while True:
        try:
            # Ask the user for input and store it in a variable
            user_input = int(input(sentence))

            # If the input is a valid integer, return the input and exit the function
            return user_input
        except ValueError:
            # If the input is not a valid integer, print an error message and continue the loop
            print("Sorry, that was not a valid integer. Please try again.")

# Prompt the user for the initial value of the gem variable
gems = input('How many gems do you have? : ')
gems = int(gems)

# Prompt the user for the number of days to consider
days = input('For how many days does it has to calculate? : ')
days = int(days)

# Prompt the user for which login reward are they at
while True:
    try:
        if not boolLogin:
            dayLogin = get_integer("Type which day you are on your login bonus (1 to 14): ")
        if 1 <= dayLogin <= 14:
            break
        else:
            print("Sorry, that was not a valid integer between 1 and 14. Please try again.")
    except ValueError:
        print("Sorry, that was not a valid integer. Please try again.")
if dayLogin > 7:
    dayLogin -= 7
saveDayLogin = dayLogin
    

# Does user buy weekly and monthly?
if useFile:
    if not 'doWeeklyFile' in locals() and not 'doMonthlyFile' in locals():
        raise Exception("Issue with the inputs.json file")
    else:
        gemsWeeklyBundle += weeklyCalc(doWeeklyFile, days, dayRewardWeekly)
        gemsMonthlyBundle += monthlyCalc(doMonthlyFile, days, dayRewardMonthly)
    
else:
    doWeekly = isTrue(input('Do you want to purchase the weekly bundle? (y/n) : '))
    if doWeekly:
        dayRewardWeekly = int(input('At what day reward are you (0 if not purchased, or 1 to 7): '))
        gemsWeeklyBundle += weeklyCalc(doWeekly, days, dayRewardWeekly)
    
    doMonthly = isTrue(input('Do you want to purchase the monthly bundle? (y/n): '))
    if doMonthly:
        dayRewardMonthly = int(input('At what day reward are you (0 if not purchased, or 1 to 28): '))
        gemsMonthlyBundle += monthlyCalc(doMonthly, days, dayRewardMonthly)
    
    pvp = rewardPvP()

# Iterate over the number of days given
for i in range(days):
    gemsEventLogin += eventLogin(i)
    gemsEventContent += eventContent(i)
    # Calculate the date for the current day in the loop
    date = today + timedelta(days=i+1)
    # Check if the current date is a Monday
    if date.weekday() == 0:
        gemsPvP += int(options[pvp])
    if date.weekday() == 1:
        gemsMaintenance += 2
        
    dayLogin = dayLogin % 7 + 1
    if dayLogin == 2 or dayLogin == 6:
        gemsLogin += 5
        
    gemsKnighthood += 1
    gemsDailies += 4
    
print(printWhatEarned(gemsWeeklyBundle, "gems from the Weekly Bundle"))
print(printWhatEarned(gemsMonthlyBundle, "gems from the Monthly Bundle"))
print(printWhatEarned(gemsPvP, " gems from the PvP reward"))
print(printWhatEarned(gemsLogin, " gems from base login reward"))
print(printWhatEarned(gemsEventLogin, " gems from the event login reward"))
print(printWhatEarned(gemsKnighthood, " gems from checking in your Knighthood"))
print(printWhatEarned(gemsDailies, " gems from doing your dailies every day"))
print(printWhatEarned(gemsMaintenance, "gems from the maintenance compensation"))
print(printWhatEarned(gemsEventContent, "gems from the events currently available"))
gems+= gemsWeeklyBundle + gemsMonthlyBundle + gemsPvP + gemsLogin + gemsEventLogin + gemsKnighthood + gemsDailies + gemsMaintenance + gemsEventContent
print(f'Total gems will be: {gems}')

data = {
    "BuyWeekly": doWeekly,
    "Weekly": dayRewardWeekly,
    "BuyMonthly": doMonthly,
    "Monthly": dayRewardMonthly,
    "DayLogin": saveDayLogin,
    "PvP" : pvp,
    "Date": str(today)
}

if not useFile:
    response = isTrue(input("Do you want to save your inputs into a json file (y/n)? : "))
    if response:
        with open(path, "w") as output_file:
            # Write the data to the file in JSON format
            json.dump(data, output_file)
            print("File created")
    else:
        print("No file created")
    
sys.exit()