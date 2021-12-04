# a = 14
# A = 10.02
# Foydalanuvchining_Ismi = 'Eldor'
# print(type(A))
# ism = "Eldor"
# A = 'Abbos'
# print(type(A))
# A = 5
# print(type(A))
# A=5.26
# a=int(A)
# print(a)
# a='Salom'
# print(a)
# print(type(a))
# a,b,c,d=1,'Eldor',3,2
# print(c,a,d,b)
# a=25//12
# print(a)
# a=5
# b='\t456789'
# m='\nShoymardanov15'
# c=m+b
# print(c)
# a=True
# print(type(a))
# x = 1.2e2
# print(x)
# a=5 # 101
# b=a<<1
# print(b)
# a=7
# b=b+9-a*c
# b+=9-a*c
# a=5
# b=a
# a=25
# print(b)
# son1 = 5
# son2 = 0b110 # 6
# son3 = 0o11 # 9
# son4 = 0x5 # 26
# print(son1,son2,son3,son4) # 5 6 9 26
# print(son1 +son3)
# son = 204
# print("{0}".format(son)) # 15
# print("{0:0b}".format(son)) # 1111
# print("{0:07b}".format(son)) # 0001111
# print("{0:0o}".format(son)) # 17
# print("{0:02X}".format(son))
# a=2/3
# a=round(a,2)
# print(a)
import math

seknud=int(input("Sekundni kiriting s="))
s=seknud//3600
seknud=seknud-s*3600
minut=seknud//60
seknud=seknud-minut*60
print("{0:02}".format(s),":","{0:02}".format(minut),":","{0:02}".format(seknud))
a=math.cos(math.pi/2)
