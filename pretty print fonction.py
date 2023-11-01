import numpy as np
import exact_cover as ec

#grille est une variable globale


grille = np.zeros((5,12))

#resu_cover = ec.get_exact_cover()

def pretty_print(resu_cover):
    sol = np.zeros((1,60))

    for i in range(12):
        line = resu_cover[i,:]
        nb = 0 
        while line[nb] == 0:
            nb+=1
        sol = sol + (nb+1)*line[12:]

    def suivant(i,j): #pour trouver la case suivange qui ne soit pas un obstacle
        x,y = grille.shape
        i2,j2 = i,j+1
        if j2>=y:
            return (i2+1,0)
        if grille[i2,j2] == -1:
            return suivant(i2,j2+1)
        return (i2,j2)

    (i,j) = suivant(0,-1)
    pretty_print = grille.copy()
    for cpt in range(60):
        pretty_print[i,j] = sol[0,cpt]
        i,j = suivant(i,j)
    

    return pretty_print
