def lexer(input_str):
    # Remove any potential byte order mark or unexpected leading characters
    input_str = input_str.lstrip('\ufeff\ufffe\xff\xfe')

    # * AUTOMATA
    transiciones = {
        'q0': [
            (lambda c: c == '$', 'q1'),
            (lambda c: c.isdigit(), 'q3'),
            (lambda c: c == "'", 'q6'),
            (lambda c: c == '/', 'q8'),
            (lambda c: c == ':', 'q12'),
            (lambda c: c == '<', 'q14'),
            (lambda c: c == '>', 'q16'),
            (lambda c: c == '!', 'q18'),
            (lambda c: c == '=', 'q20'),
            (lambda c: c == '+', 'q22'),
            (lambda c: c == '-', 'q23'),
            (lambda c: c == '*', 'q24'),
            (lambda c: c == '|', 'q25'),
            (lambda c: c == '&', 'q27'),
            (lambda c: c == '{', 'q29'),
            (lambda c: c == '}', 'q30'),
            (lambda c: c == '[', 'q31'),
            (lambda c: c == ']', 'q32'),
            (lambda c: c == '(', 'q33'),
            (lambda c: c == ')', 'q34'),
            (lambda c: c == ';', 'q35'),
        ],
        'q1': [(lambda c: c.isalnum(), 'q2')],
        'q2': [(lambda c: c.isalnum(), 'q2')],
        'q3': [
            (lambda c: c.isdigit(), 'q3'),
            (lambda c: c == '.', 'q4'),
        ],
        'q4': [(lambda c: c.isdigit(), 'q5')],
        'q5': [(lambda c: c.isdigit(), 'q5')],
        'q6': [
            (lambda c: c != "'", 'q6'),
            (lambda c: c == "'", 'q7'),
        ],
        'q7': [],
        'q8': [(lambda c: c == '*', 'q9')],
        'q9': [
            (lambda c: c != '*', 'q9'),
            (lambda c: c == '*', 'q10'),
        ],
        'q10': [(lambda c: c == '/', 'q11')],
        'q12': [(lambda c: c == '=', 'q13')],
        'q14': [(lambda c: c == '=', 'q15')],
        'q16': [(lambda c: c == '=', 'q17')],
        'q18': [(lambda c: c == '=', 'q19')],
        'q20': [(lambda c: c == '=', 'q21')],
        'q25': [(lambda c: c == '|', 'q26')],
        'q27': [(lambda c: c == '&', 'q28')],
    }

    # Estados de aceptación (clave: estado, valor: código de token)
    estados_aceptacion = {
        'q2': 100,  # identificador ($hola123)
        'q3': 150,  # entero (123)
        'q5': 200,  # decimal (123.123)
        'q7': 250,  # string ('hola')
        'q8': 451,  # aritmético (/)
        'q11': 300,  # comentario /*esto es un comentario */
        'q12': 557,  # delimitador (:)
        'q13': 350,  # asignacion (:=)
        'q14': 401,  # relacional (<)
        'q15': 403,  # relacional (<=)
        'q16': 402,  # relacional (>)
        'q17': 404,  # relacional (>=)
        'q18': 501,  # lógico (!)
        'q19': 405,  # relacional (!=)
        'q21': 406,  # relacional (==)
        'q22': 453,  # aritmético (+)
        'q23': 454,  # aritmético (-)
        'q24': 452,  # aritmético (*)
        'q26': 502,  # lógico (||)
        'q28': 503,  # lógico (&&)
        'q29': 551,  # delimitador ({)
        'q30': 552,  # delimitador (})
        'q31': 553,  # delimitador ([)
        'q32': 554,  # delimitador (])
        'q33': 555,  # delimitador (()
        'q34': 556,  # delimitador ())
        'q35': 558,  # delimitador (;)
    }

    # Significado de cada código de token
    codigos = {
        100: 'identificador',
        150: 'entero',
        200: 'decimal',
        250: 'string',
        300: 'comentario',
        350: 'asignacion',
        401: 'relacional: menor que',
        402: 'relacional: mayor que',
        403: 'relacional: menor que o igual a',
        404: 'relacional: mayor que o igual a',
        405: 'relacional: distinto a',
        406: 'relacional: igual a',
        451: 'aritmetico: division',
        452: 'aritmetico: multiplicacion',
        453: 'aritmetico: suma',
        454: 'aritmetico: resta',
        501: 'logico: negacion',
        502: 'logico: or',
        503: 'logico: and',
        551: 'delimitador: llave izq',
        552: 'delimitador: llave der',
        553: 'delimitador: corchete izq',
        554: 'delimitador: corchete der',
        555: 'delimitador: parentesis izq',
        556: 'delimitador: parentesis der',
        557: 'delimitador: dos puntos',
        558: 'delimitador: punto y coma',
        600: 'saveword'
    }

    #? Lista de palabras reservadas
    reserved_words = [
        "¡init", "end!", "array", "bool", "char", "decimal", "do", "else",
        "endif", "false", "for", "if", "integer", "of", "program", "read",
        "repeat", "string", "then", "true", "until", "var", "while", "write"
    ]

    reserved_words.sort(key=len, reverse=True)

    index = 0
    resultados = []
    longitud = len(input_str)

    while index < longitud:
        # Ignorar espacios, tabuladores y saltos de linea
        if input_str[index] in {' ', '\t', '\n', '\r'}:
            index += 1
            continue

        #! Bloque para las palabras reservadas
        encontrado = None
        for word in reserved_words:
            # Ajuste para manejar correctamente '¡init' y otras palabras reservadas
            if input_str.startswith(word, index):
                end_index = index + len(word)
                # Verificar que sea una palabra completa
                if (end_index >= longitud or not input_str[end_index].isalnum()):
                    encontrado = word
                    break

        if encontrado is not None:
            resultados.append(f"{encontrado} = {codigos[600]}")
            index += len(encontrado)
            continue

        # Resto del automata
        estado_actual = 'q0'
        inicio = index
        estado_aceptacion = None
        pos_aceptado = -1

        while index < longitud:
            char = input_str[index]
            transicion_encontrada = False

            # Verificar las transiciones desde el estado actual
            for condicion, estado_destino in transiciones.get(estado_actual, []):
                if condicion(char):
                    estado_actual = estado_destino
                    transicion_encontrada = True
                    break

            if not transicion_encontrada:
                break  

            # Si se llega a un estado de aceptación, se guarda
            if estado_actual in estados_aceptacion:
                estado_aceptacion = estado_actual
                pos_aceptado = index

            index += 1

        # Manejo de resultados tras procesar un token
        if estado_aceptacion is not None:
            token = input_str[inicio:pos_aceptado + 1]
            codigo = estados_aceptacion[estado_aceptacion]
            resultados.append(f"{token} = {codigos[codigo]}")
            index = pos_aceptado + 1
        else:
            # Si no hubo transición alguna
            if index == inicio:
                # Solo agregar como token no existente si no es un espacio o salto de línea
                if input_str[inicio] not in {' ', '\t', '\n', '\r'}:
                    resultados.append(f"{input_str[inicio]} = token no existe")
                index += 1
            else:
                token = input_str[inicio:index]
                resultados.append(f"{token} = token no reconocido")

    return resultados

# Lectura del archivo de entrada
with open('input.txt', 'r', encoding='utf-8') as file:
    entrada = file.read()

resultados = lexer(entrada)

# Escribir la salida en output.txt
with open('./output.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(resultados))