# Adicionar uma tabuada de 2 até 12 no arquivo sample.txt

with open("/Users/henri/Documents/Python/FileIO/sample.txt", 'a') as sample_file:
    for i in range(2, 13, 1):
        for j in range(0, 11, 1):
            print("{:>2} times {:<2} is {:<3}".format(i, j, i*j), file=sample_file)
        print("=" * 20, file=sample_file)
