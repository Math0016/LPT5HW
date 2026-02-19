#Øvelse 11

# print() er en indbygget Python funktion der viser tekst på skærmen
# end=' ' er et argument vi sender ind i print() der erstatter det automatiske linjeskift med et mellemrum
# så input() starter på samme linje som print() i stedet for på en ny linje
print("How old are you?", end=' ')

# input() er en indbygget Python funktion der stopper programmet og venter på at brugeren skriver noget og trykker Enter
# det brugeren skriver bliver sat ind i variablen age med =
age = input()

print("How tall are you?", end=' ')
height = input()

print("How much do you weigh?", end=' ')
weight = input()

# age, height og weight er variablerne vi satte brugerens svar ind i ovenfor med input()
# {age}, {height} og {weight} i f-strengen viser indholdet af de tre variabler på skærmen
# f-string betyder at Python erstatter {variabel} med variablens indhold
print(f"So, you're {age} old, {height} tall and {weight} heavy.")