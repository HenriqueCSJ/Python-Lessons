shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item == "spam":
#         print("I'm ignoring " + item)
#         continue #para de processar para este bloco de código e segue adianta
#     print("Buy " + item)


# for item in shopping_list:
#     if item == "spam":
# #        print("I'm ignoring " + item)
#         break #para de processar para este bloco de código e segue adianta
#     print("Buy " + item)

meal = ["eggs", "bacon", "spam", "sausages"]

nasty_food_item = ''

for item in meal:
    if item == "spam":
        print("Can't I have something without spam in it?")
        break
else:
    print("I'll have a plate of that, please.")

