import sys
import time
start = time.time()
peso = 0
articulos = []
memo = []

def read_file(input_file):
	global peso
	global articulos
	global memo
	with open(input_file,'r') as file:
		line = file.readline()
		peso = int(line)
		line = file.readline()
		while line:
			line = line.split(',')
			articulos.append([int(line[0]), int(line[1])])
			line = file.readline()
	memo = [[-1 for x in range(peso+1)] for y in range(len(articulos))]

def fuerza_bruta(i, capacidad):
	global articulos, memo
	if i == len(articulos) or capacidad == 0:
		return 0
	#exploro los 2 caminos posibles, agarrar el articulo o no agarrarlo
	#si el articulo pesa mas que la capacidad actual ni siquiera lo intento tomar.
	op1 = fuerza_bruta(i+1, capacidad)
	op2 = 0
	if capacidad >= articulos[i][0]:
		op2 = articulos[i][1] + fuerza_bruta(i+1, capacidad-articulos[i][0])
	return max(op1,op2)

def dinamica(i, capacidad):
	global articulos, memo

	if i == len(articulos) or capacidad == 0:
		return 0
	if memo[i][capacidad] != -1:
		return memo[i][capacidad]

	op1 = dinamica(i+1, capacidad)
	op2 = 0
	if capacidad >= articulos[i][0]:
		op2 = articulos[i][1] + dinamica(i+1, capacidad-articulos[i][0])
	#guardo el estado i,capacidad por si en el futuro me lo topo de nuevo
	memo[i][capacidad] = max(op1,op2)
	return memo[i][capacidad]

read_file(sys.argv[2])
res = None
if(sys.argv[1] == "1"):
	print("Algoritmo de fuerza bruta")
	res = fuerza_bruta(0, peso)
elif(sys.argv[1] == "2"):
	print("Algoritmo de programacion dinamica")
	res = dinamica(0, peso)

print("Resultado: "+str(res))
end = time.time()
print("Tiempo de ejecucion "+str((end-start))+" segundos")