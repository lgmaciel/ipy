"""
 Para criar um arquivo
 usamos a função open()
 por padrão, são arquivos modo texto
 a função open() retorna um objeto
 que representa o arquivo aberto
 através desse objeto nós poderemos
 manipular o arquivo (ler, gravar, pesquisar, etc...)
"""
arq = open('nome_arquivo.txt','w') 

"""
arq representa o arquivo 'nome_arquivo.txt'
Sempre devemos fechar o arquivo após abrí-lo
o método close() fecha o arquivo
"""
arq.close()

# Fechar o arquivo libera ele para ser usado por outros programas

