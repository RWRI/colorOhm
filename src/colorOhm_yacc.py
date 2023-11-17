from numpy import split
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

def valor(var):
    id = existeVar(var);
    if(id == -1):
        print("Variavel "+var+" nao existente")
    else:
        if(Vars[id]['type'] == 'value'):
            return var


def p_main(p):
    'programa : INICIO operacoes FIM'
    f = open("interpretado.c", "w")
    f.write(f"#include <stdio.h>\n#include <string.h>\nint main(){{\n   {p[2]}\n   return 0;\n}}")
    f.close()

def p_operacao(p):
    '''
        operacao : declarando 
                  | definicaoValor
                  | definicaoResistor
                  | operacaoParalelo
                  | operacaoSerie
                  | mostrar
    '''
    p[0] = p[1] + f"\n   "

def p_operacao_unica(p):
    '''
        operacoes : operacao 
    '''
    p[0] = p[1]

def p_operacoes(p):
    '''
        operacoes : operacoes operacao 
    '''
    p[0] = p[1] + p[2]

def p_tipo(p):
    '''
        tipo : RESISTOR 
             | VALOR_RESISTOR
    '''
    p[0] = p[1]

def p_declarando(p):
    '''
        declarando : tipo VARIAVEL TERMINADOR_LINHA
    '''
    Vars.append(
        {'name': p[2], 'type': p[1], 'value': None})
    if(p[1] == 'value'):
        p[0] = f'float {p[2]}{p[3]}\n   '
    else:
        p[0] = f'char {p[2]}[10]{p[3]}\n   '

def p_definicaoValor(p):
    '''
        definicaoValor : VARIAVEL ATRIBUICAO VALOR TERMINADOR_LINHA
    '''
    if existeVar(p[1]) == -1:
        print("Variavel não declarada!")
    Vars[existeVar(p[1])]['value'] = p[3]
    p[0] = f'{p[1]} = {p[3]}{p[4]}'

def p_definicaoResistor(p):
    '''
        definicaoResistor : VARIAVEL ATRIBUICAO modeloResistor TERMINADOR_LINHA
    '''
    if existeVar(p[1]) == -1:
        print("Variavel não declarada!")
    Vars[existeVar(p[1])]['value'] = p[3]
    p[0] = f'strcpy({p[1]},"{p[3]}"){p[4]}'

def p_modeloResisor3(p):
    '''
        modeloResistor : ABRE_COLCHETES cor VIRGULA cor VIRGULA cor FECHA_COLCHETES

    '''
    p[0] = f'{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}{p[7]}'

def p_modeloResisor4(p):
    '''
        modeloResistor : ABRE_COLCHETES cor VIRGULA cor VIRGULA cor VIRGULA cor FECHA_COLCHETES

    '''
    p[0] = f'{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}{p[7]}{p[8]}{p[9]}'

def p_Cor(p):
    '''
        cor : PRETO
            | MARROM
            | VERMELHO
            | LARANJA
            | AMARELO
            | VERDE
            | AZUL
            | VIOLETA
            | CINZA
            | BRANCO
            | DOURADO
            | PRATEADO
    '''
    p[0] = p[1]
    
def p_operacaoParalelo(p):
    '''
        operacaoParalelo : VARIAVEL ATRIBUICAO resParalelo TERMINADOR_LINHA
    '''
    p[0] = f'{p[1]} = {p[3]}{p[4]}\n    ' 

def p_resParalelo(p):
    '''
        resParalelo : VARIAVEL PARALELO VARIAVEL
    '''
    p[0] = f'(1.0/((1.0/{valor(p[1])})+1.0/({valor(p[3])})))'

def p_resParalelo2(p):
    '''
        resParalelo : resParalelo PARALELO VARIAVEL
    '''
    p[0] = f'(1.0/((1.0/{p[1]})+1.0/({valor(p[3])})))'

def p_operacaoSerie(p):
    '''
        operacaoSerie : VARIAVEL ATRIBUICAO resSerie TERMINADOR_LINHA
    '''
    p[0] = f'{p[1]} = {p[3]}{p[4]}\n    '

def p_resSerie(p):
    '''
        resSerie : VARIAVEL SERIE VARIAVEL
    '''
    p[0] = f'{valor(p[1])} + {valor(p[3])}'

def p_resSerie2(p):
    '''
        resSerie : resSerie SERIE VARIAVEL
    '''
    p[0] = f'{p[1]} + {valor(p[3])}'

def p_mostrar(p):
    '''
        mostrar : MOSTRAR ABRE_COLCHETES VARIAVEL FECHA_COLCHETES TERMINADOR_LINHA
    '''
    id = existeVar(p[3])
    if(id == -1):
        print("Variavel"+{p[3]}+"nao existente")
    else:
        if(Vars[id]['type'] == 'value'):
            p[0] = f'printf("%f\\n",{p[3]}){p[5]}'
        else:
            p[0] = f'printf("%s\\n",{p[3]}){p[5]}'

parser = yacc.yacc()

from exemploCodigos import interpretar

result = parser.parse(interpretar)

print('\nSeu codigo foi interpretado com sucesso\n')