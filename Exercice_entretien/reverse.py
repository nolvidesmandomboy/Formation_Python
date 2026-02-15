s = "Bonjour toto"
def reverse (variable):
    tab = []
    for i in range (1,len(variable)+1):
        tab.append(variable[-i])
        yes = "".join(tab)
    print(yes)

reverse (s)