import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', ':', ';', '<', '>', '.', ',', '?', '/', '+', '=', '"', '{', '}', '[', ']', ' ']

def caesar(direction, text_val, shift_amount):
  if(direction=="encode"):
    cipher_text = ""
    for letter in text_val:
      if((letter in numbers) or (letter in symbols)):
        cipher_text += letter
      else:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if(new_position > 25):
          difference = new_position - 25
          while(difference > 25):
            difference -= 26
          new_position = difference - 1
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
  else:
    plain_text = ""
    for letter in text_val:
      if((letter in numbers) or (letter in symbols)):
        cipher_text += letter
      else:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

print(art.logo)

cont = input("Would you like to use the program? Enter 'y' or 'n'. ")

while(cont == 'y'):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction, text, shift)
  cont = input("Would you like to use the program again? Enter 'y' or 'n'. ")



