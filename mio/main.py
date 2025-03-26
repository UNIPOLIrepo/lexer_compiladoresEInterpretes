tabla = {
    "<PROGRAM>": {"!init": 1},
    "<BODY>": {"var": 2, "{": 3},
    "<DECLARE>": {"var": 4},
    "<IDENTIFIERS>": {"identifier": 5},
    "<AUX1>": {";": 6, "ε": 7},
    "<TYPES>": {"integer": 8, "decimal": 8, "char": 8, "string": 8, "bool": 8},
    "<DEFAULT>": {"integer": 9, "decimal": 10, "char": 11, "string": 12, "bool": 13},
    "<MAIN>": {"{": 14},
    "<STATEMENT>": {
        "identifier": 15, "for": 16, "while": 17, 
        "if": 18, "id": 19, "read": 20, "write": 21
    },
    "<EXPRESION>": {
        "identifier": 22, "decimal": 22, "{": 22, 
        "true": 22, "false": 22, "string": 22
    },
    "<AUX2>": {
        "==": 23, "<": 23, ">": 23, "<=": 23, 
        ">=": 23, "!=": 23, "ε": 24
    },
    "<EXP>": {
        "identifier": 25, "decimal": 25, "{": 25, 
        "true": 25, "false": 25, "string": 25
    },
    "<AUX3>": {
        "+": 26, "-": 27, "||": 28, 
        "ε": 29
    },
    "<REL>": {
        "==": 30, "<": 31, ">": 32, 
        "<=": 33, ">=": 34, "!=": 35
    },
    "<ASIGN>": {"identifier": 36},
    "<TERM>": {
        "identifier": 37, "decimal": 37, "{": 37, 
        "true": 37, "false": 37, "string": 37
    },
    "<AUX4>": {
        "*": 38, "/": 39, "%%": 40, 
        "ε": 41
    },
    "<FACTOR>": {
        "{": 42, "identifier": 43, "true": 44, 
        "false": 45, "string": 46, "decimal": 47
    },
    "<STATEMENTS>": {
        "identifier": 48, "for": 48, "while": 48, 
        "if": 48, "id": 48, "read": 48, "write": 48
    },
    "<AUX5>": {
        "identifier": 49, "for": 49, "while": 49, 
        "if": 49, "id": 49, "read": 49, "write": 49, 
        "}": 50, "ε": 50
    },
    "<FOR STATEMENT>": {"for": 51},
    "<COUNTER>": {"id": 52},
    "<WHILE STATEMENT>": {"while": 53},
    "<INPUT>": {"read": 54},
    "<OUTPUT>": {"write": 55},
    "<AUX6>": {"identifier": 56},
    "<AUX7>": {")": 57, ",": 58},
    "<IF STATEMENT>": {"if": 59},
    "<AUX8>": {"endif": 60, "else": 61}
}

producciones = {
    1: ['!init', 'identifier', ';', '<BODY>', '!end'],
    2: ['<DECLARE>', '<MAIN>'],
    3: ['<MAIN>'],
    4: ['var', '<IDENTIFIERS>', ':', '<TYPES>', ';'],
    5: ['identifier', '<AUX1>'],
    6: [';', 'identifier', '<AUX1>'],
    7: ['ε'],
    8: ['<DEFAULT>'],
    9: ['integer'],
    10: ['decimal'],
    11: ['char'],
    12: ['string'],
    13: ['bool'],
    14: ['{', '<STATEMENT>', '}'],
    15: ['<ASIGN>'],
    16: ['<FOR STATEMENT>'],
    17: ['<WHILE STATEMENT>'],
    18: ['<IF STATEMENT>'],
    19: ['<COUNTER>'],
    20: ['<INPUT>'],
    21: ['<OUTPUT>'],
    22: ['<EXP>', '<AUX2>'],
    23: ['<REL>', '<EXP>'],
    24: ['ε'],
    25: ['<TERM>', '<AUX3>'],
    26: ['+', '<TERM>'],
    27: ['-', '<TERM>'],
    28: ['||', '<TERM>'],
    29: ['ε'],
    30: ['=='],
    31: ['<'],
    32: ['>'],
    33: ['<='],
    34: ['>='],
    35: ['!='],
    36: ['identifier', ':', '=', '<EXPRESION>'],
    37: ['<FACTOR>', '<AUX4>'],
    38: ['*', '<FACTOR>'],
    39: ['/', '<FACTOR>'],
    40: ['%%', '<FACTOR>'],
    41: ['ε'],
    42: ['{', '<EXPRESION>', '}'],
    43: ['identifier'],
    44: ['true'],
    45: ['false'],
    46: ['string'],
    47: ['decimal'],
    48: ['<STATEMENT>', ';', '<AUX5>'],
    49: ['<STATEMENTS>'],
    50: ['ε'],
    51: ['for', '<COUNTER>', 'do', '{', '<STATEMENTS>', '}'],
    52: ['id', ':=', '<EXPRESION>', 'for', '<EXPRESION>'],
    53: ['while', '<EXPRESION>', 'do', '{', '<STATEMENTS>', '}'],
    54: ['read', '(', '<AUX6>'],
    55: ['write', '(', '<AUX6>'],
    56: ['identifier', '<AUX7>'],
    57: [')'],
    58: [',', '<AUX6>'],
    59: ['if', '<EXPRESION>', 'then', '{', '<STATEMENTS>', '}', '<AUX8>'],
    60: ['endif'],
    61: ['else', '{', '<STATEMENTS>', '}', 'endif']
}

def mapear_token(token):
    """Mapea los tokens del lexer a los símbolos de la gramática."""
    # Mapeo específico de tokens
    if token.startswith('identificador'):
        return 'identifier'
    elif token.startswith('entero'):
        return 'integer'
    elif token.startswith('decimal'):
        return 'decimal'
    elif token.startswith('string'):
        return 'string'
    elif token.startswith('saveword'):
        # Mapeo de palabras reservadas
        palabras_reservadas = {
            '¡init': '!init',
            'end!': '!end',
            'var': 'var',
            'integer': 'integer',
            'decimal': 'decimal',
            'char': 'char',
            'string': 'string',
            'bool': 'bool',
            'true': 'true',
            'false': 'false',
            'for': 'for',
            'while': 'while',
            'if': 'if',
            'read': 'read',
            'write': 'write',
            'do': 'do',
            'then': 'then',
            'else': 'else',
            'endif': 'endif'
        }
        partes = token.split(': ')
        return palabras_reservadas.get(partes[0], token)
    elif token.startswith('relacional:'):
        # Mapeo de operadores relacionales
        operadores = {
            'menor que': '<',
            'mayor que': '>',
            'menor que o igual a': '<=',
            'mayor que o igual a': '>=',
            'distinto a': '!=',
            'igual a': '=='
        }
        partes = token.split(': ')
        return operadores.get(partes[1], token)
    elif token.startswith('aritmetico:'):
        # Mapeo de operadores aritméticos
        operadores = {
            'suma': '+',
            'resta': '-',
            'multiplicacion': '*',
            'division': '/'
        }
        partes = token.split(': ')
        return operadores.get(partes[1], token)
    elif token.startswith('logico:'):
        # Mapeo de operadores lógicos
        operadores = {
            'or': '||',
            'and': '&&',
            'negacion': '!'
        }
        partes = token.split(': ')
        return operadores.get(partes[1], token)
    elif token.startswith('delimitador:'):
        # Mapeo de delimitadores
        delimitadores = {
            'llave izq': '{',
            'llave der': '}',
            'punto y coma': ';',
            'dos puntos': ':',
            'parentesis izq': '(',
            'parentesis der': ')'
        }
        partes = token.split(': ')
        return delimitadores.get(partes[1], token)
    elif token.startswith('asignacion'):
        return ':='
    
    return token

def extract_tokens(filename):
    """Extrae los tokens del archivo de salida del lexer."""
    tokens = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            partes = line.strip().split(' = ')
            if len(partes) == 2:
                tokens.append(partes[1])
    tokens.append('$')
    return tokens

def analizador_sintactico():
    # Leer tokens del archivo de salida del lexer
    filename = './output.txt'
    tokens_lexer = extract_tokens(filename)
    
    # Mapear tokens
    entrada = [mapear_token(token) for token in tokens_lexer]
    
    print("Tokens de entrada:", entrada)
    
    pila = ['$', '<PROGRAM>']
    indice = 0
    
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
                print(f"Aplicando producción {num_produccion}: {tope} -> {simbolos}")
                pila.pop()
                if simbolos != ['ε']:
                    # Añadir en orden inverso
                    pila.extend(reversed([s for s in simbolos if s != 'ε']))
                continue
                
            elif 'ε' in tabla[tope]:
                print(f"Producción epsilon para {tope}")
                pila.pop()
                continue
                
            else:
                expected = list(tabla[tope].keys())
                raise SyntaxError(f"Token inesperado: '{token}'. Tope: '{tope}'. Esperados: {expected}")        
        else:
            raise SyntaxError(f"Símbolo inesperado en la pila: '{tope}'. Token: '{token}'")
    
    raise SyntaxError("La cadena no fue completamente aceptada")

# Ejecutar el analizador
try:
    resultado = analizador_sintactico()
    print("\nResultado final:", "Aceptado" if resultado else "Rechazado")
except SyntaxError as e:
    print("\nError de sintaxis:", e)
    print("Análisis terminado con errores")