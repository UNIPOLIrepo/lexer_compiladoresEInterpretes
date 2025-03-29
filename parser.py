tabla = {
    'PROGRAM': {'¡init': 1},
    'BODY': {'var': 2, '{': 3},
    'DECLARE': {'var': 4},
    'IDENTIFIERS': {'identifier': 5},
    'AUX1': {';': 6, ':': 7},
    'TYPES': {'integer': 8, 'decimal': 8, 'char': 8, 'string': 8, 'bool': 8},
    'DEFAULT': {'integer': 9, 'decimal': 10, 'char': 11, 'string': 12, 'bool': 13},
    'MAIN': {'{': 14},
    'STATEMENT': {'identifier': 15, 'for': 16, 'while': 17, 'if': 18, 'id': 19, 'read': 20, 'write': 21},
    'EXPRESION': {'identifier': 22, 'decimal': 22, 'string': 22, '{': 22, 'true': 22, 'false': 22},
    'AUX2': {'==': 23, '<': 23, '>': 23, '<=': 23, '>=': 23, '!=': 23, ';': 24, '}': 24, 'for': 24, 'do': 24, 'then': 24},
    'EXP': {'identifier': 25, 'decimal': 25, 'string': 25, '{': 25, 'true': 25, 'false': 25},
    'AUX3': {'+': 26, '-': 27, '||': 28, ';': 29, '}': 29, '==': 29, '<': 29, '>': 29, '<=': 29, '>=': 29, '!=': 29, 'for': 29, 'do': 29, 'then': 29},
    'REL': {'==': 30, '<': 31, '>': 32, '<=': 33, '>=': 34, '!=': 35},
    'ASIGN': {'identifier': 36},
    'TERM': {'identifier': 37, 'decimal': 37, 'string': 37, '{': 37, 'true': 37, 'false': 37},
    'AUX4': {'*': 38, '/': 39, '&&': 40, ';': 41, '}': 41, '+': 41, '-': 41, '||': 41, '==': 41, '<': 41, '>': 41, '<=': 41, '>=': 41, '!=': 41, 'for': 41, 'do': 41, 'then': 41},
    'FACTOR': {'{': 42, 'identifier': 43, 'true': 44, 'false': 45, 'string': 46, 'decimal': 47},
    'STATEMENTS': {'identifier': 48, 'for': 48, 'id': 48, 'while': 48, 'read': 48, 'write': 48, 'if': 48},
    'AUX5': {'identifier': 49, 'for': 49, 'id': 49, 'while': 49, 'read': 49, 'write': 49, 'if': 49, '}': 50},
    'FOR STATEMENT': {'for': 51},
    'COUNTER': {'id': 52},
    'WHILE STATEMENT': {'while': 53},
    'INPUT': {'read': 54},
    'AUX6': {'identifier': 55},
    'AUX7': {')': 56, ',': 57},
    'OUTPUT': {'write': 58},
    'IF STATEMENT': {'if': 59},
    'AUX8': {'else': 60, 'endif': 61},
}

producciones = {
    1: ['¡init', 'identifier', ';', 'BODY', 'end!'], # PROGRAM
    2: ['DECLARE', 'MAIN'], # BODY
    3: ['MAIN'], #BODY
    4: ['var', 'IDENTIFIERS', ':', 'TYPES', ';'], # DECLARE
    5: ['identifier', 'AUX1'], # IDENTIFIERS
    6: [';', 'identifier', 'AUX1'], # AUX1
    7: ['Empty'], # AUX1
    8: ['DEFAULT'], # TYPES
    9: ['integer'], #DEFAULT
    10: ['decimal'], # DEFAULT
    11: ['char'], # DEFAULT
    12: ['string'], # DEFAULT
    13: ['bool'], # DEFAULT
    14: ['{', 'STATEMENT', '}'], # MAIN
    15: ['ASIGN'], # STATEMENT
    16: ['FOR STATEMENT'], # STATEMENT
    17: ['WHILE STATEMENT'], # STATEMENT
    18: ['IF STATEMENT'], # STATEMENT
    19: ['COUNTER'], # STATEMENT
    20: ['INPUT'], # STATEMENT
    21: ['OUTPUT'], # STATEMENT
    22: ['EXP', 'AUX2'], # EXPRESION
    23: ['REL', 'EXP'], # AUX2
    24: ['Empty'], # AUX2
    25: ['TERM', 'AUX3'], # TERM
    26: ['+', 'TERM'], # AUX3
    27: ['-', 'TERM'], # AUX3
    28: ['||', 'TERM'], # AUX3
    29: ['Empty'], # AUX3
    30: ['=='], # REL
    31: ['<'], # REL
    32: ['>'], # REL
    33: ['<='], # REL
    34: ['>='], # REL
    35: ['!='], # REL
    36: ['identifier', ':=', 'EXPRESION'], # ASIGN
    37: ['FACTOR', 'AUX4'], # TERM
    38: ['*', 'FACTOR'], # AUX4
    39: ['/', 'FACTOR'], # AUX4
    40: ['&&', 'FACTOR'], # AUX4
    41: ['Empty'], # AUX4
    42: ['{', 'EXPRESION', '}'], # FACTOR
    43: ['identifier'], # FACTOR
    44: ['true'], # FACTOR
    45: ['false'], # FACTOR
    46: ['string'], # FACTOR
    47: ['decimal'], # FACTOR
    48: ['STATEMENT', ';', 'AUX5'], # STATEMENTS
    49: ['STATEMENTS'], #AUX5
    50: ['Empty'], # AUX5
    51: ['for', 'COUNTER', 'do', '{', 'STATEMENTS', '}'], # FOR STATEMENT
    52: ['id', ':=', 'EXPRESION', 'for', 'EXPRESION'], # COUNTER
    53: ['while', 'EXPRESION', 'do', '{', 'STATEMENTS', '}'], # WHILE STATEMENT
    54: ['read', '(', 'AUX6'], # INPUT
    55: ['identifier', 'AUX7'], # AUX6
    56: [')'], # AUX7
    57: [',', 'AUX6'], # AUX7
    58: ['write', '(', 'AUX6'], # OUTPUT
    59: ['if', 'EXPRESION', 'then', '{', 'STATEMENTS', '}', 'AUX8'], # IF STATEMENT
    60: ['else', '{', 'STATEMENTS', '}', 'endif'], # AUX8
    61: ['endif'], # AUX8
}

def is_terminal(symbol):
    return symbol not in tabla

def parse(tokens):
    stack = ['$', 'PROGRAM']
    index = 0
    current_token = tokens[index] if index < len(tokens) else None
    step = 1

    print(" ⏳⏳ Iniciando análisis sintáctico... ⏳⏳\n")
    
    while stack:
        top = stack.pop()
        print(f"\n🚶Paso {step}:")
        print(f"💾  Pila:️ ➡️ {stack}⬅️ 🟢 [{top}] 🟢")
        print(f"🔴  Token actual: {current_token}")

        if top == '$':
            if current_token is None:
                print("\n 😉✅¡Análisis exitoso! La entrada es válida.")
                return True
            else:
                print(f"\n 🤔Error: Hay tokens restantes sin procesar: {current_token}")
                return False

        if is_terminal(top):
            if top == current_token:
                print(f"🔎 Coincidencia: Terminal '{top}' encontrado.")
                index += 1
                current_token = tokens[index] if index < len(tokens) else None
            else:
                print(f"\n ❌Error: Se esperaba'{top}' pero se encontró 🔎'{current_token}'")
                return False
        else:
            if current_token not in tabla.get(top, {}):
                print(f"\n ❌Error: No hay producción para {top} con el token 🔎'{current_token}'")
                return False
            
            prod_num = tabla[top][current_token]
            production = producciones[prod_num]
            print(f"☢️  Aplicando producción 🔎 [{prod_num}]: {top} 🟰  {' '.join(production)}")

            for symbol in reversed(production):
                if symbol != 'Empty':
                    stack.append(symbol)
        
        step += 1

    return False

if __name__ == "__main__":
    with open("outputP.txt", "r", encoding='utf-8') as file:
        input_tokens = file.read().split()
    print('\n 🔎Tokens detectados: ', input_tokens)
    
    success = parse(input_tokens)
    if not success:
        print("\n ❌😭La entrada no es válida.")