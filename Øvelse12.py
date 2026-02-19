#Øvelse 12
# Kortere måde at bruge input() på end Øvelse 11
# i stedet for at bruge print() med end=' ' og input() separat
# skriver vi prompt-teksten direkte ind i input() i parentesen

# "How old are you? " er en string vi sender ind i input() i parentesen
# input() viser strengen på skærmen og venter på at brugeren skriver noget og trykker Enter
# det brugeren skriver bliver sat ind i variablen age med =
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

# age, height og weight er variablerne vi satte brugerens svar ind i ovenfor med input()
# {age}, {height} og {weight} i f-strengen viser indholdet af de tre variabler på skærmen
# f-string betyder at Python erstatter {variabel} med variablens indhold
print(f"So, you're {age} old, {height} tall and {weight} heavy.")