l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [x for x in "Leonardo"]
l4 = [x for x in "Acarajé"]

t1= zip(l1, l2)
t2= zip(l3, l4)

print(list(t1))
print(list(t2))

d1={"a":1, "b":2}
d2={"c":3, "d":4}

print(list(zip(d1, d2)))
print(list(zip(d1, d2.values())))

def trocar_valores(d1, d2):
    dicio={}
    for d1key, d2val in zip(d1, d2.values()):
        dicio[d1key]=d2val

    return dicio

print(trocar_valores(d1,d2))