a=int(input("год "))
if 0<a<999:
    if a%400==0:
        print("Высокосный")
    else: print("не Высокосный") 
elif a%4==0:
    print("Высокосный")
else: print("не Высокосный") 

