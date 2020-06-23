from random import randint
def contarDigitosPares(numero):
    pares=0
    list2=[]
    for i in numero:
        pares=0
        for k in range(i-1):
            if (k%2==0):
                pares = pares + 1 
            else:
                pares = pares+0
        list2.append(pares)
    return list2        

def metodoburbuja(newlist):
    for i in range(1,10):
        for j in range (10-i):
            if newlist[j] >= newlist[j+1]:
                ordenado = newlist[j]
                newlist[j]=newlist[j+1]
                newlist[j+1]=ordenado
    return newlist


def main():
    numeros = []
    for i in range(10):
        s = randint(10000,100000)
        numeros.append(s)
    
    nuevo = contarDigitosPares(numeros)
    x1 = metodoburbuja(numeros)
    x2 = metodoburbuja(nuevo)
    print("EL NUMERO ",x1[9]," TIENE MÁS NUMEROS PARES EN TOTAL: ",x2[2])

if __name__ == "__main__":
    main()
