def main():
    lista = ["rojo", "amarillo", "verde", "naranja", "azul","blanco"]
    print("lista: ",lista)

    lista.pop(1)#removes by assigned value
    print("lista con pop: ",lista)

    lista.remove("rojo")#removes
    print("lista con remove: ",lista)

    print(len(lista))#counts stuff

    lista.sort()#sorts stuff
    print(lista)

    lista.insert(0, "negro")#add to the list
    print(lista)

    lista.append("gris")
    print(lista)

    numeros = [10, 20, 30]
    print("lista de numeros: ", numeros)

    numeros.append(40) #append
    print("numeros con append: ", numeros)

    numeros.insert(1, 15) #insert
    print("numeros con insert: ", numeros)

    print("Suma: ", sum(numeros)) #sum
    print("Minimo: ", min(numeros)) #min
    print("Maximo: ", max(numeros)) #max

if __name__ == "__main__":
    main()
