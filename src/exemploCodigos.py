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
        res = [m,g,a,d];
        show[re, res];
    endohm
'''

codigo2 = '''
    ohm 
        value va;
        va = 3.75;
        resistor re;
        re = [y,b,v,w];
        show[va, re];
    endohm
'''

codigo3 = '''
    ohm 
        value v1, v2, v3;
        v1 = 2;
        v2 = 3;
        v3 = v1:v2;
        show[v1, v2, v3];
    endohm
'''

codigo4 = '''
    ohm 
        value v1, v2, v3, v4;
        v1 = 2;
        v2 = 3;
        v3 = 3;
        v4 = v1:v2:v3;
        show[v1, v2, v3, v4];
    endohm
'''

codigo5 = '''
    ohm 
        value v1, v2, v3;
        v1 = 2;
        v2 = 2;
        v3 = v1|v2;
        show[v1, v2, v3];
    endohm
'''

codigo6 = '''
    ohm 
        value v1, v2, v3, v4;
        v1 = 200;
        v2 = 200;
        v3 = 100;
        v4 = v1|v2|v3;
        show[v1, v2, v3, v4];
    endohm
'''

codigo7 = '''
    ohm
        value r1, r3;
        resistor r2, r4;
        r1 =  re2va [r,r,r];
        r2 =  va2re 220;
        r4 = va2re r1;
        r3 = re2va r2;
        show[r1, r4];
        show[r2, r3];
    endohm
'''

codigo8 = '''
    ohm
        resistor r1, r2;
        value r3, r4;
        r1 = [r,k,m];
        r2 = [r,k,m];
        r3 = r1 : r2;
        r4 = r1 | r2;
        show[r3, r4];
    endohm
'''

codigoDocumentacao = '''
    ohm
        value r1, r2, r3, rz;
        resistor rc, rb, ra;
        
        r1 = 200;
        rc = [m,m,r];
        
        r2 = re2va [g,r,m];
        ra = va2re 1500;
        rb = va2re r1; 
   
        r3 = r1 : r2;
        rz = rc | rb | ra; 

        show[r1,rc,r2,ra,rb,r3,rz];

    endohm
'''

interpretar = codigoDocumentacao
