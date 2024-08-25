"""
Hoe werkt het algoritme stap voor stap?

Laten we het algoritme toepassen op het nummer dat je gaf: 7992739871.

1. Verwijder de laatste cijfer: Dit is het controlecijfer. In ons geval is dat 1.

2. Verdubbel de waarde van elk tweede cijfer beginnend van rechts:
7 9 9 2 7 3 9 8 7
7 18 9 4 7 6 9 16 7

3. Als een resultaat van stap 2 groter is dan 9, trek 9 af:
7 18 9 4 7 6 9 16 7
7 9 9 4 7 6 9 7 7

4. Tel alle cijfers bij elkaar op:
7 + 9 + 9 + 4 + 7 + 6 + 9 + 7 + 7 = 71

5. Bereken het modulo 10 van de som:
71 modulo 10 = 1

6. Vergelijk het resultaat met het verwijderde controlecijfer:
Het resultaat (1) is gelijk aan het verwijderde controlecijfer (1).

Conclusie:
Omdat het resultaat van de berekening overeenkomt met het controlecijfer, is het nummer 7992739871 volgens het Luhn-algoritme geldig.
"""


def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()