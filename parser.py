import re

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
    1: ['¡init', 'identifier', ';', 'BODY', 'end!'],
    2: ['DECLARE', 'MAIN'],
    3: ['MAIN'],
    4: ['var', 'IDENTIFIERS', ':', 'TYPES', ';'],
    5: ['identifier', 'AUX1'],
    6: [';', 'identifier', 'AUX1'],
    7: ['Empty'],
    8: ['DEFAULT'],
    9: ['integer'],
    10: ['decimal'],
    11: ['char'],
    12: ['string'],
    13: ['bool'],
    14: ['{', 'STATEMENT', '}'],
    15: ['ASIGN'],
    16: ['FOR STATEMENT'],
    17: ['WHILE STATEMENT'],
    18: ['IF STATEMENT'],
    19: ['COUNTER'],
    20: ['INPUT'],
    21: ['OUTPUT'],
    22: ['EXP', 'AUX2'],
    23: ['REL', 'EXP'],
    24: ['Empty'],
    25: ['TERM', 'AUX3'],
    26: ['+', 'TERM'],
    27: ['-', 'TERM'],
    28: ['||', 'TERM'],
    29: ['Empty'],
    30: ['=='],
    31: ['<'],
    32: ['>'],
    33: ['<='],
    34: ['>='],
    35: ['!='],
    36: ['identifier', ':=', 'EXPRESION'],
    37: ['FACTOR', 'AUX4'],
    38: ['*', 'FACTOR'],
    39: ['/', 'FACTOR'],
    40: ['&&', 'FACTOR'],
    41: ['Empty'],
    42: ['{', 'EXPRESION', '}'],
    43: ['identifier'],
    44: ['true'],
    45: ['false'],
    46: ['string'],
    47: ['decimal'],
    48: ['STATEMENT', ';', 'AUX5'],
    49: ['STATEMENTS'],
    50: ['Empty'],
    51: ['for', 'COUNTER', 'do', '{', 'STATEMENTS', '}'],
    52: ['id', ':=', 'EXPRESION', 'for', 'EXPRESION'],
    53: ['while', 'EXPRESION', 'do', '{', 'STATEMENTS', '}'],
    54: ['read', '(', 'AUX6'],
    55: ['identifier', 'AUX7'],
    56: [')'],
    57: [',', 'AUX6'],
    58: ['write', '(', 'AUX6'],
    59: ['if', 'EXPRESION', 'then', '{', 'STATEMENTS', '}', 'AUX8'],
    60: ['else', '{', 'STATEMENTS', '}', 'endif'],
    61: ['endif'],
}

print('Ejecutando parser')

def clean_input(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:

            input_str = file.read()
            
        input_str = input_str.lstrip('\ufeff\ufffe\xff\xfe')
        
        tokens = re.findall(r'¡init|end!|\b\w+\b|[:=]{1,2}|[;{}()]|==|<=|>=|!=|\+|-|\*|/|\|\||&&', input_str)
        
        tokens.append('$')
        
        return tokens
    
    except FileNotFoundError:
        print(f" Error: Documento {filename} no encontrado.")
        return None
    except Exception as e:
        print(f" Error al leer el archivo: {e}")
        return None

def syntactic_analyzer(tokens):
    if not tokens:
        return False
    
    stack = ['$', 'PROGRAM']
    index = 0
    
    print("Input inicial:", tokens)
    print("Stack inicial:", stack)
    
    while stack and index < len(tokens):
        print(f"\n--- Iteracion ---")
        print(f"Stack Top: {stack[-1]}")
        print(f"Actual Token: {tokens[index]}")
        print(f"Actual Stack: {stack}")
        print(f"Index: {index}")
        
        top = stack[-1]
        token = tokens[index]
        
        if top == token:
            stack.pop()
            index += 1
            print(f"Match: Consumido {token}")
            continue
        
        if top in tabla:
            if token in tabla[top]:

                num_production = tabla[top][token]
                production = producciones[num_production]
                
                print(f"Aplicando produccion {num_production}: {production}")
                
                stack.pop()
                
                if production != ['Empty']:
                    stack.extend(reversed([s for s in production if s != 'Empty']))
                
                continue
            
            elif 'Empty' in producciones.get(num_production, []):
                print(f"Encontrado empty para {top}")
                stack.pop()
                continue
            
            else:
                print(f" Syntax Error: token no esperado: {token}. Top: {top}.  Esperado: {list(tabla[top].keys())}")
                return False
        
        else:
            print(f"Syntax Error: no se esperaba el simbolo en stack: {top}. Token: {token}")
            return False
    
    if index == len(tokens) and not stack:
        print("😉✅Codigo ACEPTADO!")
        return True
    
    print("😭❌ Codigo NO ACEPTADO")
    print(f"Remaining stack: {stack}")
    print(f"Remaining tokens: {tokens[index:]}")
    return False

def main():
    filename = 'outputP.txt'
    
    tokens = clean_input(filename)
    
    if tokens:
        syntactic_analyzer(tokens)

if __name__ == "__main__":
    main()