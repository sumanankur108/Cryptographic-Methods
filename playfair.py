import string
def createKeyTable(key):
    keyTable = []
    for char in key.upper():
        if char not in keyTable and char != 'J':
            keyTable.append(char)
    for char in string.ascii_uppercase:
        if char not in keyTable and char != 'J':
            keyTable.append(char)
    return keyTable

def encode_key(plaintext, key):
    keyTable = createKeyTable(key)
    plaintext = plaintext.replace('J', 'I')
    plaintext = plaintext.upper()
    cipherText = ''
    for i in range(0, len(plaintext)-1, 2):
        p1, p2 = plaintext[i], plaintext[i+1]
        if p1 == p2:
            cipherText += p1 + 'Z'
        else:
            r1, c1 = divmod(keyTable.index(p1), 5)
            r2, c2 = divmod(keyTable.index(p2), 5)
            if r1 == r2:
                cipherText += keyTable[r1*5 + (c1+1)%5] + keyTable[r2*5 + (c2+1)%5]
            elif c1 == c2:
                cipherText += keyTable[((r1+1)%5)*5 + c1] + keyTable[((r2+1)%5)*5 + c2]
            else:
                cipherText += keyTable[r1*5 + c2] + keyTable[r2*5 + c1]
    if len(plaintext) % 2 == 1:
        cipherText += plaintext[-1]
    return cipherText

def decode_key(ciphertext, key):
    keyTable = createKeyTable(key)
    plaintext = ''
    for i in range(0, len(ciphertext)-1, 2):
        c1, c2 = ciphertext[i], ciphertext[i+1]
        if c1 == c2:
            plaintext += c1
        else:
            r1, c1 = divmod(keyTable.index(c1), 5)
            r2, c2 = divmod(keyTable.index(c2), 5)
            if r1 == r2:
                plaintext += keyTable[r1*5 + (c1-1)%5] + keyTable[r2*5 + (c2-1)%5]
            elif c1 == c2:
                plaintext += keyTable[((r1-1)%5)*5 + c1] + keyTable[((r2-1)%5)*5 + c2]
            else:
                plaintext += keyTable[r1*5 + c2] + keyTable[r2*5 + c1]
    if len(ciphertext) % 2 == 1:
        plaintext += ciphertext[-1]
    return plaintext

def createKeyTable(key):

  keyTable = []

  # Build
  for char in key.upper():
    if char not in keyTable and char != 'J':
      keyTable.append(char)

  for char in string.ascii_uppercase:
    if char not in keyTable and char != 'J':
      keyTable.append(char)

  return keyTable

# Name: Ankur Suman
# Registration Number: 21BDS0097
print("Ankur Suman")
print("Registration Number: 21BDS0097")
print("Enter keyword: ")
new_key = input()

print("Enter message to encrypt: ")
plaintext = input()

kTable = createKeyTable(new_key)
# Print the key table grid
print("Key Table:")
for i in range(5):
 print(kTable[i*5 : (i+1)*5])

print("Encrypting. ..")
ciphertext = encode_key(plaintext, new_key)
print("The encrypted text is:", ciphertext)

print("Decrypting. ..")
decrypted = decode_key(ciphertext, new_key)
print("The encrypted text is:", decrypted)