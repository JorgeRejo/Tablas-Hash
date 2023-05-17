import re
from collections import defaultdict

def generar_tabla_hash(texto):
    tabla_hash = defaultdict(list)
    filas = texto.strip().split('\n')
    for fila, linea in enumerate(filas):
        tokens = re.findall(r'\b\w+\b', linea)  # Buscar tokens como palabras separadas
        for columna, token in enumerate(tokens):
            clave_hash = f'({fila},{columna})'
            tabla_hash[clave_hash].append(token)
    return tabla_hash

# Solicitar el campo de texto multilínea al usuario
print("Ingresa el campo de texto multilínea (presiona Enter dos veces para finalizar):")
campo_texto = ''
while True:
    linea = input()
    if linea == '':
        break
    campo_texto += linea + '\n'

tabla = generar_tabla_hash(campo_texto)

# Imprimir la tabla hash
for clave_hash, tokens in tabla.items():
    print(f'{clave_hash}: {tokens}')