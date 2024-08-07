alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("encode or decode? ").lower()
text = input("message: ").lower()
shift = int(input("shift number: "))

def encrypt(original_text, shift_amount):
    encrypted = ''
    for letter in original_text:
        position = alphabet.index(letter) + shift_amount
        position %= len(alphabet)
        encrypted += alphabet[position]
    print(encrypted)

def decrypt(original_text, shift_amount):
    decrypted = ''
    for letter in original_text:
        position = alphabet.index(letter) - shift_amount
        position %= len(alphabet)
        decrypted += alphabet[position]
    print(decrypted)

def caesar(text, shift, direction):
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

caesar(text, shift, direction)