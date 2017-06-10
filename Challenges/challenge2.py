# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

# Entrada do IP a ser analisado
ipAddress = input("Please, enter you IP address: ")
if ipAddress[-1] != ".":
    ipAddress += "."

segment = 1  # variável para armazenar o número de segmentos
segment_lenght = 0  # E o comprimento de cada segmento
# character = ""

for character in ipAddress:
    if character == ".":
        print("Segment {} contains {} characters".format(segment, segment_lenght))
        segment += 1
        segment_lenght = 0
    else:
        segment_lenght += 1

# Para cada caracter ele busca por um ponto. Se achar, adiciona 1 em segment
# Se não achar, ele adiciona um em segment_lenght. Após acgar um ponto ele
# reinicia o loop.


# O loop termina antes que as últimas variáveis tenham sido impressas (caso o ip não termine com um ponto)
# por isso, aqui, imprimimos as últimas variáveis armazenadas.
# if character != ".":
#     print("Segment {} contains {} characters".format(segment, segment_lenght))
