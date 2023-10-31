import numpy as np
import matplotlib.pyplot as plt

l_col=np.zeros((13,3))
l_col[0]=(255,255,255)
l_col[1]=(173,20,87)
l_col[2]=(224,64,251)
l_col[3]=(101,31,255)
l_col[4]=(121,134,203)
l_col[5]=(33,150,243)
l_col[6]=(0,188,212)
l_col[7]=(29,233,182)
l_col[8]=(27,94,32)
l_col[9]=(238,255,65)
l_col[10]=(245,127,23)
l_col[11]=(109,76,65)
l_col[12]=(229,115,115)


test=[[3,3,6,6,7,5,5,5,11,11,11,11],[3,6,6,6,7,9,5,5,10,11,12,12],[3,1,6,7,7,9,9,10,10,10,12,8],[3,1,1,4,4,4,9,9,10,12,12,8],[1,1,4,4,2,2,2,2,2,8,8,8]]
print(np.shape(test))

def visu(pp):
    l_col=np.zeros((13,3))
    l_col[0]=(255,255,255)
    l_col[1]=(173,20,87)
    l_col[2]=(224,64,251)
    l_col[3]=(101,31,255)
    l_col[4]=(121,134,203)
    l_col[5]=(33,150,243)
    l_col[6]=(0,188,212)
    l_col[7]=(29,233,182)
    l_col[8]=(27,94,32)
    l_col[9]=(238,255,65)
    l_col[10]=(245,127,23)
    l_col[11]=(109,76,65)
    l_col[12]=(229,115,115)
    # je crée ma liste de couleurs
    x0=np.shape(pp)[1]
    y0=np.shape(pp)[0]
    x= x0*10 
    y = y0*10 
    tab= np.zeros((y,x,3), dtype=np.uint8)
    # je crée la grille 
    tab[:,:,:] = 255
    for i in range(x0):
        for j in range(y0):
            tab[j*10:(j+1)*10,i*10:(i+1)*10]=l_col[int(test[j][i])]
            #je remplis ma grille
    plt.imshow(tab)
    plt.show()

visu(test)
