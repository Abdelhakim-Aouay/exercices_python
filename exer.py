'''A=int(input("donner la première valeur : "))
if A%2==0:
    print (A, "est un valeur paire")
else:
    print (A, "est un entier impair")'''

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

from math import sqrt
A=int(input("donner la premiere valeur : "))
B=int(input("donner la deuxieme valeur : "))
C=int(input("donner la troisieme valeur : "))
if A==0:
    X = (-C / B)
    print (X)
else:
    X1=-B+sqrt(pow(B,2)-4*(A*C))/2*A
    X2 = (-B-sqrt(pow(B,2)-4*A*C)/2*A)
    print(X1, X2)