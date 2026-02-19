#Øvelse 6
# F-strings (formatted string literals) gør koden mere læsbar og hurtigere at skrive # end den ældre .format()-metode.
# Med f-strings kan man lave string interpolation, dvs. indsætte variabler, # udtryk og funktioner direkte i strengen.
types_of_people = 10

x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# .format() var brugt i ældre version af python men bliver stasdig brugt
# Her sætter vi en variable "hilarious" som er lig med False i den tomme placeholder {} som bliver printed som "Isn't that joke so funny?! False"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)