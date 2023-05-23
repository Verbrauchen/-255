from random import randint 
x=randint(0,100)
i=0
print(x)
c=randint(1,2)
print("количество попыток",c)
a=int(input("угадай число "))
if 0<=a<=100:
    i=i+1
    while a!=x:
        i=i+1
        if a>x:
            print("загаданное число меньше ")
        elif a<x:
            print("загаданное число больше")
        a=int(input("побробуй еще "))
        if i-1>c:
            print("you lose")
            break
            
if a==x:
     print("ты угадал \nколичество  попыток",str(i) )
elif(0>a) or (a>100):
    print("ведди число от 0 до 100")      