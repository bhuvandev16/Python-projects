def validate_card_number(card_number):
    card_number = card_number.replace('-', "").replace(' ', '')
    
    if not card_number.isdigit():
        return False

    card_number = card_number[::-1]
    
    sum_odd_digits = 0
    sum_even_digits = 0

    for i in card_number[::2]:
        sum_odd_digits += int(i)

    for x in card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even_digits += (x % 10) + 1
        else:
            sum_even_digits += x

    total = sum_odd_digits + sum_even_digits

    return total % 10 == 0

card_number = input("Enter a credit card number: ")
if validate_card_number(card_number):
    print("Valid")
else:
    print("Invalid")
