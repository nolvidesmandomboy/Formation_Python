s = "un chasseur sachant chasser sait chasser sans son chien"
p = "je m'appelle Nolvides Victorin et je suis Kinésithérapeute"

def get_min_and_max_words (sentense):
    sentense = sentense.split()
    motlepluslong = sentense[0]
    motlepluscourt = sentense[0]
    listtriee = [len(i) for i in sentense]
    nb_max = max(listtriee)
    nb_min = print (min(listtriee))
    for w in sentense :
        if len(w) == nb_max:
            motlepluslong = w
        elif len(w) == nb_min:
            motlepluscourt = w
    print ("mot le plus long : " + motlepluslong)
    print ("mot le plus court : " + motlepluscourt)
    return motlepluslong, motlepluscourt

get_min_and_max_words(s)
get_min_and_max_words(p)