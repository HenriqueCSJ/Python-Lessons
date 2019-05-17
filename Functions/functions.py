def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=" "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("/Users/henri/Documents/Python/Functions/centered", mode="w")
# as centered_file:

# Call the function
with open("/Users/henri/Documents/Python/Functions/menu", mode="w") as menu:
    s1 = center_text("Spam and eggs")
    print(s1, file=menu)
    s2 = center_text("Spam, spam and eggs")
    print(s2, file=menu)
    print(center_text("Spam, spam, spam and spam"), file=menu)
    print(center_text(12), file=menu)
    s5 = center_text("Center", "3", 4, "arg", sep="--")
    print(s5, file=menu)
