fisrtName = 'James'
lastName = 'Bond'
Version = 7

fullName = fisrtName + ' ' + lastName + ' ' + str(Version)
print(fullName)

lenghtOfName = len(lastName)
print(lenghtOfName)
print(lastName[2])
# ------------------------- print(lastName[4]) ------------------len(string)-1 is the max

name = "Mußtermann"
print("Hallo Herr " + name[0] + "********" + name[len(name) - 1])

rico = name.casefold() #aggressively turns letters to lower case including ß
print(rico)

gag = rico.center(19, '-')
print(gag)