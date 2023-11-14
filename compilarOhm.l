%{
    #include<stdio.h>
%}

%option noyywrap

inicio(ohm)
fim(endohm)
terminadorLinha(;)
letra[a-zA-Z]
digito[0-9]
atribuicao(=)
paralelo(\|)
serie(:)
conversaoValor(\(value\))
conversaoResistor(\(resistor\))
virgula(,)
ponto(.)
abreColchetes(\[)
fechaColchetes(\])
resistor(resistor)
valorResitor(value)
cor(k|m|r|o|y|g|d|v|a|w)
mostrar(show)

tipo({resistor}|{valorResitor})
variavel({letra}+({digito}|{letra})*)
valor(({digito}+)|({digito}+{ponto}{digito}+))
conversao({conversaoValor}|{conversaoResistor})

modeloResistor({abreColchetes}{cor}{virgula}{cor}{virgula}({cor}|({cor}{virgula}{cor})){fechaColchetes})
declarando({tipo}{variavel}({virgula}{variavel})*{terminadorLinha})
definicaoValor({variavel}{atribuicao}{valor}{terminadorLinha})
defincaoResistor({variavel}{atribuicao}{valorResitor}{terminadorLinha})
conversao1({variavel}{atribuicao}{conversaoValor}{modeloResistor}{terminadorLinha})
conversao2({variavel}{atribuicao}{conversaoResistor}{valor}{terminadorLinha})
conversaoGenerica({variavel}{atribuicao}{conversao}{variavel}{terminadorLinha})
operacaoSerie({variavel}{atribuicao}{variavel}({serie}{variavel})+{terminadorLinha})
operacaoParalelo({variavel}{atribuicao}{variavel}({paralelo}{variavel})+{terminadorLinha})
mostrando({mostrar}{abreColchetes}{variavel}({virgula}{variavel})*{fechaColchetes}{terminadorLinha})

operacoes({declarando}|{definicaoValor}|{defincaoResistor}|{conversao1}|{conversao2}|{conversaoGenerica}|{operacaoSerie}|{operacaoParalelo})
algoritmo({inicio}{operacoes}+{fim})


%%
{inicio} {printf("'%s' -> INICIO\n",yytext);}
{fim} {printf("'%s' -> FIM\n",yytext);}
{tipo} {printf("'%s' -> TIPO\n",yytext);}
{atribuicao} {printf ("'%s' -> ATRIBUIÇÃO\n",yytext);}
{terminadorLinha} {printf("'%s' -> TERMINADOR_LINHA\n",yytext);}
{variavel} {printf("'%s' -> VARIAVEL\n",yytext);}
{valor} {printf("'%s' -> VALOR\n",yytext);}
{definicaoValor} {printf("'%s' -> DEFINICAO_VALOR\n",yytext);}
{declarando} {printf("'%s' -> DECLARANDO\n",yytext);}
{conversaoValor} {printf("'%s' -> CONVERSAO_VALOR\n",yytext);}
{modeloResistor} {printf("'%s' -> MODELO_RESISTOR\n",yytext);}
{algoritmo} {printf("'%s' -> ALGORITMO\n",yytext);}
%%

int main(){
    yylex();
    return 0;
}
    
