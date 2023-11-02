import random

wining_list = random.sample(range(1, 49), 6)
list_of_numbers = []

for i in range(6):
    while True:
        player_picks = int(input('Enter 6 numbers: '))
        if 1 <= player_picks <= 49:
            if player_picks not in list_of_numbers:
                list_of_numbers.append(player_picks)
                break
            else:
                print('You already picked that number! Enter different number!')
        else:
            print('Wrong number pick number from 1-49')
list_of_numbers.sort()
wining_list.sort()
print(list_of_numbers)
print(wining_list)

matched = 0
for el_1 in list_of_numbers:
    for el_2 in wining_list:
        if el_1 == el_2:
            matched += 1
    if matched == 3:
        print("You guessed 3")
    elif matched == 4:
        print("You guessed 4")
    elif matched == 5:
        print("You guessed 5")
    elif matched == 6:
        print("You guessed 6")
else:
    print("We don't have any wining price for you today :(")