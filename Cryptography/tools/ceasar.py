# Loop through all possiblities of Ceasar
alphabet= 'abcdefghijklmnopqrstuvwxyz'
ciphertext =  input("Enter the ciphertext to decrypt: ")

for shift in range(26):
        result =''
        for char in ciphertext:
                if (char.lower() not in alphabet):
                        result += char
                        continue
                idx= (alphabet.index(char.lower())- shift) % 26
                result += alphabet [idx]
        print(f"Shift {shift}: {result}")
