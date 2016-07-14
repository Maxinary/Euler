def palindrome(a):
	a = str(a)
	for i in range(int(len(a)/2)):
		if(a[i] != a[len(a) - i - 1]):
			return False
	return True

largest = 0
minim = 100
for i in range(999, 100, -1):
	if i>minim:
		for j in range(999, minim, -1):
			if(palindrome(i*j) and i*j>largest):
				largest = i*j
				minim = min([i,j])
				break
	if(i%10==0):
		print(i)
print("BIG:", largest)
