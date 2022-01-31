arquivos_contato = open('dados/contatos_escrita.csv', encoding='latin_1', mode = 'a+')

contatos = ['11, Carol, carol@carol.com.br\n',
            '12, Ana, ana@ana.com.br\n',
            '13, Tais, tais@tais.com.br\n',
            '14, felipe, felipe@felipe.com.br\n',
            ]
for contato in contatos:
    arquivos_contato.write(contato)
arquivos_contato.flush()
arquivos_contato.seek(28)
arquivos_contato.write('12, Ana, ana@ana.com.br\n'.upper())
arquivos_contato.flush()
arquivos_contato.seek(0)

for linha in arquivos_contato:
    print(linha,end='')
