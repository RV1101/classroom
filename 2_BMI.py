print 'input your weight in kg'
weight=input()
print 'input your high in m'
high=input()
print 'your BMI is %f' % (weight/high**2)
if(weight/high**2>=18.5 and weight/high**2<24):
	print 'your BMI is normal'
else:
	print 'U should care about your healthy!!'