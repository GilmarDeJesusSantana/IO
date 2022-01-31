try:
    arquivo_contato = open('dados/contatos.csv', encoding='latin_1')

    conteudo = arquivo_contato.readlines()

    for linha in arquivo_contato:
        print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado.')
except PermissionError:
    print('Sem permissão de escrita.')
finally:
    arquivo_contato.close()