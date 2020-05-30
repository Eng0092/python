num1=5
num2=6
print(num1>num2)
print(num1<num2)
print(5>6)
print(5<6)
print(5==6)
print(5==5)
print(5!=5)
print(5!=6)
print('\n')
print(5>=6)
print(5<=6)
print(6>=5)
print(5>=5)
print(int('5') <= int('6'))
print('\n')

print(False and False) #false
print(False and True) #false
print(True and False) #false
print(True and True) #true
a,b = 1,2
print(a>b and b<a) #false
print(a!=a and b ==b) #false
print(a==a and b<a) #false
print(a<b and b==b) #true
print('\n')

print(False or False) #false
print(False or True) #true
print(True or False) #true
print(True or True) #true
a,b = 4,7
print(a>5 or b!=7) #false
print(a!=4 or b==7) #true
print(a>2 or b<3) #true
print(a==4 or b==(10-3)) #true

print(not False) #true
print(not True) #false
a,b,c = 4,2,8
print(not a<b) #true
print(not c!=b) #false
print('\n')

print(5>6 or 8>2)
print(5>6 or 8<13)
print(5==5 and 2==(10/5))
print(2!=4 and 4<2)
