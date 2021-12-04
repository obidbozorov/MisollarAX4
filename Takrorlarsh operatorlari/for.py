# b=[7,8,56,6,9,'dasdad',12,6,11]
# for i in b:
#     print(i)
# for i in range(10):#for(int i=0;i<n;i++)
#     print(i)
# b=[7,8,56,6,9,'dasdad',12,6,11]
# for i in range(len(b)):
#     print(b[i],end=" ")
# sum = 0
# n = int(input("n="))
# for i in range(1, n + 1):
#     continue
#     sum = sum + i
# print("summa(1+...+n) =", sum)
# n=int(input("n="))
# s=0
# for i in range(n+1):
#     s=s+i
# print("1-s=",s)
# s=0
# for i in range(1,n+1):
#     s=s+i
# print("2-s=",s)
# s=0
# for i in range(1,n+1,1):
#     s=s+i
# print("3-s=",s)
# n=50
# for i in range(n,0,-2):
#     print(i)
# ismlar=["Faxriddin", "Bekzod","Nosir","Aktam",[5,6,7,8,9,10],7,9,8,7,True]
# for i in ismlar:
#     print(i)
a=[4,5,9,74,89,-2,-24,48,6447,152]
for i in a:
    if i<0:
        break
    if i%2==0:
        continue
    else:print(i,end=" ")

b=[11,12,13,45,17,-9,78,14,6,9,8]
i=0
# while i<min(len(a),len(b)) and ((a[i]>0 and b[i]>0) or (a[i]<0 and b[i]<0)):
#     print(a[i], end=" ")
#     print(b[i])
#     i=i+1
# while i<min(len(a),len(b)) and a[i]*b[i]>0:
#     print(a[i], end="\t\t")
#     print(b[i])
#     i=i+1