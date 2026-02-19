#Øvelse 17
# Husk at oprette test.txt i samme mappe før du kører scriptet
# Scriptet kopierer indholdet fra test.txt over i new_test.txt

# sys er et modul der hedder "system", en samling af funktioner Python har lavet til dig på forhånd
# argv er én bestemt funktion inde i modulet som vi henter ud - se Øvelse 13
from sys import argv

# os er et modul der hedder "operating system" og giver adgang til computerens filsystem
# path er en samling af funktioner inde i os der arbejder med filstier
# exists er én bestemt funktion inde i path som vi henter ud
# exists() tjekker om en fil eksisterer på computeren og returnerer True eller False
from os.path import exists

# from_file er en variabel. "test.txt" er en string der bliver sat ind i variablen med =
# strengen er ikke selve filen, bare tekst - det er først når vi skriver open(from_file) nedenunder at Python finder filen
from_file = "test.txt"
# to_file er en variabel. "new_test.txt" er strengen der bliver sat ind i variablen med =
to_file = "new_test.txt"

# f-string der viser hvad from_file og to_file indeholder - se Øvelse 5/6
print(f"Copying from {from_file} to {to_file}")

# in_file er en variabel. open() er en indbygget funktion der finder og åbner filen på computeren
# from_file er variablen med strengen "test.txt" som vi definerede ovenfor
# det der bliver sat ind i in_file med = er adgangen til filen, ikke selve indholdet - se Øvelse 15
in_file = open(from_file)

# indata er en variabel
# in_file er filen vi åbnede ovenfor
# .read() er en indbygget Python metode der tilhører in_file og læser hele indholdet af filen som er test.text
# al teksten fra "test.txt" bliver læst og sat ind i indata med =
indata = in_file.read()

# indata indeholder al teksten fra "test.txt" som vi læste med .read() ovenfor
# "test.txt" er en fil der ligger på computeren med noget tekst i, f.eks. "This is stuff I typed into a file."
# len() er en indbygget Python funktion der tæller antallet af tegn i indata og giver det tilbage som et tal
# det tal vises i f-strengen der hvor {len(indata)} står
print(f"The input file is {len(indata)} bytes long")

# exists() er funktionen vi hentede fra os.path øverst i koden
# to_file er variablen med strengen "new_test.txt" som vi definerede ovenfor
# vi sender to_file ind i parentesen i exists(to_file) og den tjekker om "new_test.txt" allerede findes på computeren
# exists() giver True eller False tilbage og det vises i f-strengen der hvor {exists(to_file)} står
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")

# input() stopper programmet og venter på at vi trykker Enter - se Øvelse 11
input()

# out_file er en variabel
# open() åbner filen "new_test.txt" som er gemt i to_file
# 'w' er write-mode som betyder at Python opretter filen hvis den ikke findes - se Øvelse 16
out_file = open(to_file, 'w')

# out_file er filen vi åbnede ovenfor
# .write() er en indbygget Python metode der tilhører out_file og skriver det vi sender ind i parentesen til filen
# vi sender indata ind som er al teksten fra "test.txt" som vi læste tidligere
# så vi kopierer altså teksten fra "test.txt" ind i "new_test.txt"
out_file.write(indata)

print("Alright, all done.")

# out_file og in_file er de to filer vi åbnede tidligere
# .close() er en indbygget Python metode der lukker filen når vi er færdige - se Øvelse 15
out_file.close()
in_file.close()