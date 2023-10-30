#Напишите программу, демонстрирующую работу try\except\finally
def getvalues():
    x=input("x: ")
    y=input("y: ")
    try:
        x=int(x)
        y=int(y)
        return x,y
    except ValueError as v:
     print(v)
     return 0,0
    finally:
     print("finally выполняется до return")

x,y=getvalues()
print(x,y)