# 3.Pedir numeros por teclado hasta que el usuario ingrese un 0, mostrar los numeros de menor a mayor.
def myFuncion(valueOne,list,tuple):
    list.append(valueOne)
    while valueOne > 0:
        valueOne = int(input("Escribe otro numero: "))
        list.append(valueOne)
    list.sort()
    tuple = list
    return tuple
list = []
tuple = ()
valueOne = int(input("Escribe un numero: "))
resultado = myFuncion(valueOne,list,tuple)
print(resultado)