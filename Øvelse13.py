#Øvelse 13
# Kør scriptet med: python Øvelse13.py first 2nd 3rd

# sys er et modul der hedder "system", en samling af funktioner Python har lavet til dig på forhånd
# argv er én bestemt funktion inde i modulet som vi henter ud
# from sys import argv betyder: gå ind i sys-modulet og hent kun argv ud, ikke hele modulet
from sys import argv

# argv er en argument vector, det er en liste over alt vi skriver i terminalen når vi starter scriptet
# når vi kører python Øvelse13.py first 2nd 3rd ser argv sådan ud: ['Øvelse13.py', 'first', '2nd', '3rd']
# med = fordeler vi 'Øvelse13.py', 'first', '2nd' og '3rd' ud i variablerne script, first, second og third
# script får 'Øvelse13.py' fordi det er det første element i listen og script er den første variabel
# first får 'first' fordi det er det andet element i listen og first er den anden variabel
# second får '2nd' fordi det er det tredje element i listen og second er den tredje variabel
# third får '3rd' fordi det er det fjerde element i listen og third er den fjerde variabel
# hvis vi giver færre eller flere argumenter i terminalen end der er variabler giver Python en ValueError
script, first, second, third = argv

# script er variablen med 'Øvelse13.py' som vi fik fra argv ovenfor
# {script} i f-strengen viser indholdet af script på skærmen
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)