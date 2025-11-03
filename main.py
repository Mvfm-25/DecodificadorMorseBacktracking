# Projeto & Otimização de Algoritmos : T2
# Marcus Margarites (23102543)

# C: 21/10/25 - A: 03/11/25

MORSE_DICT = {
    "*-": "A", "-***": "B", "-*-*": "C", "-**": "D", "*": "E",
    "**-*": "F", "--*": "G", "****": "H", "**": "I", "*---": "J",
    "-*-": "K", "*-**": "L", "--": "M", "-*": "N", "---": "O",
    "*--*": "P", "--*-": "Q", "*-*": "R", "***": "S", "-": "T",
    "**-": "U", "***-": "V", "*--": "W", "-**-": "X", "-*--": "Y", "--**": "Z",

    " ": " ",

    "*----": "1", "**---": "2", "***--": "3", "****-": "4", "*****": "5",
    "-****": "6", "--***": "7", "---**": "8", "----*": "9", "-----": "0",

    "*-*-*-": ".", "--**--": ",", "**--**": "?", "*----*": "'",
    "-*-*--": "!", "-**-*":  "/", "-*--*": "(", "-*--*-": ")",
    "*-***": "&", "---***": ":", "-*-*-*": ";", "-***-": "=",
    "*-*-*": "+", "-****-": "-", "**--*-": "_", "*-**-*": "\"",
    "***-**-": "$", "*--*-*": "@"
}

def decodificar_morse(morse):
    resultados = []

    def backtrack(restante, atual):
        if not restante:
            resultados.append("".join(atual))
            return

        for i in range(1, len(restante) + 1):
            prefixo = restante[:i]
            if prefixo in MORSE_DICT:
                backtrack(restante[i:], atual + [MORSE_DICT[prefixo].lower()])

    backtrack(morse, [])
    return resultados


# Exemplo:
print("Decodificador Morse - v.1\n[mvfm]\n")
entrada = input("Escreva uma mensagem em morse para ser decodificada :")

possibilidades = decodificar_morse(entrada)

for idx, p in enumerate(possibilidades, 1):
    print(f"{idx}. {p}")