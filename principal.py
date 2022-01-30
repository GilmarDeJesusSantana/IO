arquivo_contato = open('dados/contatos.csv', encoding='latin_1')

conteudo = arquivo_contato.readlines()

print(conteudo, end= '')

# for linha in arquivo_contato:
#     print(linha, end='')
