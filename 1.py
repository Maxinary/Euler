sum = 0
k = 0
while k<1000:
	sum+=k
	k+=3
k = 0
while k<1000:
	if k%3 != 0:
		sum+=k
	k+=5
print(sum)
