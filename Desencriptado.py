import math
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

incriptado = [169789, 308984, 214866, 318078, 92114, 69387, 14740, 156947, 234707, 289875]


p, q = 571, 563
p2, q2 = p-1, q-1

e = 2
n = p2*q2

while e < n:
    if math.gcd(e, n) == 1:
        break
    else:
        e = e+1
e = 3539
llave = (p*q, e)
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
  abc = "abcdefghijklmnopqrstuvwxyz"
  nums = [int(str(numeros[0]) + str(numeros[1])), int(str(numeros[2]) + str(numeros[3])), int(str(numeros[4]) + str(numeros[5]))]

  for i in range(3):
    for j in range(len(abc)):
      if nums[i] == j:
        print(abc[j], end = "")

print("Encriptado: " + str(incriptado))
print("desencriptado: ", end = "")

for i in decodificado:
  convertir(i)