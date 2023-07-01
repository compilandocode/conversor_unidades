from longitud import metros_a_pulgadas, pulgadas_a_pies
from peso import kilogramos_a_libras, libras_a_gramos
from volumen import litros_a_galones, galones_a_onzas_fluidas

def convertir_longitud(valor, unidad_origen, unidad_destino):
    if unidad_origen == "metros" and unidad_destino == "pulgadas":
        return metros_a_pulgadas(valor)
    elif unidad_origen == "pulgadas" and unidad_destino == "pies":
        return pulgadas_a_pies(valor)
    # Agrega más conversiones de unidades de longitud según tus necesidades
    else:
        print("No se pudo realizar la conversión. Unidades no válidas.")
        return None

def convertir_peso(valor, unidad_origen, unidad_destino):
    if unidad_origen == "kilogramos" and unidad_destino == "libras":
        return kilogramos_a_libras(valor)
    elif unidad_origen == "libras" and unidad_destino == "gramos":
        return libras_a_gramos(valor)
    # Agrega más conversiones de unidades de peso según tus necesidades
    else:
        print("No se pudo realizar la conversión. Unidades no válidas.")
        return None

def convertir_volumen(valor, unidad_origen, unidad_destino):
    if unidad_origen == "litros" and unidad_destino == "galones":
        return litros_a_galones(valor)
    elif unidad_origen == "galones" and unidad_destino == "onzas fluidas":
        return galones_a_onzas_fluidas(valor)
    # Agrega más conversiones de unidades de volumen según tus necesidades
    else:
        print("No se pudo realizar la conversión. Unidades no válidas.")
        return None

if __name__ == "__main__":
    # Ejemplo de uso para longitud
    valor = 2.5
    unidad_origen = "metros"
    unidad_destino = "pulgadas"

    resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
    print(f"{valor} {unidad_origen} equivale a {resultado} {unidad_destino}.")

     # Ejemplo de uso para volumen
    valor = 100
    unidad_origen = "litros"
    unidad_destino = "galones"
    resultado = convertir_volumen(valor, unidad_origen, unidad_destino)
    print(f"{valor} {unidad_origen} equivale a {resultado} {unidad_destino}.")
    
    # Ejemplo de uso para peso
    valor = 200
    unidad_origen = "kilogramos"
    unidad_destino = "libras"
    resultado = convertir_peso(valor, unidad_origen, unidad_destino)
    print(f"{valor} {unidad_origen} equivale a {resultado} {unidad_destino}.")
    