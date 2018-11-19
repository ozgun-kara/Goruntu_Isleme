import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def randomMatrisGenerator(): 
    return np.random.randint(0,2,(28,28))

def findMBR(array): 
    MBR ={"minX": 28,"maxX": 0,"minY": 28,"maxY": 0}
    satirsayisi,sutunsayisi=0,0
    for satir in array:
        for eleman in satir:
            if(eleman==1 and MBR["minX"]>sutunsayisi+1):
                MBR["minX"]=sutunsayisi+1
            if(eleman==1 and MBR["maxX"]<sutunsayisi+1):
                MBR["maxX"]=sutunsayisi+1
            if(eleman==1 and MBR["minY"]>satirsayisi+1):
                MBR["minY"]=satirsayisi+1
            if(eleman==1 and MBR["maxY"]<satirsayisi+1):
                MBR["maxY"]=satirsayisi+1
            sutunsayisi=sutunsayisi+1
        satirsayisi=satirsayisi+1
        sutunsayisi=0
    return MBR  

def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            if(character_a[i,j]==character_b[i,j]):
                my_similarity=my_similarity+1
    return my_similarity

for i in range(100):
    if(i==0):
        anaCharacter = randomMatrisGenerator()
        enBenzer = 0
    digerCharacter = randomMatrisGenerator()
    benzerlik = get_similarity(anaCharacter,digerCharacter)

    if(benzerlik>enBenzer):
        enBenzer = benzerlik
        enBenzerCharacter = digerCharacter
        
print("Benzerliði en yüksek karakter: ", enBenzer, " Oraný: ",round(enBenzer/784.0*100,2))
plt.imshow(anaCharacter,cmap='gray')
plt.show()
plt.imshow(enBenzerCharacter,cmap='gray')
plt.show()