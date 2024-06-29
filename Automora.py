import re
import random

vehiculos = []

def validar_patente(patente):
    """Valida que el RUT ingresado sea correcto."""
    pattern = r"^\d{1,2}\.\d{3}\.\d{3}"
    return re.match(pattern, ) is not None

def grabar_datos_de_vehiculo(Tipo, patente, marca,precio, multas, fecha_de_registro_vehículo, nombre_del_dueño):
    """Graba los datos de una persona en la lista de afiliados."""
    if not validar_patente(patente):
        print("RUT inválido. Por favor, ingrese un RUT correcto.")
        return False
    if edad < 18:
        print("Edad inválida. Debe ser mayor a 18 años.")
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
    """Busca una persona por su RUT y muestra toda su información."""
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            return vehiculo
    print("No se ha encontrado Vehiculo.")
    return None

def imprimir_certificado(patente):
    """Imprime el certificado de afiliación de una persona."""
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
    """Sale del programa mostrando un mensaje de despedida."""
    print("Saliendo del programa. Gracias por usar el sistema registro seguro 'Auto Seguro'.")
