#Øvelse 14
# Kør scriptet med: python Øvelse14.py DitNavn

# sys er et modul der hedder "system", en samling af funktioner Python har lavet til dig på forhånd
# argv er én bestemt funktion inde i modulet som vi henter ud - se Øvelse 13
from sys import argv

# argv er en argument vector, det er en liste over alt vi skriver i terminalen når vi starter scriptet
# når vi kører python Øvelse14.py DitNavn ser argv sådan ud: ['Øvelse14.py', 'DitNavn']
# med = fordeler vi 'Øvelse14.py' og 'DitNavn' ud i variablerne script og user_name
# script får 'Øvelse14.py' fordi det er det første element i listen og script er den første variabel
# user_name får 'DitNavn' fordi det er det andet element i listen og user_name er den anden variabel
script, user_name = argv

# prompt er en variabel. '> ' er en string der bliver sat ind i variablen med =
# vi gemmer '> ' i prompt så vi kun skal ændre det ét sted hvis vi vil ændre prompttegnet
prompt = '> '

# script er variablen med 'Øvelse14.py' og user_name er variablen med 'DitNavn' som vi fik fra argv ovenfor
# {script} og {user_name} i f-strengen viser indholdet af de to variabler på skærmen
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")

# prompt er variablen med '> ' som vi definerede ovenfor
# input() viser '> ' på skærmen og venter på at brugeren skriver noget og trykker Enter
# det brugeren skriver bliver sat ind i variablen likes med =
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# likes, lives og computer er variablerne vi satte brugerens svar ind i ovenfor med input()
# {likes}, {lives} og {computer} i f-strengen viser indholdet af de tre variabler på skærmen
# triple-quote """ bruges til at skrive tekst over flere linjer uden brug af \n - se Øvelse 9
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")