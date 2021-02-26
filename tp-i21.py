from random import*
#bibliothéque pour la fonction random python
lettres='abcdefghijklmnopqrstuvwxyz'
parenthèses='(,)'
symboles='!,+,*'
#question n°1
def ListerVariables(expression):
    l=[]
    for char in expression :
        if char in lettres and not char in l :
          l.append(char)
    return sorted(l)
#question n°2
def DicoVariables(liste):
    i=0
    dico={}
    while i<len(liste):
        dico[liste[i]]=i
        i=i+1
    return dico
#question n°3
def Int2Bin(entier,n):
    binaire=bin(entier)[2:]
    while len(binaire)< n :
        binaire='0'+binaire
    return binaire
#question n°4
def Bin2Bool(bits):
    rep=[]
    i=0
    while i<len(bits):
        if bits[i]=='1' :
            rep=rep + [True]
        elif bits[i]=='0' :
            rep=rep + [False]
        else :
             rep=rep + ['error']
        i=i+1
    return tuple(rep)
#question n°5
def Math2Python(expression,vecteur,dicovar):
    rep=''
    for char in expression :
        if char=='!' :
            rep=rep+'not '
        if char=='+' :
            rep=rep+' or '
        if char=='*' :
            rep=rep+' and '
        if char=='(' :
            rep=rep+'('
        if char==')' :
            rep=rep+')'
        if char=='' :
            rep=rep+''
        if char in dicovar:
            rep=rep+str(vecteur[dicovar[char]])
    return rep
#question n°6
def randbin():
    return 0 if random()<0.5 else 1

def TableVerite(expression,dicovar):
    n=len(dicovar)
    vec=[(randbin(),randbin(),randbin())]
    len_t = len(vec)
    while len_t < 2**n :
        t=(randbin(),randbin(),randbin())
        if not t in vec :vec+=[t]
        len_t = len(vec)
    result=[]
    for vec in vec :
        result += [vec +(1 if eval(Math2Python(expression,vec,dicovar))else 0,)]
    return result

#question 7
def affichetable(dicovar,expression,result):
    line_1="|"+"|".join(list(sorted(dicovar.keys()))+[expression])+"|"
    line_A="-" * len(line_1)
    print(line_A)
    print(line_1)
    print(line_A)
    #pour faire l'entete du tableau voir au dessus
    for i in range(len(result)):
        v=['1' if v else '0' for v in sorted(result)[i]]
    # v permet d'identifier le resultat vrai ou faux de la ligne i du tableau
        print("|"+"|".join(v))
    print(line_A+"\n")

#question 8: forme conjonctive
def FNC(TDV,listevar):
    disjonctiv = []

    for vector in TDV:
        if vector[len(vector)-1]==0:
            monome=[]
            for index , value in enumerate(vector[:len(vector)-1]):
                characeter=listevar[index]
                monome += [characeter if value ==1 else characeter +"\u0304"]
            disjonctiv += ["(" + "+".join(monome) + ")"]
    return "*".join(disjonctiv)

## QUESTION _ forme disjontive:
def FND(TDV,listevar):
    disjonctiv = []

    for vector in TDV:
        if vector[len(vector)-1]==1:
            monome=""
            for index , value in enumerate(vector[:len(vector)-1]):
                characeter=listevar[index]
                monome += characeter if value == 1 else characeter + "\u0304"
            disjonctiv +=[monome]
    return "+".join(disjonctiv)

#main
test='!(p+q)*(!p+r)+(p*q)'
vecteur=(False,False,True)

variables=ListerVariables(test)
print(variables,"\n")

dico=DicoVariables(variables)
print(dico,"\n")

binaire=Int2Bin(5,5)
print(binaire,"\n")

bool=Bin2Bool(binaire)
print(bool,"\n")

remplace=Math2Python(test,vecteur,dico)
print(remplace,"\n")

table = TableVerite(test,dico)
affichetable(dico,test,table)

fnc = FNC(table,variables)
print("forme normal conjonctive:",fnc,"\n")

fnd= FND(table,variables)
print("forme normale disjonctive:",fnd,"\n")
