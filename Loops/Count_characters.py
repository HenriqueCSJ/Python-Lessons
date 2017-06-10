print("Olá, vamos analisar algumas coisas sobre parágrafos que você deve escrever")
paragrafo = input("Por favor, digite agora seu parágrafo e digite ENTER ao final: ")

if paragrafo == "":
    print("Você não digitou um parágrafo")
else:
    if paragrafo[-1] != ".":
        paragrafo += "."


sentencas = 0
virgulas = 0
caracteres = ""

for caracteres in paragrafo:
    if caracteres == ".":
        sentencas += 1
    else:
        if caracteres == ",":
            virgulas += 1

tamanho_das_sentencas = len(paragrafo)
print("Este texto tem {} sentenças com {} vírgulas e um total de {} caracteres.".format(sentencas, virgulas, tamanho_das_sentencas))

