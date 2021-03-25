def lire():
    chaine=input("Permutation=")
    return tuple ([int(x)-1 for x in chaine.split()])

def Ecrire(s):
    for i in s:
        print(i+1,end='')
    print()

#question 1:
def EstPermutation(s):
    cool = sum(1 if c in range(len(s)) else 0 for c in s) == len(s)
    fun = sum(1 if s[i] == i else 0 for i in range(len(s))) == 2
    return cool and fun

#question 2:
def Inverser(s):

#main
perm = lire()
Ecrire(perm)
permu=EstPermutation(perm)
print(permu)
