import json

f = open('data.json')

data = json.load(f)

aux = 0
maior = 0
menor = 0
soma = 0
media = 0


for dia in data:
    if (dia['valor']) != 0:
        aux = dia['valor']

        if (aux > maior):
            maior = aux

        if(menor == 0):
            menor = aux
        elif (aux < menor):
            menor = aux

        soma += dia['valor']

print('O maior valor do faturamento do mês foi: R$ ' + str(maior) + '.')
print('O menor valor do faturamento do mês foi: R$ ' + str(menor) + '.')

media = soma / len(data)

diasFaturamento = ''

for i in data:
    if (i['valor']) != 0:

        if (i['valor']) > media:
           diasFaturamento += (str(i['dia']) + ' ')
        
print('Os dias em que o faturamento foi maior que a média mensal foram: ' + diasFaturamento)