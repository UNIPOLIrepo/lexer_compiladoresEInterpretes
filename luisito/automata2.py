class Lexer:
    def __init__(self):
        # Palabras reservadas (sin caracteres especiales)
        self.reserved_words = {
            "init": "init",
            "end": "end",
            "var": "var",
            "integer": "integer",
            "decimal": "decimal",
            "bool": "bool",
            "if": "If",
            "then": "then",
            "else": "else",
            "endif": "endif",
            "true": "True",
            "false": "False",
            "while": "while",
            "do": "do",
            "for": "for",
            "read": "Read",
            "write": "Write"
        }
        
        # Tokens y sus representaciones
        self.token_types = {
            ':=': '=',
            '<': '<',
            '>': '>',
            '<=': '<=',
            '>=': '>=',
            '!=': '!=',
            '==': '==',
            '+': '+',
            '-': '-',
            '*': '*',
            '/': '/',
            '||': '||',
            '&&': '&&',
            '{': '{',
            '}': '}',
            '(': '(',
            ')': ')',
            ':': ':',
            ';': ';'
        }

    def analyze(self, text):
        results = []
        i = 0
        n = len(text)

        while i < n:
            # Saltar espacios en blanco
            if text[i].isspace():
                i += 1
                continue

            # Palabras reservadas e identificadores
            if text[i].isalpha() or text[i] == '$':
                start = i
                while i < n and (text[i].isalnum() or text[i] == '_' or text[i] == '$'):
                    i += 1
                word = text[start:i]

                # Verificar si es palabra reservada
                token = self.reserved_words.get(word)
                if token is not None:
                    results.append(f"{word} = {token}")
                else:
                    results.append(f"{word} = identifier")
                continue

            # Números (enteros/decimales)
            if text[i].isdigit():
                start = i
                while i < n and text[i].isdigit():
                    i += 1
                if i < n and text[i] == '.':
                    i += 1
                    while i < n and text[i].isdigit():
                        i += 1
                    results.append(f"{text[start:i]} = decimal")
                else:
                    results.append(f"{text[start:i]} = integer")
                continue

            # Operadores de 2 caracteres
            if i + 1 < n:
                two_char = text[i:i+2]
                if two_char in self.token_types:
                    results.append(f"{two_char} = {self.token_types[two_char]}")
                    i += 2
                    continue

            # Operadores de 1 carácter
            if text[i] in self.token_types:
                results.append(f"{text[i]} = {self.token_types[text[i]]}")
                i += 1
                continue

            # Caracteres no reconocidos
            results.append(f"{text[i]} = token no reconocido")
            i += 1

        return results

def main():
    try:
        with open('codigo.txt', 'r') as file:
            entrada = file.read()
        
        # Crear una instancia de Lexer y llamar al método analyze
        lexer = Lexer()
        resultados = lexer.analyze(entrada)
        
        with open('./inputAnalizadorG.txt', 'w') as file:
            file.write('\n'.join(resultados))

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'codigo.txt'")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()