##

import numpy as np

vierge = np.zeros((5,5))

#On définit les pièces comme une suite de 0 et de 1 dans une matrice de taille 5*5
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

X = vierge.copy()
X[0,1],X[1,0:3],X[2,1] = 1,1,1

Y = vierge.copy()
Y[0,1],Y[1,0:2],Y[2,1],Y[3,1] = 1,1,1,1

Z = vierge.copy()
Z[0,0:2], Z[1,1], Z[2,1:3] = 1,1,1

#print(F,I,L,N,P,T,U,V,W,X,Y,Z)


#On définit une fonction rotation de pièce -> effectue une rotation de pi/2 dans le sens horaire
#r est d'ordre 4 : r^4 = e
def rot(piece): #rotation de 90°
    lignes, colonnes = piece.shape
    
    pieceretournee = np.zeros((colonnes, lignes), dtype=piece.dtype) 

    for i in range(lignes): #on effectue la rotation
        for j in range(colonnes):
            pieceretournee[j, lignes - 1 - i] = piece[i, j]
    
    #on souhaite effectuer un décalage vers la gauche du nombre de colonnes contenant 0 pour retrouver la pièce en haut à gauche
    nombre_de_colonnes_avec_que_des_zeros = np.sum(np.all(pieceretournee == 0, axis=0)) 
    matrice_decalage = np.roll(pieceretournee, shift=-nombre_de_colonnes_avec_que_des_zeros, axis=1)
    return matrice_decalage

#print(rot(P))

#On définit maintenant une fonction symétrie -> effectue la réflexion selon un axe vertical. 
#La réflexion selon l'axe horizontal revient juste à rotation*réflexion*rotation
#La symétrie s est d'ordre 2 --> s² = e
def sym(piece) : 
    indices_lignes_non_nulles = ~np.all(piece == 0, axis=1)   
    indices_colonnes_non_nulles = ~np.all(piece == 0, axis=0)
    piece_sans_zeros = piece[indices_lignes_non_nulles][:, indices_colonnes_non_nulles]     
# On prend la matrice contenant uniquement la pièce, sans les lignes et colonnes nulles
    piece_reflechie = np.fliplr(piece) #on effectue la réflexion
    piece_int = vierge+piece_reflechie #on réinjecte dans une matrice 5*5
    nombre_de_colonnes_avec_que_des_zeros = np.sum(np.all(piece_int == 0, axis=0)) 
    piece_bis = np.roll(piece_int, shift=-nombre_de_colonnes_avec_que_des_zeros, axis=1) #on a recadré en haut à gauche
    return piece_bis

#print(sym(P))

Liste = [F,I,L,N,P,T,U,V,W,X,Y,Z]

#Fonction qui renvoie la position de la lettre 
def association(lettre) :
    if lettre in Liste :
        position = Liste.index(lettre)
        return position

#print(association(F))

#L'objectif maintenant est de créer une liste avec, pour chaque lettre, toutes ses différentes configurations possibles (sans répétitions).
#Pour ça, on teste d'abord l'ensemble généré par les rotations : on "applique" r la rotation 1 fois, si c'est la même figure, on s'arrête
#Sinon on continue (jusqu'à 3 itérations car r est d'ordre 4 : r^4 = id)
#On applique ensuite s une fois à la première figure, si le symétrique == la figure, rien ne se passe, sinon on effectue une symétrie
#pour tous les éléments de la liste de la lettre
#Listes des pièces avec configurations 
"""
Lettres_config = [[]]

for lettre in Liste :
    n = Lettres_config.index(lettre)
    Lettres_config[n].append(lettre)
    for k in range (0,3) : 
        if rot(lettre) != lettre :
            Lettres_config[n].append(rot(lettre))
        else : 
            break


print(Lettres_config)
"""