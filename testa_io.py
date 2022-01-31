arquivo = open('dados/contatos.csv', encoding='latin_1')

print(type(arquivo.buffer))

conteudo = arquivo.buffer.read()

print(conteudo)

texto_em_bytes = bytes('Este é um text em bytes', 'latin_1')
print(texto_em_bytes)
print(type(texto_em_bytes))

arquivo.close()
