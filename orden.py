def main():
    print("Bienvenido al programa de ordenamiento de números.")
    
    tipo_numero = input("¿Qué tipo de números deseas ordenar? (entero/flotante): ").lower()
    if tipo_numero == "entero":
        numeros = [int(x) for x in input("Ingresa los números separados por espacios: ").split()]
    elif tipo_numero == "flotante":
        numeros = [float(x.replace(',', '.')) for x in input("Ingresa los números separados por espacios: ").split()]
    else:
        print("Tipo de número no válido. Debes seleccionar 'entero' o 'flotante'.")
        return
    
    orden = input("¿Cómo deseas ordenar los números? (ascendente/descendente): ").lower()
    if orden == "ascendente":
        numeros.sort()
    elif orden == "descendente":
        numeros.sort(reverse=True)
    else:
        print("Opción de orden no válida. Debes seleccionar 'ascendente' o 'descendente'.")
        return
    
    tabla = generar_tabla(numeros)
    primeros_numeros = "-".join([str(int(num)) for num in numeros[:2]])
    guardar_tabla_en_archivo(tabla, primeros_numeros)

def generar_tabla(numeros):
    num_por_fila = 8
    tabla = []

    for i in range(0, len(numeros), num_por_fila):
        fila = numeros[i:i+num_por_fila]
        fila_str = " ".join([str(num) for num in fila])
        tabla.append(fila_str)

    return "\n".join(tabla)

def guardar_tabla_en_archivo(tabla, nombre_archivo):
    nombre_archivo += ".txt"

    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(tabla)
        print(f"La tabla ha sido guardada en {nombre_archivo}.")
    except Exception as e:
        print("Hubo un error al guardar el archivo:", e)

if __name__ == "__main__":
    main()
