#Øvelse 16
# Kør scriptet med: python Øvelse16.py test.txt

# sys er et modul der hedder "system", en samling af funktioner Python har lavet til dig på forhånd
# argv er én bestemt funktion inde i modulet som vi henter ud - se Øvelse 13
from sys import argv

# argv er en argument vector, det er en liste over alt vi skriver i terminalen når vi starter scriptet
# når vi kører python Øvelse16.py test.txt ser argv sådan ud: ['Øvelse16.py', 'test.txt']
# med = fordeler vi 'Øvelse16.py' og 'test.txt' ud i variablerne script og filename
# script får 'Øvelse16.py' fordi det er det første element i listen og script er den første variabel
# filename får 'test.txt' fordi det er det andet element i listen og filename er den anden variabel
script, filename = argv

# filename er variablen med 'test.txt' som vi fik fra argv ovenfor
# {filename} i f-strengen viser indholdet af filename på skærmen, altså teksten 'test.txt'
# ikke indholdet af filen — filen er ikke åbnet endnu, det sker først med open() nedenunder
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# input() er en indbygget Python funktion der stopper programmet og venter på at vi trykker Enter
# "?" er teksten der vises på skærmen inden vi trykker - se Øvelse 11
input("?")

# target er en variabel
# open() er en indbygget Python funktion der finder og åbner filen på computeren
# filename er variablen med 'test.txt' som vi fik fra argv ovenfor — det er den fil open() går ud og finder
# 'w' er en string som open() er programmeret til at genkende som write-mode
# write-mode betyder at Python opretter filen hvis den ikke findes, og sletter indholdet hvis den gør
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

# line1, line2 og line3 er tre variabler
# input() venter på at vi skriver noget i terminalen og sætter det vi skriver ind i variablen med =
# "Line 1: " er teksten der vises på skærmen inden vi skriver - se Øvelse 11
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

# target er filen vi åbnede ovenfor med open(filename, 'w')
# .write() er en indbygget Python metode der tilhører target og skriver det vi sender ind i parentesen til filen
# vi sender line1 ind — det er teksten vi skrev da input("Line 1: ") ventede på os
target.write(line1)
# .write("\n") skriver et linjeskift efter line1 fordi .write() ikke tilføjer det automatisk - se Øvelse 9/10
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")

# target er filen vi åbnede ovenfor
# .close() er en indbygget Python metode der lukker filen når vi er færdige - se Øvelse 15
target.close()

# result er en variabel
# open(filename) åbner 'test.txt' igen — denne gang uden 'w' så Python åbner den i read-mode som er standard
# result.read() læser hele indholdet af filen og print() viser det på skærmen
# så vi kan tjekke at det vi skrev med input() rent faktisk blev gemt i filen
result = open(filename)
print(result.read())
result.close()