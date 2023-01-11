import datetime
from datetime import timedelta
import os
import json
import sys
import hashlib

github_url = "https://github.com/Aikiooo/7dsGems"
try:
    import requests
    with open('7dsGems.py', 'rb') as f:
        local_hash = hashlib.sha1(f.read()).hexdigest()
    try:
        # check internet connection
        r = requests.get("https://github.com/")
        r.raise_for_status()
        response = requests.get('https://raw.githubusercontent.com/Aikiooo/7dsGems/master/7dsGems.py')
        remote_hash = hashlib.sha1(response.content).hexdigest()

        if not local_hash == remote_hash:
            print(f"Not up to date, download latest version of the script --> \033[1;34;40m{github_url}\033[0m <--")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"No Internet connection, check for latest version of the script here --> \033[1;34;40m{github_url}\033[0m <--")

except ImportError:
    raise SystemExit(f"Cannot check if the script is up to date, check yourself here --> \033[1;34;40m{github_url}\033[0m <-- ")

    
with open('7dsGems.py', 'rb') as f: 
    local_hash = hashlib.sha1(f.read()).hexdigest()

# Get today's date
now = datetime.datetime.today()
today = now.date()

dayRewardMonthly = None
dayRewardWeekly = None

gemsPvP = 0
gemsLogin = 0
gemsWeeklyBundle = 0
gemsMonthlyBundle = 0
gemsDailies = 0
gemsMaintenance = 0
gemsEvent = 0
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

eventList = [{
                "start": ["2023-01-03"],
                "loginEvent": [30, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                "freeSumonEquivalent": [30],
                "eventBoss": [5],
                "fromMissions": [10]
             },
             {
                "start": ["2023-01-17"],
                "finalBoss": [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35],
                "specialStoryEvent": [5],
                "boostedDailies": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
             }
]

file_name = "inputs"
path = f".\{file_name}.json"

doWeekly = False
doMonthly = False
boolLogin = False
useFile = False

def event():
    eventContentGems = 0
    eventLoginGems = {}
    
    for xEvent in eventList:
        dateDiffEvent = (today - datetime.datetime.strptime(xEvent['start'][0], "%Y-%m-%d").date()).days
        for key, values in xEvent.items():
            if key == "start":
                continue
            elif len(values) > 1:
                eventLoginGems[key] = 0
                if dateDiffEvent < 0:
                    range_start = 0
                    range_end = days + dateDiffEvent + 1
                else:
                    range_start = dateDiffEvent + 1
                    range_end = dateDiffEvent + days + 1
                for value in values[range_start:range_end]:
                    if isinstance(value, (int,float)):
                        eventLoginGems[key] += value
                if wantDetailedEvent and eventLoginGems[key] > 0 : print(f"You've earned: {eventLoginGems[key]} gems from {key}")
            elif len(values) == 1:
                if dateDiffEvent < 0:
                    range_start = 0
                    range_end = days + dateDiffEvent
                else:
                    range_start = dateDiffEvent
                    range_end = dateDiffEvent + days
                for value in values[range_start:range_end]:
                    if isinstance(value, (int,float)):
                        eventContentGems += value
                if wantDetailedEvent and eventContentGems > 0 : print(f"You've earned: {eventContentGems} gems from {key}")

        
    return eventContentGems, eventLoginGems
    
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
    elif response == "yes" or response == "y":
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

if os.path.exists(path):
    useFile = isTrue(input("A json file already exist, want to use this one (y/n)? : "))
    if useFile:
        f = open(path)
        data = json.load(f)
        savedDate = datetime.datetime.strptime(data['Date'], "%Y-%m-%d")
        savedDate = savedDate.date()
        days_difference = (today - savedDate).days
        if "WantDetailedEvent" in data:
            if data["WantDetailedEvent"]:
                wantDetailedEvent = True
            else:
                wantDetailedEvent = False
        else:
            raise Exception("Something is missing in your json file, you cannot not use it")
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
            dayLogin += days_difference
            boolLogin = True
        else:
            raise Exception("Something is missing in your json file, you cannot not use it")
        if "PvP" in data:
            pvp = str(data['PvP'])
        else:
            raise Exception("Something is missing in your json file, you cannot not use it")
        
        boolScript = True


# Prompt the user for the initial value of the gem variable
gems = get_integer('How many gems do you have? : ')

# Prompt the user for the number of days to consider
daysOrDatePrompted = input(f'For how many days does it has to calculate?\nYou can also type a date in format: {today}: ')
daysOrDatePrompted = daysOrDatePrompted.strip()

if daysOrDatePrompted.isdigit():
    days = int(daysOrDatePrompted)
    print(f"It will calculate the number of gems earned in {days} days.")
    pass
else:
    # Try to parse the date
    try:
        daysOrDatePrompted = daysOrDatePrompted.replace("/", "-")
        daysOrDatePrompted = datetime.datetime.strptime(daysOrDatePrompted, "%Y-%m-%d")
        daysOrDatePrompted = daysOrDatePrompted.date()
        days = (daysOrDatePrompted - today).days
        print(f"It will calculate the number of gems earned in {days} days.")
        pass
    except ValueError:
        # The user didn't enter a valid date
        raise Exception("Invalid input. Please try again.")
if days < 0:
    raise Exception("Your input resulted in a negative number.")


# Prompt the user for which login reward are they at
while True:
    try:
        if not boolLogin:
            dayLogin = get_integer("Type which day you are on your login bonus (1 to 14): ")
        if 1 <= dayLogin <= 14:
            break
        else:
            print("The value cannot be lower than 1 and cannot be higher than 14.")
    except ValueError:
        print("Sorry, that was not a valid integer. Please try again.")
if dayLogin > 7:
    dayLogin -= 7
saveDayLogin = dayLogin
    

# Does user buy weekly and monthly + does user want detailed event?
if useFile:
    if not 'doWeeklyFile' in locals() and not 'doMonthlyFile' in locals():
        raise Exception("Issue with the inputs.json file")
    else:
        gemsWeeklyBundle += weeklyCalc(doWeeklyFile, days, dayRewardWeekly)
        gemsMonthlyBundle += monthlyCalc(doMonthlyFile, days, dayRewardMonthly)
    
else:
    doWeekly = isTrue(input('Do you want to purchase the weekly bundle? (y/n): '))
    if doWeekly:
        dayRewardWeekly = int(input('At what day reward are you (0 if not purchased, or 1 to 7): '))
        gemsWeeklyBundle += weeklyCalc(doWeekly, days, dayRewardWeekly)
    
    doMonthly = isTrue(input('Do you want to purchase the monthly bundle? (y/n): '))
    if doMonthly:
        dayRewardMonthly = int(input('At what day reward are you (0 if not purchased, or 1 to 28): '))
        gemsMonthlyBundle += monthlyCalc(doMonthly, days, dayRewardMonthly)
    pvp = rewardPvP()
    wantDetailedEvent = isTrue(input('Do you want a detailed list of the where the gems from the event were earned? (y/n): '))

print("\n",end="")
# Iterate over the number of days given
for i in range(days):
    # Calculate the date for the current day in the loop
    date = today + timedelta(days=i+1)
    # Check if the current date is a Monday
    if date.weekday() == 0:
        gemsPvP += int(options[pvp])
    if date.weekday() == 1:
        gemsMaintenance += 2
    if date.weekday() == 6:
        gemsDailies += 2
        
    dayLogin = dayLogin % 7 + 1
    if dayLogin == 2 or dayLogin == 6:
        gemsLogin += 5
        
    gemsKnighthood += 1
    gemsDailies += 4

gemsEventContentObtainedLastDay, gemsEventLoginObtainedLastDay = event()
gemsEvent += gemsEventContentObtainedLastDay
gemsEvent += sum(gemsEventLoginObtainedLastDay.values())
print(printWhatEarned(gemsWeeklyBundle, "gems from the Weekly Bundle"))
print(printWhatEarned(gemsMonthlyBundle, "gems from the Monthly Bundle"))
print(printWhatEarned(gemsPvP, "gems from the PvP reward"))
print(printWhatEarned(gemsLogin, "gems from base login reward"))
if not wantDetailedEvent: print(printWhatEarned(gemsEvent, "gems from the events currently available"))
print(printWhatEarned(gemsKnighthood, "gems from checking in your Knighthood"))
print(printWhatEarned(gemsDailies, "gems from doing your dailies every day"))
print(printWhatEarned(gemsMaintenance, "gems from the maintenance compensation"))
gems+= gemsWeeklyBundle + gemsMonthlyBundle + gemsPvP + gemsLogin + gemsEvent + gemsKnighthood + gemsDailies + gemsMaintenance
print(f'\nTotal gems will be: {gems}')

data = {
    "WantDetailedEvent": wantDetailedEvent,
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