arq = open('nome_arquivo.txt','r',encoding='utf-8')
linhas = arq.readlines()

for n, linha in enumerate(linhas):
    print(n+1, linha.strip())

arq.close()