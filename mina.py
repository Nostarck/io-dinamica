
import sys
import time
start = time.time()
mina = None
memo = None
INF = 1000000000000

def read_file(input_file):
	global mina,memo
	mina = []
	with open(input_file,'r') as file:
		line = file.readline()
		while line:
			oros = []
			line = line.split(',')
			for l in line:
				oros.append(int(l))
			mina.append(oros)
			line = file.readline()
	memo = [[-1 for x in range(len(mina))] for y in range(len(mina))]


def fuerza_bruta(i, j):
	global memo
	if(i < 0 or i == len(memo)):
		return -INF
	if(j == len(memo)-1):
		return mina[i][j]
	# exploro los 3 posibles caminos y le sumo el oro de la casilla actual
	op1 = mina[i][j] + fuerza_bruta(i,j+1)
	op2 = mina[i][j] + fuerza_bruta(i+1,j+1)
	op3 = mina[i][j] + fuerza_bruta(i-1,j+1)
	return max(max(op1,op2), op3)

def dinamica(i, j):
	global memo
	if(i < 0 or i == len(memo)):
		return -INF
	if(j == len(memo)-1):
		return mina[i][j]
	if(memo[i][j] != -1):#si ya calcule este estado retorno lo que calcule en el pasado
		return memo[i][j]
	op1 = mina[i][j] + dinamica(i,j+1)
	op2 = mina[i][j] + dinamica(i+1,j+1)
	op3 = mina[i][j] + dinamica(i-1,j+1)
	#guardo el estado i,j en la matriz memo por si en el futuro lo necesito calcular de nuevo
	memo[i][j] = max(max(op1,op2), op3)
	return memo[i][j]

read_file(sys.argv[2])
res = 0
if(sys.argv[1] == "1"):
	print("Algoritmo de fuerza bruta")
	for i in range(0,len(mina)):
		res = max(res, fuerza_bruta(i,0))
elif(sys.argv[1] == "2"):
	print("Algoritmo de programacion dinamica")
	for i in range(0,len(mina)):
		res = max(res, dinamica(i,0))

print("Resultado: "+str(res))
end = time.time()
print("Tiempo de ejecucion "+str((end-start))+" segundos")