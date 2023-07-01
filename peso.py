def kilogramos_a_libras(kilogramos):
    return kilogramos * 2.20462

def libras_a_gramos(libras):
    return libras * 453.592

# El bloque para hacer pruebas solo en este archivo
if __name__ == "__main__":
    # Ejemplo de uso del módulo peso.py
    kilogramos = 5
    libras = kilogramos_a_libras(kilogramos)
    print(f"{kilogramos} kilogramos equivale a {libras:.2f} libras.")
