import re
import random

vehiculos = []

def validar_patente(patente):

    return re.match(patente) is not None

def grabar_datos_de_vehiculo(tipo, patente, marca,precio, multas, fecha_de_registro_vehículo, nombre_del_dueño):
    
    if not validar_patente(patente):
        print("Patente inválido. Por favor, ingrese una Patente correcta.")
        return False

    vehiculo = {
        'Tipo': tipo,
        'Patente': patente,
        'Marca': marca,
        'Precio del Vehiculo': precio,
        'Multas': multas,
        'Fecha de Registro': fecha_de_registro_vehículo,
        'Nombre del Dueño': nombre_del_dueño
    }
    vehiculos.append(vehiculo)
    print("Vehiculo Registrado Correctamente.")
    return True

def buscar_patente(patente):
   
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            return vehiculo
    print("No se ha encontrado Vehiculo.")
    return None

def imprimir_certificado(patente):
    
    vehiculo = buscar_vehiculo(patente)
    if vehiculo:
        valor_certificado = random.randint(1500, 3500)
        print("\nCertificado de Afiliación")
        print("=========================")
        print(f"Tipo: {vehiculo['Tipo']}")
        print(f"Patente: {vehiculo['Patente']}")    
        print(f"Marca: {vehiculo['Marca']}")
        print(f"Precio del Vehuculo: {vehiculo['Precio del Vehiculo']}")
        print(f"Fecha de Registo: {vehiculo['Fecha de Registro']}")
        print(f"Nombre del Dueño: {vehiculo['Nombre del Dueño']}")
    else:
        print("No se pudo imprimir el certificado. Vehiculo no Encontrado.")

def salir():
    
    print("Saliendo del programa. Gracias por usar el sistema registro seguro 'Auto Seguro'.")
