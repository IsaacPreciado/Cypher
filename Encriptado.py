import math
def pal(frase):
    listi = []
    abc = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    finallist=[]
    for i in range(len(frase)):
        for j in range(len(abc)):
            if frase[i] == abc[j]:
                if(j < 10):
                    listi.append(str(0) + str(j))
                else:
                    listi.append(str(j))
    
    aux=[]
    while len(listi)%3!=0:
        aux.append(listi.pop())
    if len(aux)==2:
        listi.append("00")
        listi.append(aux[1])
        listi.append(aux[0])
    elif len(aux)==1:
        listi.append("00")
        listi.append("00")
        listi.append(aux[0])

    for i in range(0, len(listi), 3):
        finallist.append(listi[i]+listi[i+1]+listi[i+2])
    
    return finallist
    

p, q = 593, 719
p2, q2 = p-1, q-1

e = 2
n = p2*q2

while e < n:
    if math.gcd(e, n) == 1:
        break
    else:
        e = e+1

llave = (p*q, e)

#ask for the phrase
frase = input("Ingrese frase: ")

listifinal= pal(frase)
for i in range(len(listifinal)):
    aux= int(listifinal[i])
    listifinal[i]= aux

incriptado = []

for i in listifinal:
    incriptado.append(pow(i, e) % (p*q))


def d(numero, modulo):
    def algoritmo_extendido_euclides(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            mcd, x, y = algoritmo_extendido_euclides(b, a % b)
            return (mcd, y, x - (a // b) * y)

    mcd, x, _ = algoritmo_extendido_euclides(numero, modulo)

    if mcd == 1:
        inverso = x % modulo
        return inverso
    else:
        print("no")

inversa= d(e, n)
decodificado = []
cont = 0
pal = ""

for i in incriptado:
    decodificado.append(str((pow(i, inversa) % (p*q))))
    if(len(decodificado[cont]) < 6):
      faltan = 6 - len(decodificado[cont]);
      for i in range(faltan):
        pal += "0"
      decodificado[cont] = pal + decodificado[cont]
    cont += 1
    pal = ""

def convertir(numeros):    
  abc = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  nums = [int(str(numeros[0]) + str(numeros[1])), int(str(numeros[2]) + str(numeros[3])), int(str(numeros[4]) + str(numeros[5]))]

  for i in range(3):
    for j in range(len(abc)):
      if nums[i] == j:
        print(abc[j], end = "")

print("Frase: " + frase)
print("Encriptado: " + str(incriptado))
print("desencriptado: ", end = "")

for i in decodificado:
  convertir(i)