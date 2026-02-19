#Øvelse 20
# Husk at oprette ex20_test.txt i samme mappe før du kører scriptet

# sys er et modul der hedder "system", en samling af funktioner Python har lavet til dig på forhånd
# argv er én bestemt funktion inde i modulet som vi henter ud
# from sys import argv betyder: gå ind i sys-modulet og hent kun argv ud, ikke hele modulet
from sys import argv

# input_file er en variabel. "ex20_test.txt" er en string der bliver sat ind i variablen med =
# strengen er ikke selve filen, det er bare tekst ligesom "hej"
# det er først når vi skriver open(input_file) længere nede at Python faktisk finder filen på computeren
input_file = "ex20_test.txt"

# def betyder vi laver en funktion. print_all er navnet vi selv har valgt
# f er argumentet vi skriver i parentesen i def print_all(f)
# når vi kalder print_all(current_file) senere i koden går current_file ind i parentesen og får navnet f inde i funktionen
# da current_file er en fil vi åbnede med open(), bliver f til den fil
# f.read() læser hele filens indhold og giver det videre til print() som viser det på skærmen
def print_all(f):
    print(f.read())

# rewind er et navn vi selv har valgt
# f i parentesen er et argument ligesom i def print_all(f) ovenfor
# seek(0) er en indbygget metode der nulstiller Pythons position i filen til starten
# vi har brug for det fordi efter print_all() har læst hele filen er Python nået til slutningen
# og ville ikke finde noget hvis vi prøvede at læse igen
def rewind(f):
    f.seek(0)

# print_a_line er et navn vi selv har valgt
# i parentesen (line_count, f) definerer vi to argumenter, line_count på første plads og f på anden plads
# når vi kalder print_a_line(current_line, current_file) senere går current_line ind som line_count
# og current_file ind som f fordi de står på samme pladser i parentesen
# readline() er forskellig fra read() fordi den kun læser én linje og stopper
# næste gang vi kalder readline() fortsætter den fra hvor den slap
def print_a_line(line_count, f):
    print(line_count, f.readline())

# current_file er en variabel. open() er en indbygget funktion der finder og åbner filen på computeren
# input_file er variablen vi definerede øverst med filnavnet "ex20_test.txt"
# alt efter = bliver sat ind i variablen current_file
current_file = open(input_file)

print("First let's print the whole file:\n")

# kalder print_all() funktionen og sender current_file ind i parentesen som argumentet f
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# kalder rewind() funktionen og sender current_file ind så seek(0) kan nulstille positionen
rewind(current_file)

print("Let's print three lines:")

# 1 bliver med = sat ind i variablen current_line
current_line = 1

# kalder print_a_line() og sender current_line ind som line_count og current_file ind som f
print_a_line(current_line, current_file)

# += er en genvej for current_line = current_line + 1, så current_line går fra 1 til 2
current_line += 1
# gentager kaldet, men nu er current_line lig med 2 så print_a_line() printer linje 2
print_a_line(current_line, current_file)

# current_line går fra 2 til 3
current_line += 1
# gentager kaldet, nu er current_line lig med 3 så print_a_line() printer linje 3
print_a_line(current_line, current_file)

# lukker filen når vi er færdige - se Øvelse 15
current_file.close()