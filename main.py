a=int(input("Катет который прилажащий"))
b=int(input("Ну тип противолежащий катет"))
c=int(input("Гипотенуза типа"))
if c**2==a+b**2:
    sin=b/c
    cos=a/c
    p=3.14
    if sin<= p/4:
        print(sin)
    elif cos>p/4:
        print(cos)
    else:print("Прилащий крутой, значит больше противолежащего")
else:print("Ну а прямоугольный треугольник попуск")
