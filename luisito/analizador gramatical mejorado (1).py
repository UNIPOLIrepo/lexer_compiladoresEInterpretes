tabla = {
    "<Program>": {"init": 1},
    "<Body>": {"var": 2, "{": 3},
    "<Declare>": {"var": 4},
    "<Identifiers>": {"identifier": 5},
    "<Au1>": {";": 6, "ε": 7},
    "<Types>": {"integer": 8, "decimal": 8, "char": 8, "string": 8, "bool": 8},
    "<Default>": {"integer": 9, "decimal": 10, "char": 11, "string": 12, "bool": 13},
    "<Main>": {"{": 14},
    "<Statement>": {
        "identifier": 15, "for": 16, "while": 17, 
        "if": 18, "id": 19, "read": 20, "write": 21
    },
    "<Expression>": {
        "identifier": 22, "decimal": 22, "{": 22, 
        "true": 22, "false": 22, "string": 22
    },
    "<Au2>": {
        "==": 23, "<": 23, ">": 23, "<=": 23, 
        ">=": 23, "!=": 23, "ε": 24
    },
    "<Exp>": {
        "identifier": 25, "decimal": 25, "{": 25, 
        "true": 25, "false": 25, "string": 25
    },
    "<Au3>": {
        "+": 26, "-": 27, "||": 28, 
        "{": 29, "==": 29, "<": 29, ">": 29, 
        "<=": 29, ">=": 29, "!=": 29, 
        "do": 29, ")": 29, "then": 29, "ε": 29
    },
    "<Rel>": {
        "==": 30, "<": 31, ">": 32, 
        "<=": 33, ">=": 34, "!=": 35
    },
    "<Assign>": {"identifier": 36},
    "<Term>": {
        "identifier": 37, "decimal": 37, "{": 37, 
        "true": 37, "false": 37, "string": 37
    },
    "<Au4>": {
        "*": 38, "/": 39, "&&": 40, 
        ";": 41, "}": 41, "+": 41, "-": 41, 
        "||": 41, "==": 41, "<": 41, ">": 41, 
        "<=": 41, ">=": 41, "!=": 41, 
        "do": 41, ")": 41, "then": 41, "ε": 41
    },
    "<Factor>": {
        "{": 42, "identifier": 43, "true": 44, 
        "false": 45, "string": 46, "decimal": 47
    },
    "<Statements>": {
        "identifier": 48, "for": 48, "while": 48, 
        "if": 48, "id": 48, "read": 48, "write": 48
    },
    "<Au5>": {
        "identifier": 49, "for": 49, "while": 49, 
        "if": 49, "id": 49, "read": 49, "write": 49, 
        "}": 50, "ε": 50
    },
    "<For Statement>": {"for": 51},
    "<Counter>": {"id": 52},
    "<While Statement>": {"while": 53},
    "<Input>": {"read": 54},
    "<Output>": {"write": 55},
    "<Au6>": {"(": 56, ",": 57, "ε": 57},
    "<Au7>": {"identifier": 58},
    "<If Statement>": {"if": 59},
    "<Au8>": {"else": 60, "endif": 61}
}

producciones = {
    1: ['init', 'identifier', ';', '<Body>', 'end'],
    2: ['<Declare>', '<Main>'],
    3: ['<Main>'],
    4: ['var', '<Identifiers>', ':', '<Types>', ';'],
    5: ['identifier', '<Au1>'],
    6: [';', 'identifier', '<Au1>'],
    7: ['ε'],
    8: ['<Default>'],
    9: ['integer'],
    10: ['decimal'],
    11: ['char'],
    12: ['string'],
    13: ['bool'],
    14: ['{', '<Statement>', '}'],
    15: ['<Assign>'],
    16: ['<For Statement>'],
    17: ['<While Statement>'],
    18: ['<If Statement>'],
    19: ['<Counter>'],
    20: ['<Input>'],
    21: ['<Output>'],
    22: ['<Exp>', '<Au2>'],
    23: ['<Rel>', '<Exp>'],
    24: ['ε'],
    25: ['<Term>', '<Au3>'],
    26: ['+', '<Term>'],
    27: ['-', '<Term>'],
    28: ['||', '<Term>'],
    29: ['ε'],
    30: ['=='],
    31: ['<'],
    32: ['>'],
    33: ['<='],
    34: ['>='],
    35: ['!='],
    36: ['identifier', '=', '<Expression>', ';'],
    37: ['<Factor>', '<Au4>'],
    38: ['*', '<Factor>'],
    39: ['/', '<Factor>'],
    40: ['&&', '<Factor>'],
    41: ['ε'],
    42: ['{', '<Expression>', '}'],
    43: ['identifier'],
    44: ['true'],
    45: ['false'],
    46: ['string'],
    47: ['decimal'],
    48: ['<Statement>', ';', '<Au5>'],
    49: ['<Statement>', ';'],
    50: ['ε'],
    51: ['for', '<Counter>', 'do', '{', '<Statements>', '}'],
    52: ['id', ':=', '<Expression>', 'to', '<Expression>'],
    53: ['while', '<Expression>', 'do', '{', '<Statements>', '}'],
    54: ['read', '(', '<Au7>', ')', ';'],
    55: ['write', '(', '<Au7>', ')', ';'],
    56: [')'],
    57: [',', '<Au7>'],
    58: ['identifier', '<Au6>'],
    59: ['if', '<Expression>', 'then', '{', '<Statements>', '}', '<Au8>'],
    60: ['else', '{', '<Statements>', '}', 'endif'],
    61: ['endif']
}
def extract_right_side_elements(filename):
    elementos = []
    # Read the file
    with open(filename, 'r') as file:
        # Process each line
        for line in file:
            # Split the line by '=' 
            parts = line.split('=')
            if len(parts) > 1:
                # Trim both sides
                right_side = parts[1].strip()
                
                # If the right side is empty (which happens with ":=")
                if right_side == '':
                    elementos.append('=')
                else:
                    elementos.append(right_side) 
    return elementos
def procesar_elementos(elementos):
    entrada = []  
    # Iterar sobre cada elemento y agregarlo a entrada
    for elemento in elementos:
        entrada.append(elemento)
    # Agregar '$' al final del arreglo
    entrada.append('$')
    return entrada
filename = 'inputAnalizadorG.txt'
# Extraer elementos del archivo
elementos = extract_right_side_elements(filename)
# Procesar elementos y crear entrada
def analizador_sintactico_modificado():
    # Leer tokens desde el archivo
    entrada = procesar_elementos(elementos)
    if entrada is None:
        return
    # Resto del código del analizador sintáctico (igual que antes)
    pila = ['$', '<Program>']
    indice = 0
    print("Entrada inicial:", entrada)
    print("Pila inicial:", pila)
    while True:
        if indice >= len(entrada):
            break
        if not pila:
            break
        tope = pila[-1]
        token = entrada[indice]
        print(f"\n--- Iteración ---")
        print(f"Tope de pila: {tope}")
        print(f"Token actual: {token}")
        print(f"Pila actual: {pila}")
        print(f"Índice: {indice}")
        if token == '$' and tope == '$':
            print("¡Cadena aceptada!")
            return True
        if token == tope:
            pila.pop()
            indice += 1
            print(f"Coincidencia: consumido {token}")
            continue
        elif tope in tabla:
            if token in tabla[tope]:
                num_produccion = tabla[tope][token]
                simbolos = producciones[num_produccion]
                print(f"Aplicando producción {num_produccion}: {simbolos}")
                pila.pop()
                if simbolos != ['ε']:
                    pila.extend(reversed([s for s in simbolos if s != 'ε']))
                continue
            elif 'ε' in tabla[tope]:
                print(f"Encontrado epsilon para {tope}")
                pila.pop()
                continue
            else:
                raise SyntaxError(f"Token inesperado: {token}. Tope: {tope}. Esperados: {list(tabla[tope].keys())}")        
        else:
            raise SyntaxError(f"Símbolo inesperado en la pila: {tope}. Token: {token}")
    raise SyntaxError("La cadena no fue completamente aceptada")
# Ejecutar el analizador
analizador_sintactico_modificado()