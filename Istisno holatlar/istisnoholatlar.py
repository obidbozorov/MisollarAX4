massiv=[1,4,8,9,5,2,66,89,47,65]
try:
    a = int(input("a sonini kiriting a="))
    b = int(input("b sonini kiriting b="))
    c=massiv[2]
    print(a/b)
    #print(a[0])
except ValueError as xato:
    print("Siz son kiritishingiz kerak!", xato)
except ZeroDivisionError:
    print("b sonining qiymati 0 bo'lmasligi kerak")
except IndexError:
    print("Massivning mavjud bo'lmagan elementig murojaat qildingiz")
except:
    print("Boshqa turdagi xatolik")
finally:
    print("Dastur ishlashi yakunlandi")


