import numpy as np 

vierge = np.zeros((5,5))

#on crée les différentes pièces

F = vierge.copy()
F[0:3,1],F[1,0],F[0,2] = 1,1,1

I = vierge.copy()
I[:,0] = 1

L = vierge.copy()
L[0:4,0],L[3,1] = 1,1

N = vierge.copy()
N[2:4,0],N[0:3,1] = 1,1

P = vierge.copy()
P[0:3,0],P[0:2,1] = 1,1

T = vierge.copy()
T[0,:],T[0:3,1] = 1,1

U = vierge.copy()
U[1,:],U[0,0],U[0,2] = 1,1,1

V = vierge.copy()
V[0:3,0],V[2,0:3] = 1,1

W = vierge.copy()
W[0:2,0],W[1:3,1],W[2:3,2] = 1,1,1

Z = vierge.copy()
Z[0,0:2], Z[1,1], Z[2,1:3] = 1,1,1

Y = vierge.copy()
Y[0,1],Y[1,0:2],Y[2,1],Y[3,1] = 1,1,1,1

X = vierge.copy()
X[0,1],X[1,0:3],X[2,1] = 1,1,1

def association(lettre) :
    Liste = [F,I,L,N,P,T,U,V,W,X,Y,Z]
    if lettre in Liste :
        position = Liste.index(lettre)
        return position

#certaines colonnes/lignes sont vides. On regarde celles qui
#nous intéressent

def maxlig(piece):
    vecteur = np.sum(piece,axis=1)
    fin = len(vecteur)
    for i in range(fin):
        if vecteur[fin-i-1] >= 1.:
            return fin-i-1
    return fin-1

def maxcol(piece):
    vecteur = np.sum(piece,axis=0)
    fin = len(vecteur)
    for i in range(fin):
        if vecteur[fin-i-1] >= 1.:
            return fin-i-1
    return fin-1

#on encode l'opération de symétrie

def sym(piece) : 
    indices_lignes_non_nulles = ~np.all(piece == 0, axis=1)
    indices_colonnes_non_nulles = ~np.all(piece == 0, axis=0)
    piece_sans_zeros = piece[indices_lignes_non_nulles][:, indices_colonnes_non_nulles]     # Sélectionner les lignes et colonnes non nulles
    piece_reflechie = np.fliplr(piece)
    piece_int = vierge+piece_reflechie
    nombre_de_colonnes_avec_que_des_zeros = np.sum(np.all(piece_int == 0, axis=0)) 
    piece_bis = np.roll(piece_int, shift=-nombre_de_colonnes_avec_que_des_zeros, axis=1)
    return piece_bis


#on numérote chaque case, en sotant les obstacles

def numgrille(grille):
    compte = 0
    m,n = grille.shape
    grillebis = -1*np.ones((m,n))
    for i in range(m):
        for j in range(n):
            if grille[i,j] == 0:
                grillebis[i,j] = compte
                compte+=1
    return grillebis

#avec une pièce et un morceau de notre grille, on regarde s'il n'y a pas
#d'obstacle qui gènent

def pasdecollison(A,B):
    m,n = A.shape
    for i in range(m):
        for j in range(n):
            if A[i,j] == 1 and B[i,j] == -1 :
                return False
    return True

#on construit le vecteur qui encode une position possible de la pièce

def attrib(grillebis,p,i,j,largeur,hauteur,m,n):
    vecteur = [0]*(grille[-1:-1]+1)
    for k in range(largeur):
        for l in range(hauteur):
            vecteur[i+k,j+l] = p[k,l]
    return vecteur

#on encode la fonction qui détermine l'ensemble des positions possibles
#pour une pièce donnée à une orientation donnée

def test(grille,piece):
    largeur = maxcol(piece)
    hauteur = maxlig(piece)
    p = piece.copy()
    p = p[0:largeur,0:hauteur]
    a,b = grille.shape
    total = []
    for i in range(a-largeur+1):
        for j in range(b-hauteur+1):
            if pasdecollison(p,grille[i:i+largeur+1,j:j+hauteur+1]):
                vecteur = atrib(grillebis,p,i,j,largeur,hauteur,m,n)

                index = [0 for i in range(12)] 
                index[association(piece)] = 1

                total.append([index,vecteur])
    return total
    



