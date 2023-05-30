a=float(input("Первое число"))
b=float(input("Второе число"))
if b<a:
    print("Второе число меньше")
if a<b:
    print("Первое число меньше")
else: print ("Они одинаковы")

a=int(input("Сторона квадрата "))
b=int(input("Радиус круга "))
if 0<=0 and 0<=b:
    s=a**2
    if b>s:
        print ("Впишется")
    if b<s:
        print ("не впишется")
    if b==s:
        print("пересикутся")
else: print("erorr")

a=int(input("Сторона квадрата "))
b=int(input("Радиус круга "))
if 0<=0 and 0<=b:
    s=a**2
    if s>b:
        print ("Впишется")
    if s<b:
        print ("не впишется")
    if b==s:
        print("пересикутся")
else: print("erorr")

a=float(input("Первое число"))
b=float(input("Второе число")) 
s=[a,b]
print(max (s))

x=float(input())
if x<0:
    print (x**2)
elif x>0:
    print(1/x**2)
else: print ("error")
