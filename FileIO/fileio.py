# jabber = open("/Users/henri/Documents/Python/FileIO/sample.txt", 'r')

# for line in jabber:
#     if "jabberwock" in line.lower():
# print(line, end="")  # Impede o print de gerar uma nova linha em branco

# jabber.close()

# with open("/Users/henri/Documents/Python/FileIO/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end="")

# with open("/Users/henri/Documents/Python/FileIO/sample.txt", 'r') as jabber:
#     line = jabber.readline()  # pega a primeirqa linha
#     while line:
#         print(line, end="")
# line = jabber.readline()  # passa para a próxima linha ao final do loop

# with open("/Users/henri/Documents/Python/FileIO/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)

# for line in lines:
#     print(line, end="")

# with open("/Users/henri/Documents/Python/FileIO/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)

# for line in lines:
#     print(line, end="")

# with open("/Users/henri/Documents/Python/FileIO/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)

# for line in lines[::-1]:
#     print(line, end="")

with open("/Users/henri/Documents/Python/FileIO/sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end="")
