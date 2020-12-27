alphabet = "zyxwvutsrqponmlkjihgfedcba"
key = 3
message = "hqcrjdeulho"

A = ''

for i in range(len(message)):
    for j in range(len(alphabet)):
        if alphabet[j] == message[i]:
            A += alphabet[(j+key)%len(alphabet)]
            break
print(f'.{A}.')