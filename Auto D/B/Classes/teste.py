caracteres_invalidos = '\/:*?"<>|'
texto = 'a\c/df:g*h?jdf"<j>jd|kj'
print(caracteres_invalidos)

for caractere in range(0, len(caracteres_invalidos), 1):
    # print(caractere)
    caracteres_corrigidos = texto.replace(caracteres_invalidos[caractere], "")

print(caracteres_corrigidos)
