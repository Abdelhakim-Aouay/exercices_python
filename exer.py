'''A=int(input("donner la première valeur : "))
if A%2==0:
    print (A, "est un valeur paire")
else:
    print (A, "est un entier impair")'''
import math

'''A=int(input("donner valeur : "))
if A%3==0 and A%7==0:
    print (A, "est un entier multiple de 3 et 7")
else:
    print (A, "n'est pas un entier multiple de 3 et 7")'''


'''A=float(input("donner valeur : "))
B=abs(A)
print(B)'''
'''A=int(input("donner la premiere valeur : "))
B=int(input("donner la deuxieme valeur : "))
C=int(input("donner la troisieme valeur : "))
if A<B and A<C :
    print (A)
elif B<A and B<C:
    print (B)
else :
    print (C)'''

'''from math import sqrt
A=int(input("donner la premiere valeur : "))
B=int(input("donner la deuxieme valeur : "))
C=int(input("donner la troisieme valeur : "))
delta=B ** 2-4*A*C
if A==0:
    X = (-C / B)
    print (X)
else:
    X1= -B + sqrt(delta)/(2*A)
    X2 = (-B-sqrt(delta))/(2*A)
    print(X1, X2)'''
'''
s=0
n=int(input("la valeur est "))
for i in range (0,n+1,5):
    s=s+i
    print(i,s)
print (s)'''

'''s=0
n=int(input("la valeur est "))
for i in range (0,n+1):
    s=s+pow(i,2)
    
print(s)'''

'''s = 1
n = int(input("la valeur est "))
for i in range(1, 20, 2):
    s = s *i
    print(i,s)
print(s)'''


#l=0
#s=input("donner une phrase  ")
#for i in (s):
#   print(i)
#    l=l+1
#print (l)

'''n=int(input("donner la valeur "))
for i in range (1,n+1):
    if n % i == 0 :
       print( i , end = ' ')'''
'''s=500
n=int(input("donner la valeur de n "))
while s < 600:
    for i in range(1, n):
        s=s+10
        print(i,s)

print(i+1)'''
'''n=int(input("donner un valeur "))
A=n
for i in range (1,n+1):
    A=n*i
    print(n,"*",i, " = ", A)'''


'''for i in range (1,11):
    A=i
    print("table de ", i)
    for c in range (1,11):
        A=i*c
        print(i, " * ", c, " = ", A)'''
'''n=int(input(" donner la valeur "))
A="*"
for i in range (1, n+1):
    print(A*i)'''

'''while True:
 n=float(input(" donner la valeur "))
 if n>1 and n<3:
     print ("bravo")
      break'''
s=4
i=4
while s<=1234:
      s=s+i
      i=i+1
print(i)











