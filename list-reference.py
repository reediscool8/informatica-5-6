def main():

    lista = ["rojo", "amarillo", "verde", "naranja", "azul","blanco"]
    print("lista: ",lista)

    lista.pop(1)#removes by assignd value
    print("lista con pop: ",lista)

    lista.remove("rojo")#removes
    print("lista con remove: ",lista)

    print(len(lista))#counts stuff

    lista.sort()#sorts stuff
    print(lista)

    lista.insert("negro")#add to the list
    print(lista)

    lista.append()



if __name__ == "__main__":
    main()
