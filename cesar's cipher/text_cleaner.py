
text = open('text.txt').read().strip()

A = ''

for i in range(len(text)):
    if text[i] not in '-., ':
        A += text[i]

text = open('text.txt','w')
text.write(A)
text.close()