alfabeto = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa "
chave = 899
mensagem = "HzrdszehqdzsnzcdzqZhm"

A = ''

for i in range(len(mensagem)):
    for j in range(len(alfabeto)):
        if alfabeto[j] == mensagem[i]:
            A += alfabeto[(j+chave)%len(alfabeto)]
            break
print(f'.{A}.')