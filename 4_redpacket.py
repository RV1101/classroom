# -*- coding: cp936 -*-
import random
def redpacket(people,money):
	result=[]
	x=[]
	s=0.0
	remain=people
	for i in range(people):
		t=random.random()
		while t==0:
			t=random.random()
		x.append(t)
		s+=x[0]
	for i in range(people):
		remain-=1
		result.append(money*x[remain]/s/100.0)
	return result
people=int(input('红包个数：\n'))
money=int(input('总金额：\n')*100)
a=redpacket(people,money)
print a
