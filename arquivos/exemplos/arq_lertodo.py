arq = open('nome_arquivo.txt','r',encoding='utf-8')
conteudo = arq.read() # Lê até o final do stream

print(conteudo)
arq.close()