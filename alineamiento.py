import sys
import time
start = time.time()
memo = None
path = None
str1 = None
str2 = None
def read_file(input_file):
	global str1, str2
	global memo,path
	with open(input_file,'r') as file:
		str1 = file.readline()
		str1 = str1.strip("\n")
		str2 = file.readline()
		str2 = str2.strip("\n")
	#para hacer los calculos de la programacion dinamica
	memo = [[0 for x in range(len(str2)+1)] for y in range(len(str1)+1)]
	#para guardar los caminos
	path = [[0 for x in range(len(str2)+1)] for y in range(len(str1)+1)]
	for i in range(len(memo)):
		memo[i][0] = i * -2
	for i in range(len(memo[0])):
		memo[0][i] = i * -2

def alineamiento():
	'''
	Para evaluar el score como el ejemplo del documento, tengo los siguientes criterios
	+1 si hay match
	-1 si hay dismatch
	-2 si hay guiones
	'''
	global memo
	global path
	global str1,str2
	str1_aligned = ""
	str2_aligned = ""

	for i in range(len(str1)):
		for j in range(len(str2)):
			op1 = memo[i][j+1]-2
			op2 = memo[i+1][j]-2
			op3 = memo[i][j] + (1 if str1[i]==str2[j] else -1)
			if(op1 > op2 and op1 > op3):
				path[i+1][j+1] = 0
				memo[i+1][j+1] = op1
			elif(op2 > op1 and op2 > op3):
				path[i+1][j+1] = 1
				memo[i+1][j+1] = op2
			else:
				path[i+1][j+1] = 2
				memo[i+1][j+1] = op3




def camino():
	global str1,str2
	i = len(memo)-1
	j = len(memo[0])-1
	str1_aligned = ""
	str2_aligned = ""
	print("Score: "+str(memo[i][j]))
	while i>0 or j >0:
		if(path[i][j] == 2):
			str1_aligned = str1[i-1] + str1_aligned
			str2_aligned = str2[j-1] + str2_aligned
			i -= 1
			j -= 1
		elif(path[i][j] == 0):
			str1_aligned = str1[i-1] + str1_aligned
			str2_aligned = "-" + str2_aligned
			i -= 1
		else:
			str1_aligned = "-" + str1_aligned
			str2_aligned = str2[j-1] + str2_aligned
			j -= 1

	print(str1_aligned)
	print(str2_aligned)



read_file(sys.argv[1])
alineamiento()
camino()
end = time.time()
print("Tiempo de ejecucion "+str((end-start))+" segundos")