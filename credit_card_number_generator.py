from random import randint

cc_number = []
multiplied_by_two = []
remaining_numbers = []
new_number = ''

# Ask for a first 15 digits of a card
starting_15 = input('Enter first 15 digits: ')

# Generate 10 numbers.
z = 0
y = 0

while z < 25:
    for i in str(starting_15):
        cc_number.append(int(i))
    
    # extract all the numbers that have to be multiplied by 2
    for i in cc_number[0:16:2]:
        i *= 2
        if len(str(i)) == 2:        # check if the multiplied number is a two digit number
            for x in str(i):        # if it is, separate them, and add them together
                y += int(str(x))
            i = y
        multiplied_by_two.append(i)
        y = 0

    for i in cc_number[1:15:2]:     # extract remaining numbers
        remaining_numbers.append(i)

    # Luhn's algorithm
    last_digit = ((sum(multiplied_by_two) + sum(remaining_numbers)) * 9) % 10

    for i in cc_number:
        new_number += str(i)

    print(new_number + str(last_digit))
    cc_number = []
    multiplied_by_two = []
    remaining_numbers = []
    new_number = ''

    starting_15 = int(starting_15) + randint(-15, 25)
    z += 1
