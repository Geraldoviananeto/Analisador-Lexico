
import re

def lexical_analyzer():
    # Definir os padrões de tokens
    token_patterns = {
        'int': r'\b\d+\b',
        'float': r'\b\d+\.\d+\b',
        'identifier': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
        'keyword': r'\b(if|else|while|for|return|int|float|string|void)\b',
        'string': r'"[^"]*"',
        'symbol': r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]'
    }

    # Ler a entrada do usuário
    input_text = input("Digite o texto a ser analisado (ou 'sair' para encerrar):\n")

    # Sair do loop se o usuário digitar 'sair'
    if input_text.lower() == 'sair':
        return "Encerrando a análise léxica."

    # Inicializar a lista de tokens
    tokens = []

    # Percorrer o texto de entrada e identificar os tokens
    for line in input_text.split('\n'):
        for token_type, pattern in token_patterns.items():
            matches = re.findall(pattern, line)
            for match in matches:
                tokens.append({
                    'Token': match,
                    'Categoria': token_type
                })

    # Formatar a saída
    output = ''
    for token in tokens:
        output += f"<Token: '{token['Token']}', Categoria: {token['Categoria']}>\n"

    return output

# Executar o analisador léxico em loop
while True:
    result = lexical_analyzer()
    print(result)
    if result.startswith("Encerrando"):
        break
    print()
