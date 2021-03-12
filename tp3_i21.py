from time import time
#question n°1:
#calcul de factorielle ( fact 6 : x1 x2 x3 x4 x5 x6)
def factorielle(n):
    if n == 0:
        return 1
    fact=1
    i=1
    while i <= n:
        fact = fact*i
        i+=1
    return fact

#question n°2:
#transmet les resultat sous forme le pyramide
def TrianglePascal(n):
    c=[]
    for x in range(n):
        c += [[1] * (x+1)]
    for x in range(2,n):
        for y in range (1,x):
            c[x][y] = c[x - 1][y - 1] + c[x - 1][y]
    return c

#question n°3:
#prendre la valeur donné et la transforme en tout les possi "." et "-"
def phoque(n):
    if n == 1: return ["."]
    elif n == 2: return ["-", ".."]

    n_1 = ["." + a for a in phoque(n - 1)]
    n_2 = ["-" + a for a in phoque(n - 2)]

    return n_1 + n_2

#question n°4:
#pareil que la question n°3
def phoqueit(n):
    s1 = ["."]
    s2 = ["-", ".."]

    if n == 0: return s1
    elif n == 1: return s2
    print("valeur phoque \n")

    for i in range(2, n):
        s1b = [a + "-" for a in s1]
        s2b = [a + "." for a in s2]
        s1, s2 = s2, s1b + s2b

    return s2

#question n°5:
def Fibonacci(n):
    termes = tuple()
    for i in range(n + 1):
        j, f1, f2 = 0, 0, 1
        while j < i+1:
            f1, f2 = f2, f1 + f2
            j += 1
        termes += (f2,)
    return termes

#question n°6:
def genuplet(n, m, nuplet):
    if n > 0:
        for i in range(m):
            genuplet(n - 1, m, nuplet + (i + 1,))
    else: print(nuplet)

genuplet(2, 3, ())

#main :
#question n°1
#print("valeur test factorielle \n")
test1=3#float(input())
rep=factorielle(test1)
print("la factorielle de",test1, "est:" ,rep,"\n")

#question n°2:
#print("valeur test du TrianglePascal \n")
test2=3#int(input())
rep2=TrianglePascal(test2)
print("le TrianglePascal de",test2,"est",rep2,"\n")

#question n°3:
#print("valeur phoque \n")
test3=4#int(input())
rep3=phoque(test3)
print("le code phoque de",test3,"est",rep3,"\n")

#question n°4:
#print("valeur phoqueit \n")
test4=4#int(input())
rep4=phoque(test3)
print("le code phoque de",test4,"est",rep4,"\n")

#question n°5:
print("valeur Fibonacci \n")
test5=5#int(input())
rep5=Fibonacci(test5)
print("la valeur Fibonacci de",test5,"est",rep5,"\n")

#question n°6:
print("valeur genuplet \n")
test6=2#int(input())
test7=3#int(input())
rep6=genuplet(test6,test7,())
print("la valeur genuplet de",test6,"est",rep6,"\n")
