global i
i=3
def penis():
    global i
    while i>0:
        a=input("ответ ")
        if a==l:
            print("правильно")
            break
        else: print("непраильно")
        i=i-1
        print("количество попыток",i)
        if i == 0:
            print("игра окончена")
            break
    print("количество попыток",i)
    return(i)
        
print("весит груша нельзя скушать")
l="лампа"
penis()
if i>0:
    print("Чем можно поделиться только один раз?")
    l="секрет"
    penis()
if i>0:
    print("Меня можно разрушить, не касаясь меня, можно даже не видеть меня. Кем я могу быть?")
    l= "тишина"
    penis()
