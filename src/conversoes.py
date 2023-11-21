import math

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
            
print(conversao2(9))