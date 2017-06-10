from math import *

type_of_calculation = input(
    "Are tou calculating for an acidic or basic buffer [A|B]? ")
conc_acid = float(
    input("Type the concentration of your acidic species: (in M) "))
conc_base = float(
    input("Type the concentration of your basic species: (in M) "))

if type_of_calculation == "A":
    Ka = float(input("Type the Ka of your weak acid (Ex.: 1.8e-5): "))
else:
    Kb = float(input("Type the Kb of your weak base (Ex.: 1.8e-5): "))
    Ka = (1e-14) / Kb

Rate = conc_base / conc_acid
pKa = -log10(Ka)
pH = pKa + log10(Rate)

print("The pH is {0:4.3f}".format(pH))
