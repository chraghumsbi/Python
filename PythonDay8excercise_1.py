# Ciper game, Decode and encode messages

from cipher_art import logo
print(logo)

# def encrypt(plan_text, shift_amount):
#     ciper_text = ''
#     for letter in plan_text:
#         position = alphabet.index(letter)
#         new_position = position+shift_amount
#         new_letter = alphabet[new_position]
#         ciper_text += new_letter
#     print(f' the encoded text is {ciper_text}')


# def decrpt(cipher_text, shift_amount):
#     plan_text = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position-shift_amount
#         plan_text += alphabet[new_position]
#     print(f' The decode text is {plan_text}')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# if direction in ('Encode', 'Decode'):
#     # text = input('Type your message: \n').lower()
#     # shift = int(input('Type the shift number: \n'))
#     if direction == 'Encode':
#         encrypt(plan_text=text, shift_amount=shift)
#     elif direction == 'Decode':
#         decrpt(cipher_text=text, shift_amount=shift)
# else:
#     print('Plesae select correct code type')


# new way to do above code

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f' The {cipher_direction} text is {end_text}')


should_continue = True
while should_continue:
    direction = input(
        " Type 'Enccode' to encrypt, Type 'Decode' to decrypt: \n").lower()
    text = input('Type your message: \n').lower()
    shift = int(input('Type the shift number: \n'))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input(
        "Type 'yes' if you want to continue again. Otherwise type 'No'. \n")
    if result == 'no':
        should_continue = False
        print('Good bye!')
