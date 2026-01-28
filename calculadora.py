#hacer un programa que despliegue un menu que permita hacer las operaciones sencillas
#de una calculador (suma,resta,multi,div)

def menu():
    print("""*** CALCULADORA SENCILLA ***
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir
---------
Opcion(1-5)? """)
    
def leer_opcion():
    op = input()
    while(not op.isdigit() or int(op) < 1  or int(op) > 5):
        print("Error. Opcion invalida. Digite un numero de 1 a 5")
        input("Presione cualquier letra para continuar....")
        print("\n\n")
        menu()
        op = input(
        )
    return int(op)

def leer_float(msg):
    while (True):
        try:
            str_num = float(input(msg))
            return str_num
        except ValueError:
            print("Error. NO es un numero float valido")
            input("Intente nuevamente. Presione cualquier tecla para continuar")


def suma():
    print("*** 1.Suma ***")

    n1 = leer_float("Ingrese el primer numero:")
    n2 = leer_float("Ingrese el segundo numero:")
    print(f"La suma es: {n1+n2}")
    return n1 + n2

def resta():
    print("*** 2.Resta ***")

    n1 = leer_float("Ingrese el primer numero:")
    n2 = leer_float("Ingrese el segundo numero:")
    print(f"La resta es: {n1-n2}")
    return n1 - n2

def multiplicacion():
    print("*** 3.Multiplicacion ***")

    n1 = leer_float("Ingrese el primer numero:")
    n2 = leer_float("Ingrese el segundo numero:")
    print(f"La multiplicacion es: {n1*n2}")
    return n1 * n2

def division():
    print("*** 4.Division ***")

    n1 = leer_float("Ingrese el primer numero:")
    n2 = leer_float("Ingrese el segundo numero:")
    print(f"La division es: {n1/n2}")
    return n1 / n2


def main():
    opcion = 0
    while(opcion !=5):
        menu()
        opcion = leer_opcion()

        if opcion ==1:
            suma()
        elif opcion ==2:
            resta()
        elif opcion ==3:
            multiplicacion()
        elif opcion ==4:
            division()
        elif opcion ==5:
            print("\n\nGracias por usar la calculadora. ADIOS.")
            
        input("Presione cualquier tecla para terminar")
        print("\n\n\n")        


main()