#Øvelse 18
# Denne øvelse viser fire funktioner der alle gør næsten det samme men på forskellig måde
# fra den mest komplicerede print_two til den simpleste print_none
# det er med vilje så du kan se forskellen

# def betyder vi laver en funktion. print_two er navnet vi selv har valgt
# *args i parentesen i def print_two(*args) er det der fanger alle værdier vi sender ind
# når vi kalder print_two("Zed", "Shaw") længere nede i koden
# fanger *args begge værdier "Zed" og "Shaw"
# arg1, arg2 = args fordeler dem ud:
#   arg1, arg2 = args
#   ^      ^      ^
#   |      |      args er listen med alle værdier der blev fanget af *args
#   |      Shaw --+
#   Zed ---------+
# så arg1 er "Zed" og arg2 er "Shaw" når vi når til print()
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")  # f-string - se Øvelse 5/6

# print_two_again gør præcis det samme som print_two ovenfor men på en kortere måde
# i stedet for *args der fanger værdierne og arg1, arg2 = args der fordeler dem ud
# navngiver vi argumenterne direkte i parentesen (arg1, arg2)
# når vi kalder print_two_again("Zed", "Shaw") længere nede i koden
# går "Zed" direkte ind i arg1 og "Shaw" direkte ind i arg2
# fordi de står på samme pladser i parentesen
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# print_one er samme idé som print_two_again ovenfor
# men parentesen (arg1) har kun ét argument i stedet for to
# når vi kalder print_one("First!") længere nede i koden går "First!" direkte ind i arg1
def print_one(arg1):
    print(f"arg1: {arg1}")

# print_none er samme idé igen men parentesen () er helt tom
# funktionen tager ingen argumenter ind overhovedet
# når vi kalder print_none() sender vi ingenting ind og funktionen kører bare print() direkte
def print_none():
    print("I got nothin'.")

# her kalder vi alle fire funktioner
# de tre første sender vi værdier ind i parentesen
# print_none() kalder vi med tom parentes fordi den ikke tager nogen argumenter ind
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()