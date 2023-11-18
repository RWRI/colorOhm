codigo0 = '''
    ohm 
        value va;
        va = 2.79;
        show[va];
    endohm
'''

codigo1 = '''
    ohm 
        resistor re, res;
        re = [r,k,o];
        res = [r,k,o];
        show[re];
        show[res];
    endohm
'''

codigo2 = '''
    ohm 
        value v1, v2, v3;
        v1 = 2;
        v2 = 3;
        v3 = v1:v2;
        show[v3];
    endohm
'''

codigo3 = '''
    ohm 
        value v1, v2, v3, v4;
        v1 = 2;
        v2 = 3;
        v3 = 3;
        v4 = v1:v2:v3;
        show[v4];
    endohm
'''

codigo4 = '''
    ohm 
        value v1, v2, v3;
        v1 = 2;
        v2 = 2;
        v3 = v1|v2;
        show[v3];
    endohm
'''

codigo5 = '''
    ohm 
        value v1, v2, v3, v4;
        v1 = 200;
        v2 = 200;
        v3 = 100;
        v4 = v1|v2|v3;
        show[v4];
    endohm
'''

interpretar = codigo5