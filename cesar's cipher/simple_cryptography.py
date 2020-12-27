alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
key = 3
message = open('texto.txt').read().strip()

A = ''

for i in range(len(message)):
    if message[i] != ' ' :
        for j in range(len(alphabet)):
            if alphabet[j] == message[i]:
                A += alphabet[(j+key)%len(alphabet)]
                break

folder = open('encryptophyed_text.txt','w') #criate a file with the encryptophyed message
folder.write(A)
folder.close()

print(f'.{A}.')