import math

def switchc1(case):
        if case == 'k':
            return 0
        if case == 'm':
            return 1
        if case == 'r':
            return 2
        if case == 'o':
            return 3
        if case == 'y':
            return 4
        if case == 'g':
            return 5
        if case == 'b':
            return 6
        if case == 'v':
            return 7
        if case == 'a':
            return 8
        if case == 'w':
            return 9
        if case == 'd':
            return -1

def switch(case):
        if case == 0:
            return 'k'
        if case == 1:
            return 'm'
        if case == 2:
            return 'r'
        if case == 3:
            return 'o'
        if case == 4:
            return 'y'
        if case == 5:
            return 'g'
        if case == 6:
            return 'b'
        if case == 7:
            return 'v'
        if case == 8:
            return 'a'
        if case == 9:
            return 'w'

def conversao1(p):
    
    valor = 0

    if len(p)== 3:
        valor = switchc1(p[0])*10
        valor = valor + switchc1(p[1])
        valor = valor*(10**(switchc1(p[2])))
        

    if len(p) == 4:
        valor = switchc1(p[0])*100
        valor = valor + switchc1(p[1])*10
        valor = valor + switchc1(p[2])
        valor = valor*(10**(switchc1(p[3])))

    return valor

def conversao2(p):
    if p>9:
        count = 0
        n = math.trunc(p)
        quantDigito = math.trunc(math.log10(n) + 1)
        divisor = 10 ** (quantDigito-2)
        valor = math.trunc(n/divisor)
        
        faixa2 = math.trunc(valor%10)
        faixa1 = math.trunc(valor/10)
        faixa3 = quantDigito-2
    
        faixa1 = switch(faixa1)
        faixa2 = switch(faixa2)
        faixa3 = switch(faixa3)
    elif p<1:
        faixa1 = switch(0)
        faixa2 = switch(0)
        faixa3 = switch(0)
    else:
        n = math.trunc(p)
        quantDigito = math.trunc(math.log10(n) + 1)
        divisor = 10 ** (quantDigito-2)
        valor = math.trunc(n/divisor)
        
        faixa2 = math.trunc(valor%10)
        faixa1 = math.trunc(valor/10)
        
        faixa1 = switch(faixa1)
        faixa2 = switch(faixa2)
        faixa3 = 'd'     

    return '['+ faixa1 + ',' + faixa2 + ',' + faixa3 +']'

def modeloResitor2vetor(mod):
    caracteres = len(mod)-1
    mod = mod[1:caracteres]
    letras = mod.split(',')
    return letras