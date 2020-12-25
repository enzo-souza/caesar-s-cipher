message = 'enzo gabriel'
new_message = ''

letter_percent=[]  

for i in range(len(message)): #calculation of the percentage of the message's letters
    letter_score = 0

    if message[i]  not in new_message and message[i] != ' ':
    
        for j in range(len(message)):
            if message[i] == message[j]:
                letter_score += 1
                if message[i] not in new_message:
                    new_message += message[i]
                
        letter_percent.append([message[i],f'{(letter_score/len(message)):.2f}']) #put in a list (letter_percent) the percent of each letter in the messege
        print(new_message,'--',message[i])
print(letter_percent)

