#Øvelse 8

# Variable med fire tomme placeholders {} {} {} {}
formatter = "{} {} {} {}"

# Genbruger de tomme placeholders
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# Output: {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
# fordi vi printer selve variablen 'formatter', som kun indeholder "{} {} {} {}".
# Der bliver derfor ikke indsat værdier i placeholders, vi udskriver bare selve skabelonen.
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
print(formatter.format(
    "Der er et yndigt land",
    "Det står med brede bøge",
    "Nær salten østerstrand, nær salten østerstrand",
    "Det bugter sig i bakke, dal Det hedder gamle Danmark"
))