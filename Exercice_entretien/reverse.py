s = "Bonjour toto"
a = "Nolvides"
def reverse (variable):
    tab = []
    for i in range (1,len(variable)+1):
        tab.append(variable[-i])
        valeurinversee = "".join(tab)
    print (valeurinversee)
    return valeurinversee

reverse (s)
reverse(a)

# Autre manière de faire :
print (s[::-1])