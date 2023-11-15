%{
    #include<stdio.h>
%}

%option noyywrap

letra[a-zA-Z]
digito[0-9]
cor(k|m|r|o|y|g|d|v|a|w)
resistor(resistor)
valorResistor(value)
conversaoValor(\(value\))
conversaoResistor(\(resistor\))
ponto(.)

%%
"ohm"           {return INICIO;}
"endohm"        {return FIM;}
";"             {return TERMINADOR_LINHA;}
"="             {return ATRIBUICAO;}
"|"             {return PARALELO;}
":"             {return SERIE;}
","             {return VIRGULA;}
"["             {return ABRE_COLCHETES;}
"]"             {return FECHA_COLCHETES;}
"show"          {return MOSTRAR;}

({cor})                                 {return COR;}
({valorResistor})                       {return VALOR_RESISTOR;}
({resistor}|{valorResistor})             {return TIPO;}
({letra}+({digito}|{letra})*)           {return VARIAVEL;}
({digito}+)|({digito}+{ponto}{digito}+) {return VALOR;}
({conversaoValor})                      {return CONVERSAO_VALOR;}
({conversaoResistor})                   {return CONVERSAO_RESISTOR;}
({conversaoValor}|{conversaoResistor})  {return CONVERSAO;}

[ \t\n]            ;
.                  {return *yytext;} 
%%

int yywrap(void){
    return 1;
}
    
