from numpy import split
import ply.yacc as yacc

from colorOhm_lex import tokens
from conversoes import conversao1, conversao2, modeloResitor2vetor

Vars = []

def existeVar(name):
    index = 0
    for v in Vars:
        if v['name'] == name:
            return index
        index += 1
    return -1

def valor(var):
    id = existeVar(var)
    if(id == -1):
        print("Variavel "+var+" nao existente")
    else:
        if(Vars[id]['type'] == 'value'):
            return var
        else:
            letras = modeloResitor2vetor(Vars[id]['value'])
            return conversao1(letras)

def p_main(p):
    'programa : INICIO operacoes FIM'
    f = open("interpretado.c", "w")
    f.write(f"#include <stdio.h>\n#include <string.h>\n\nint main(){{\n   {p[2]}\n   return 0;\n}}")
    f.close()

def p_operacao(p):
    '''
        operacao : declarando 
                  | definicaoValor
                  | definicaoResistor
                  | operacaoParalelo
                  | operacaoSerie
                  | conversao1
                  | conversao2
                  | conversaoGenerica
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
        declarando : tipo variaveis TERMINADOR_LINHA
    '''
    vars = p[2].split(',')
    if(p[1] == 'value'):
        p[0] = f'float {p[2]}{p[3]}\n   '
        for v in vars:
            Vars.append({'name': v, 'type': p[1], 'value': None})
    else:
        final = '_'
        for v in vars:
            Vars.append({'name': v, 'type': p[1], 'value': None})
            final += ','+v+'[10]'
        p[0] = f'char {final}{p[3]}\n   '

def p_var(p):
    '''
        variaveis : VARIAVEL
    '''
    p[0] = p[1]

def p_vars(p):
    '''
        variaveis : variaveis VIRGULA VARIAVEL
    '''
    p[0] = F'{p[1]}{p[2]}{p[3]}'

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
    id = existeVar(p[1])
    if  id == -1:
        print("Variavel não declarada!")
    if Vars[id]['type'] != "value":
        print("Tipo incorreto para conversao")
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
    id = existeVar(p[1])
    if  id == -1:
        print("Variavel não declarada!")
    if Vars[id]['type'] != "value":
        print("Tipo incorreto para conversao")
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

def p_conversao1(p):
    '''
        conversao1 : VARIAVEL ATRIBUICAO CONVERSAO_VALOR modeloResistor TERMINADOR_LINHA
    '''
    id = existeVar(p[1])
    if  id == -1:
        print("Variavel não declarada!")
    if Vars[id]['type'] != "value":
        print("Tipo incorreto para conversao")
    valorRes = conversao1(modeloResitor2vetor(p[4]))
    Vars[id]['value'] = valorRes
    Vars[id]['type'] = 'value'
    p[0] = f'{p[1]} = {valorRes}{p[5]}'

def p_conversao2(p):
    '''
        conversao2 : VARIAVEL ATRIBUICAO CONVERSAO_RESISTOR VALOR TERMINADOR_LINHA
    '''
    id = existeVar(p[1])
    if  id == -1:
        print("Variavel não declarada!")
    if Vars[id]['type'] != "resistor":
        print("Tipo incorreto para conversao")
    valorRes = conversao2(float(p[4]))
    Vars[id]['value'] = valorRes
    Vars[id]['type'] = 'resistor'
    p[0] = f'strcpy({p[1]},"{valorRes}"){p[5]}'

def p_conversaoGenerica(p):
    '''
        conversaoGenerica : VARIAVEL ATRIBUICAO conversao VARIAVEL TERMINADOR_LINHA
    '''
    id = existeVar(p[1])
    if  id == -1:
        print("Variavel não declarada!")
    tipo = 'value' if (p[3] == "re2va") else 'resistor'
    if Vars[id]['type'] != tipo:
        print("Tipo incorreto para conversao")
    id = existeVar(p[4])
    if(tipo == 'value'):
        valorRes = conversao1(modeloResitor2vetor(Vars[id]['value']))
        Vars[existeVar(p[1])]['value'] = valorRes
        p[0] = f'{p[1]} = {valorRes}{p[5]}'
    else:
        valorRes = conversao2(float(Vars[id]['value']))
        Vars[existeVar(p[1])]['value'] = valorRes
        p[0] = f'strcpy({p[1]},"{valorRes}"){p[5]}'

def p_conversao(p):
    '''
        conversao : CONVERSAO_RESISTOR 
                   | CONVERSAO_VALOR
    '''
    p[0] = p[1]

def p_mostrar(p):
    '''
        mostrar : MOSTRAR ABRE_COLCHETES variaveis FECHA_COLCHETES TERMINADOR_LINHA
    '''
    vars = p[3].split(',')
    p[0] = ''
    for v in vars:
        id = existeVar(v)
        if(id == -1):
            print("Variavel"+{v}+"nao existente")
        else:
            if(Vars[id]['type'] == 'value'):
                p[0] += f'printf("{v} = %.2f\\n",{v}){p[5]}\n   '
            else:
                p[0] += f'printf("{v} = %s\\n",{v}){p[5]}\n   '

parser = yacc.yacc()

from exemploCodigos import interpretar

result = parser.parse(interpretar)