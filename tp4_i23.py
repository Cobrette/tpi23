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
    l=[0]*lens(s)
    for i in range(0,len(s)):
        l[s[i]]=1
    return tuple(l)
   
#question 3:
def composer(s,t):
    p=[0]*len(s)
    if len(s)!=len(t):
        return('pas la meme longueur')
    elif not (EstPermutation(s) and EstPermutations(t)):
        return ('ce ne sont pas des permutations')
    else:
        i=0
        for e in t:
            p[s[i]]=e
            i+=1
    return Ecrire(s)

#question 4:
def orbite(k,s):
    k=k-1
    resultat=(k,)
    debut=k
    if not EstPermutation(s):
        print('pas de permutation')
    else:
        while s[k] != debut :
            resultat += (s[k],)
            k=s[k]
    return resultat


#question 5:
def Signature(s):
    pass    

#question 6:
def Cycles(s):
    pass
    
#question 7:
def Transposition(s):
    pass

#main
perm = lire()
Ecrire(perm)
permu=EstPermutation(perm)
print(permu)
print(composer(a,c))
print (Ecrire(orbite(1,lire())))
