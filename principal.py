arquivo_contato = open('dados/contatos.csv', encoding='latin_1')

conteudo = arquivo_contato.readlines()

for linha in conteudo:
    print(linha, end= '')

# for linha in arquivo_contato:
#     print(linha, end='')
