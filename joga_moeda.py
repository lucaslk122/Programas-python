from random import random
def joga_moeda():
    if random() > 0.5:
        return "Coroa"
    else:
        return "Cara"
print (joga_moeda())