import ply.lex as lex

reserved = {
    'ohm':'INICIO',
    'endohm':'FIM',
    'show':'MOSTRAR',
    'resistor':'RESISTOR',
    'value': 'VALOR_RESISTOR',
    '(value)': 'CONVERSAO_VALOR',
    '(resistor)': 'CONVERSAO_RESISTOR',
}

tokens = [
    'TERMINADOR_LINHA',
    'ATRIBUICAO',
    'PARALELO',
    'SERIE',
    'VIRGULA',
    'PONTO',
    'ABRE_COLCHETES',
    'FECHA_COLCHETES',
    'COR',
    'VARIAVEL',
    'VALOR',
] + list(reserved.values())

t_TERMINADOR_LINHA = r';'
t_ATRIBUICAO = r'='
t_PARALELO = r'\|'
t_SERIE = r':'
t_VIRGULA = r","
t_PONTO = r'.'
t_ABRE_COLCHETES = r'\['
t_FECHA_COLCHETES = r'\]'
t_COR = r'k|m|r|o|y|g|d|v|a|w'
t_VALOR = r'\d+(.\d+)?'

def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIAVEL')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()