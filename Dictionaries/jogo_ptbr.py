# -*- coding: iso8859-1 -*-
import os
import sys
from random import randint

locais = {0: "Você está na frente do computador aprendendo Python.",
          1: "Você está parado no fim de uuma estrada, na frente de um prédio de tijolos.",
          2: "Você está no topo de uma colina.",
          3: "Você está dentro de um prédio.",
          4: "Você está em um vale, próximo a um rio.",
          5: "Você está numa floresta."}

saidas = {0: {"Q": 0},
          1: {"L": 2, "O": 3, "S": 4, "N": 5, "Q": 0},
          2: {"L": 1, "S": 4, "N": 5, "Q": 0},
          3: {"O": 1, "S": 4, "N": 5, "Q": 0},
          4: {"N": 1, "L": 3, "O": 2, "Q": 0},
          5: {"S": 1, "O": 2, "L": 3, "Q": 0}}

localiz = randint(1, 5)  # É preciso começar em algum lugar

while True:
    saidasDisponiveis = ", ".join(saidas[localiz])

    print(locais[localiz])
    print("Para onde deseja seguir?")
    saidaEscolhida = input(
        "Selecione uma das direções possíveis: " + saidasDisponiveis + ": ").upper()
    print()
    if saidaEscolhida == "Q":
        print(locais[0])
        break
    # se o valor escolhido existir na saida
    if saidaEscolhida in saidas[localiz]:
        # imprime a chave da localização escolhida vvvvv
        localiz = saidas[localiz][saidaEscolhida]
    else:
        print("Você não pode ir nessa direção!")
