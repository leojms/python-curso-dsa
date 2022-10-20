dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

def trocar_valores(d1, d2):
    dicio={}
    for d1key, d2val in zip(d1, d2.values()):
        dicio[d1key]=d2val

    return dicio

print(trocar_valores(dict1, dict2))