locations = {0: "You're sitting in front of the computer learning Python.",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside of a building, a well house for a small stream.",
             4: "You are in a valley beside a stream.",
             5: "You are in the forest."}

exits = [{"Q", 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1  # começa na posição 1
while True:  # Loop infinito

    # Abaixo o jeito ineficiente: variável availableExits vazia
    # "diretion" é populado com valores de "exits" iniciando na posição 1
    #    # e pega os valores das chaves (na posição 1 de começo)  (WENSQ)
    # availableExits += concatena os valores (WENSQ), separando-os por ,

    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    availableExits = ", ".join(exits[loc].keys())  # Concatena os valores WENSQ
    print(locations[loc])  # imprime o valor do dicionário (não a chave)

    if (loc == 0):  # loc 0 para o jogo
        break

    direction = input("Available exits are: " +
                      availableExits.upper() + " ")  # exibe as direções salvas em availableExits
    # e lê uma entrada de teclado, armazenando-a em maiúscula
    print()  # linha em branco

    # Se a direção selecionada existir nas localizações disponibilizadas
    # anteriormente...
    if direction in exits[loc]:
        # Na entrada loc (1 no começo) a Direção WENSQ corresponde a qual valor
        # no dicionário? Este valor será salvo em loc (é um tipo de corrdenada
        # XY). Exemplo. em EXITS na posição 1 a chave W tem o valor 2. Esse
        # valor será salvo em loc.
        loc = exits[loc][direction]
    else:
        print("You can not go in that direction!")
