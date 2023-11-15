import ply.yacc as yacc

from colorOhm_lex import tokens

Vars = []

def existeVar(name):
    index = 0
    for v in Vars:
        if v['name'] == name:
            return index
        index += 1
    return -1

def p_main(p):
    'programa : INICIO operacoes FIM'
    f = open("interpretado.c", "w")
    f.write(f"#include <stdio.h>\nint main(){{\n   {p[2]}\n   return 0;\n}}")
    f.close()

def p_operacao(p):
    '''
        operacao : declarando 
                  | definicaoValor
                  | mostrar
    '''
    p[0] = p[1] + f"\n   "

def p_operacao_unica(p):
    '''
        operacoes : operacao 
    '''
    p[0] = p[1] + f"\n   "

def p_operacoes(p):
    '''
        operacoes : operacoes operacao 
    '''
    p[0] = p[1] + p[2] + f"\n   "

def p_tipo(p):
    '''
        tipo : RESISTOR 
             | VALOR_RESISTOR
    '''
    p[0] = 'float'

def p_declarando(p):
    '''
        declarando : tipo VARIAVEL TERMINADOR_LINHA
    '''
    Vars.append(
        {'name': p[2], 'type': p[1], 'value': None})
    p[0] = f'float {p[2]}{p[3]}\n   '

def p_definicaoValor(p):
    '''
        definicaoValor : VARIAVEL ATRIBUICAO VALOR TERMINADOR_LINHA
    '''
    if existeVar(p[1]) == -1:
        print("Variavel não declarada!")
    Vars[existeVar(p[1])]['value'] = p[3]
    p[0] = f'{p[1]} = {p[3]}{p[4]}\n    '

def p_mostrar(p):
    '''
        mostrar : MOSTRAR ABRE_COLCHETES VARIAVEL FECHA_COLCHETES TERMINADOR_LINHA
    '''
    p[0] = f'printf("%f\\n",{p[3]}){p[5]}\n    '

parser = yacc.yacc()

print('\n----- fim codigo -----\n')
# entrada de teste para output de string comum
data0 = '''
    ohm 
        value a;
        a = 2;
        show[a];
    endohm
'''

result = parser.parse(data0)