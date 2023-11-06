# xDy+z
# y – rodzaj kostek, których należy użyć (np. D6, D10),
# x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
# z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).
import random

def how_many_rolls(num_rolls: int, dice: str) -> list[int]:
    if num_rolls <= 0:
        raise ValueError('Number of rolls must be greater than 0')

    if not dice.startswith('D') or not dice[1:].isdigit():
        raise ValueError('Wrong type of dice. Use "Dn" format, where n is the number of the sides of the dice')

    num_sides = int(dice[1:])
    if num_sides < 4:
        raise ValueError('Number of sides must be at least 4')

    rolls: list[int] = []
    for i in range(num_rolls):
        random_roll: int = random.randint(1, num_sides)
        rolls.append(random_roll)
    return rolls

try:
    num_rolls = int(input("How many rolls? "))
    dice_type = input("What kind of dice? (e.g. D3, D4, D6, D8, D10, D12, D20, D100) ")
    result = how_many_rolls(num_rolls, dice_type)
    print(f'Throw result {dice_type}: {result}')
except ValueError:
    print("Error!")