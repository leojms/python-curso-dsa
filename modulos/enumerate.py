l1 = [x for x in "abc"]
print(list(enumerate(l1)))

print("\n")

for i,val in enumerate(l1):
    print(i, val)

print("\n")

for i,val in enumerate(l1):
    if(i>=2):
        break
    else:
        print(val)

print("\n")

l2 = "Banana, Maçã, Pêra".split(", ")

for i, val in enumerate(l2):
    print(i, val)

print("\n")

for i, val in enumerate("Não tenho criatividade"):
    print(i, val)