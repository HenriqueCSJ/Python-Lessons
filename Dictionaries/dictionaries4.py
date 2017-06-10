atoms = {1: "Hydrogen",
         2: "Helium",
         3: "Lithium",
         4: "Berilium",
         5: "Boron",
         6: "Carbon",
         7: "Nitrogen",
         8: "Oxygen",
         9: "Fluorine",
         10: "Neon"}

orbitals = [{"1S": 1},
            {"1S": 2},
            {"1S": 2, "2S": 1},
            {"1S": 2, "2S": 2},
            {"1S": 2, "2S": 2, "2P": 1},
            {"1S": 2, "2S": 2, "2P": 2},
            {"1S": 2, "2S": 2, "2P": 3},
            {"1S": 2, "2S": 2, "2P": 4},
            {"1S": 2, "2S": 2, "2P": 5},
            {"1S": 2, "2S": 2, "2P": 6}]

startingAtom = int(input("Enter the initial atom: "))


while True:
    numberofElectrons = " + ".join(orbitals[startingAtom].keys())
    print(startingAtom)