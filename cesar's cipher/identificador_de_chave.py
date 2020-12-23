message = 'enzo gabriel'
new_message = ''

letter_percent=[]

for i in range(len(message)):
    letter_score = 0

    if message[i]  not in new_message or message[i] != ' ':

        for j in range(len(message)):
            if message[i] == message[j]:
                letter_score += 1
                new_message += message[i]
        letter_percent.append([message[i],f'{(letter_score/len(message)):.2f}'])

print(letter_percent)