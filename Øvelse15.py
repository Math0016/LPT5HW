#Øvelse 15
# Kør scriptet med: python Øvelse15.py ex15_sample.txt

# sys er et modul der hedder "system", en samling af funktioner Python har lavet til dig på forhånd
# argv er én bestemt funktion inde i modulet som vi henter ud - se Øvelse 13
from sys import argv

# argv er en argument vector, det er en liste over alt vi skriver i terminalen når vi starter scriptet
# når vi kører python Øvelse15.py ex15_sample.txt ser argv sådan ud: ['Øvelse15.py', 'ex15_sample.txt']
# med = fordeler vi 'Øvelse15.py' og 'ex15_sample.txt' ud i variablerne script og filename
# script får 'Øvelse15.py' fordi det er det første element i listen og script er den første variabel
# filename får 'ex15_sample.txt' fordi det er det andet element i listen og filename er den anden variabel
script, filename = argv

# txt er en variabel
# open() er en indbygget Python funktion der finder og åbner filen på computeren
# filename er variablen med 'ex15_sample.txt' som vi fik fra argv ovenfor — det er den fil open() går ud og finder
# 'ex15_sample.txt' er ikke selve filen, bare en string — det er først når vi skriver open(filename) at Python finder filen
# det der bliver sat ind i txt med = er adgangen til filen, ikke selve indholdet
txt = open(filename)

# filename er variablen med 'ex15_sample.txt' som vi fik fra argv ovenfor
# {filename} i f-strengen viser indholdet af filename på skærmen, altså teksten 'ex15_sample.txt'
print(f"Here's your file {filename}:")

# txt er filen vi åbnede ovenfor med open(filename)
# .read() er en indbygget Python metode der tilhører txt og læser hele indholdet af filen
# indholdet af 'ex15_sample.txt' f.eks. "This is stuff I typed into a file." bliver givet til print() som viser det på skærmen
print(txt.read())

print("Type the filename again:")

# input() er en indbygget Python funktion der stopper programmet og venter på at brugeren skriver noget og trykker Enter
# '> ' er teksten der vises på skærmen inden brugeren skriver
# det brugeren skriver bliver sat ind i variablen file_again med =
file_again = input("> ")

# file_again er variablen med det filnavn brugeren skrev ovenfor med input()
# open(file_again) finder og åbner den fil brugeren skrev ind
txt_again = open(file_again)
print(txt_again.read())

# txt og txt_again er de to filer vi åbnede ovenfor
# .close() er en indbygget Python metode der lukker filen når vi er færdige
# god vane så operativsystemet frigiver ressourcer
txt.close()
txt_again.close()