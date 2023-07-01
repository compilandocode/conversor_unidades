def litros_a_galones(litros):
    return litros * 0.264172

def galones_a_onzas_fluidas(galones):
    return galones * 128

# El bloque para hacer pruebas solo en este archivo
if __name__ == "__main__":
    # Ejemplo de uso del módulo volumen.py
    litros = 10
    galones = litros_a_galones(litros)
    print(f"{litros} litros equivale a {galones:.2f} galones.")
