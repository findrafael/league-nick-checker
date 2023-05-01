import requests
import time

CHAVE_DEVELOPER = 'DEVELOPER KEY HERE'

with open('nicks.txt', 'r') as arquivo:
    linhas = arquivo.readlines()


array = []

for linha in linhas:
    array.append(linha.strip())


print('***')
print('')

cont = 0

for elemento in array:
    url = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + elemento + '?api_key=' + CHAVE_DEVELOPER
    response = requests.get(url)

    if response.status_code == 200:
        # Sucesso na requisição
        print(elemento + ' -> CONTA JÁ EXISTE')
    else:
        # Erro na requisição
        print(elemento + ' -> CONTA LIVRE')
    
    cont = cont + 1

    if cont == 10:
        time.sleep(2)


print('')
print('***')
