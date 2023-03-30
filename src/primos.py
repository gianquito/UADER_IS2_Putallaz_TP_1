#Le pide al usuario hasta que numero se buscan primos
max = int(input("Find primes up to what number? : "))
primeList = []
#for loop for checking each number
for x in range(2, max + 1): #va numero a numero (hasta el maximo) revisando si es primo
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
print(primeList) # se muestra la lista de primos
#-------------------------------------------------------------
# prime number calculator: find the first n primes
#Le pide al usuario cuantos numeros primos calcular
count = int(input("Find how many primes?: "))
primeList = []
x = 2
#Calcula los numeros primos
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)