"""
pour la question 1
x={a,b,c,d,e}
g={a:{1,2},b:{1},c:{2,3},e{4}}
y={1,2,3,4,5,6}
pour la question 2
x={1,2,3,4,5,6}
g={a:{1,2},b:{1},c:{2,3},e{4}}
y={a,b,c,d,e}
"""

#question1
#creat° dico pour le fichier donne
def Lecture(nomFichier):
    with open(nomFichier, "r+") as fichier:
        X, G, Y = set(), dict(), set()
        for line in fichier.readlines():
            comp = line.rstrip().split(">")
            if len(comp[0]) == 0: continue
            if len(comp[1]) == 0: continue
            if not comp[0] in G.keys():
                G[comp[0]] = set()
            X.add(comp[0])
            G[comp[0]].add(comp[1])
            Y.add(comp[1])
        return X, G, Y

#question2
#cree l'inverse du dico du fichier
def reciproque(c):
    g_1=dict()

    for sortie in c[2]:
        if not sortie in g_1.keys():
            g_1[sortie]=set()
        for entree in c[0]:
            if sortie in c[1][entree]:
                g_1[sortie].add(entree)
    return c[2],g_1,c[0]

#question3
#donne les chiffres correspondant a la lettre donnee
def ImageDirecte(C,A):
    sortie=[]
    for x in A:
        if x in C[0]: sortie += [C[1][x]]
    return sortie

#question4
# donne les lettres correpondant aux chiffres donne
def ImageReciproque(C,B):
    return ImageDirecte(reciproque(C),B)

#question5
#melange question 1 et 2 en retirant les lettre et les chiffres sans correspondant et en faisant correspondre les lettre avec les lettres restantes
def Composer(g,f):
    G_g=g[1]
    G_f=f[1]
    G=dict()

    for entree_g in G_g.keys():
        for sortie_g in G_g[entree_g]:
            if len(sortie_g) !=0:
                G[entree_g]= ImageDirecte(f,sortie_g)[0]
    return g[0], G ,f[2]

#question6
#test si la correspondance est une fonction
def EstFonction(C):
    for value in C[1].values():
        if len(value)>1:
            return True
    return False

#question7
#test si la correspondance est une application
def EstApplication(C):
    if not EstFonction(C):
        return False
    for entree in c[0]:
        if entree =="":
            return False
    for sortie in c[1][entree]:
        if len(sortie)==0:
            return False
    return True

#affiche beau goss  resultat lisibe

def affiche(c):
    print("x=",str(c[0]).replace("'",''))
    print("G=",str(c[1]).replace("'",''))
    print("Y=",str(c[2]).replace("'",''),end='\n\n')
#main
fichier=Lecture("correspondance.txt")
compo=Composer(fichier,reciproque(fichier))

print("C:")
affiche(fichier)

print("C-1:")
affiche(reciproque(fichier))

print("image de a:",ImageDirecte(fichier,"a"),"\n")

print("image de 1:",ImageReciproque(fichier,"1"),"\n")

print("composer de c et c-1")
affiche(compo)

print("fonction ou non ?",EstFonction(fichier),"\n")

print("application ou non ?",EstApplication(fichier),"\n")
