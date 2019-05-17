print("Hi, I'm a software that only says 'Hello!'.")

times_to_say = int(input("How many times do you want me to say 'Hello!'?: "))
my_range = list(range(0, times_to_say))

print("OK, I'll say 'Hello!' {} times".format(times_to_say))
print("There we go!")

for i in my_range:
    print("Hello!")
