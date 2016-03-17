# -*- coding: utf-8 -*-
def isPrime(N):
	while N<=1000:
		num=0
		j=1
		while j<=N:
			if N%j==0:
				num=num+1
			j=j+1	
		if num==2:
			return 1
		else:
			return 0
		N=N+1	

N=2
sum=0
for N in range(2,1001):
	print '%d Prime:%d' %(N,isPrime(N))
	x=isPrime(N)
	if x==1:
		sum=sum+N
print 'The sum of the prime is %d.' %sum
