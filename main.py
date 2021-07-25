alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo 
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(start_text,shift_amount,direc):
  end_text = ""  
  for char in start_text: 
    if char in alphabet: 
      position = alphabet.index(char) 
      print(f"{alphabet[position]} position {position}") 
      if direc == "decode":
        new_position = position - shift_amount
        if new_position < 0: 
          new_position = new_position%26
      else:
        new_position = position +shift_amount 
        if new_position > 25:
          new_position = new_position%26
        print(f"new position {new_position} {alphabet[new_position]}")
      end_text += alphabet[new_position]
    else:
      print("")
      print("******not in alphabet**********")
      print("")
      end_text += char
      print(f"end text {end_text}")
  print(end_text)
caesar(start_text=text,shift_amount = shift,direc=direction)
ask_again = input("restart the cipher game. yes or no: ").lower()
while ask_again == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text,shift_amount = shift,direc=direction)
  ask_again = input("restart the cipher game. yes or no: ").lower()
else:
  print("sad to see you leave. visit again!")