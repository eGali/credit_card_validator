import sys


def validate(numbers, com):
    big = []
    length = len(numbers)
    total = 0

    y = 2
    total = 0
    for t in range(0, length):
        if numbers[length - y] < 5:
            total += (numbers[length - y] * 2)
        elif numbers[length - y] >= 5:
            num = numbers[length - y] * 2
            while num:
                digit = num % 10
                big.append(digit)
                num /= 10
            total += (big[0] + big[1])
        del big[:]
        y += 2
        if y > length:
            break;

    ltotal = 0
    y = 1

    for t in range(2, length):
        ltotal += numbers[length - y]
        y += 2
        if y > length:
            break;

    numTotal = total + ltotal
    if numTotal%10 == 0:
        print('Your' , com, 'is valid!\n')
    else:
        print('Your', com, 'is not Valid!\n')

def validateType(card):
    
    if card[0] == 3 and card[1] == 7:
        com= 'Master Card'
        validate(card, com)
    elif card[0] == 4:
        com = 'Visa'
        validate(card, com)
    elif card[0] == 5:
        com = 'Master Card'
        validate(card, com)
    elif card[0] == 6:
        com = 'Discover'
        validate(card, com)
        
    else:
        print('Card Type Not Recognized\n')

def valide(card):
	numbers = [int(i) for i in str(card)]
	length = len(numbers)
	validateType(numbers) if length > 12 and length < 17 else print('Card not valide length!')


# beginning of main loop
x = 1

while x != 2:
    print('===Credit Card Validation===')
    print('1. Validate Number')
    print('2. Exit Program')
    print('============================')
    x = int(input('Menu Choice: '))
    
    if x == 1:
        card = int(input('\nEnter your credit card number: '))
        valide(card)
    print()
