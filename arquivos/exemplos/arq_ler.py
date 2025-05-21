# Abrimos o arquivo para leitura
# o modo de leitura é 'r' (reading)

arq = open('nome_arquivo.txt','r',encoding='utf-8')

caracteres = arq.read(4) # lê 4 caracteres do arquivo
uma_linha = arq.readline().strip()
outra_linha = arq.readline().strip()

print(f'caracteres lidos: {caracteres}')
print(f'linha lida: {uma_linha}')
print(f'linha lida: {outra_linha}')



arq.close()