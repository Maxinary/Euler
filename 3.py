def factorize(a):
	factors = []
	for i in range(2, int(a**.5)+1):
		if(a%i == 0):
			factors.insert(int(len(factors)/2), int(a/i))
			factors.insert(int(len(factors)/2), i)
	return factors

a = factorize(600851475143)
a = a[:int(len(a)/2)]

#remove non-primes
for i in range(len(a) - 1, 0, -1):
	for j in range(i):
		if(a[i]%a[j] == 0):
			a.pop(i)
			break
print(a[len(a) - 1])
