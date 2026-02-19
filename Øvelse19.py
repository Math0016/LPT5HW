#Øvelse 19

# def betyder vi laver en funktion. cheese_and_crackers er navnet vi selv har valgt
# i parentesen (cheese_count, boxes_of_crackers) definerer vi to argumenter
# cheese_count på første plads og boxes_of_crackers på anden plads
# når vi kalder funktionen skal vi sende to værdier ind i parentesen og de får disse navne inde i funktionen
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # de fire print() linjer kører automatisk når funktionen kaldes
    # {cheese_count} og {boxes_of_crackers} i f-strengene bliver erstattet med de værdier vi sender ind - se Øvelse 5/6
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")  # \n laver en tom linje efter teksten - se Øvelse 9/10

print("We can just give the function numbers directly:")
# 20 går ind som cheese_count og 30 går ind som boxes_of_crackers
# fordi de står på samme pladser i parentesen som da vi definerede funktionen med def
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# 10 bliver sat ind i variablen amount_of_cheese og 50 i amount_of_crackers - se Øvelse 4
amount_of_cheese = 10
amount_of_crackers = 50
# det samme som at skrive cheese_and_crackers(10, 50)
# Python henter bare værdierne ud af variablerne
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# Python udregner 10 + 20 til 30 og 5 + 6 til 11 før den sender dem ind i funktionen
# det samme som at skrive cheese_and_crackers(30, 11) - se Øvelse 3
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# Python henter amount_of_cheese som er 10 og lægger 100 til
# og henter amount_of_crackers som er 50 og lægger 1000 til
# det samme som at skrive cheese_and_crackers(110, 1050)
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)