sum = 0
a = 2
b = 1
while a<4000000:
	sum+=a
	for _ in range(3):
		c=a
		a+=b
		b=c
		
print(sum)
