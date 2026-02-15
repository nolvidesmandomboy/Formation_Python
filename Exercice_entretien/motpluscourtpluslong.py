s = "un chasseur sachant chasser sait chasser sans son chien"
p = "je m'appelle Nolvides Victorin et je suis Kinésithérapeute"

def get_min_and_max_words (sentense):
    sentense = sentense.split()
    motlepluslong = ""
    motlepluscourt = ""
    listtriee = [len(i) for i in sentense]
    nb_max = max(listtriee)
    nb_min = min(listtriee)
    for w in sentense :
        if len(w) == nb_max:
            motlepluslong = w
        if len(w) == nb_min:
            motlepluscourt = w
    return motlepluslong, motlepluscourt

maxword, min_word = get_min_and_max_words(s)
print ("mot le plus long : " + maxword)
print ("mot le plus court : " + min_word)