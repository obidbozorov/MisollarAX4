# a=[1,'AX',3,[4,[5,7],11],True,6.05]
# #print(type(a))
# print(a[-3:])
# a=[12,13]
# print(a*6)
# b=list(range(101))
# for i in b:
#     print(i)
# nums1 = [1,3,2]
# nums2 = [3,1,2]
# if nums1[1] == nums2[0]:
#     print("Bu ro`yxatlar aynan teng.")
# else:
#     print("Bu ro`yxatlar teng emas.")
# a=[1,2,4,4]
# a.append(3)
# # a.insert(0,4)#[1,2,4,3]
# # a.remove(4)
# # print(a)
# # a.pop(2)
# a=list("Assalomu alaykum")
# print(a.count('a'))
# #print(a.index(8))
# son=[7,98,12,58,66,45,2,6,55,15,51]
# nomlar = ["Anvar","Sobir","Sobir","Qosim"]
# son.sort()
# print(son)
# nomlar = ["anvar","Sobir","sobir","Qosim","tolib"]
# sorted_nomlar = sorted(nomlar, key = str.lower)
# print(sorted_nomlar)
# print(min(son))
# vil1 = ["Toshkent", "Xorazm", ]
# vil2=[]
# vil2=list.copy(vil1)
# vil2.append('Buxoro')
# vil1.append('Samarqand')
# print(vil1) # ['Toshkent', 'Xorazm', 'Buxoro']
# print(vil2) # ['Toshkent', 'Xorazm', 'Buxoro']
# a=[]
# n=int(input("Ro`yxatda nechta element bo`lsin!"))
# for i in range(n):
#     a.append(input(str(i+1)+"-elementni kiriting="))
# print(a)
# vil = ["Toshkent", "Xorazm", 'Buxoro', 'Navoi', 'Jizzax','Surxondaryo']
# vil1 = vil[:2]
# print(vil1) # ['Toshkent', 'Xorazm']
# vil2 = vil[2:4]
# print(vil2) # ['Buxoro', 'Navoi']
# vil3 = vil[::3]
# print(vil3) # ['Xorazm', 'Navoi'
# vil1 = ["Toshkent", "Xorazm", 'Buxoro']
# vil1[1]='Sirdaryo'
# vil2 = ['Navoi', 'Jizzax']
# vil = vil2 + vil1
# print(vil)
# a=[1,45,89,56,57,82,69,47,13]
# minimum=min(a)
# maximum=max(a)
# maxurni=a.index(maximum)
# minurni=a.index(minimum)
# a[minurni]=maximum
# a[maxurni]=minimum
# print(a)
s=input("Satrni kiriting s=")
a=list(s.split(r','))
print(a)
