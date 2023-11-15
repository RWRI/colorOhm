%{
	#include <stdio.h>
	#include <math.h> 
	#include <stdlib.h>
	#include <string.h>
	#include "tipo.h"
	#define YYERROR_VERBOSE
	// extern "C" int yylex(void);
	// extern "C" int yyparse();
	// extern "C" FILE *yyin;
	void yyerror(const char *s);
	void loc_para_c(tipo *raiz);
	void sub_loc_para_c(tipo *raiz);
	FILE *entrada, *saida;
	tipo *raiz;
	char *var_nome;   
%}

%union{
	tipo *pnt;
}

%token <pnt> INICIO
%token <pnt> FIM
%token <pnt> TERMINADOR_LINHA
%token <pnt> ATRIBUICAO
%token <pnt> PARALELO
%token <pnt> SERIE
%token <pnt> VIRGULA
%token <pnt> PONTO
%token <pnt> ABRE_COLCHETES
%token <pnt> FECHA_COLCHETES
%token <pnt> MOSTRAR
%token <pnt> COR
%token <pnt> VALOR_RESISTOR
%token <pnt> TIPO
%token <pnt> VARIAVEL
%token <pnt> VALOR
%token <pnt> CONVERSAO_VALOR
%token <pnt> CONVERSAO_RESISTOR
%token <pnt> CONVERSAO

%type <pnt> modeloResistor
%type <pnt> declarando
%type <pnt> definicaoValor
%type <pnt> defincaoResistor
%type <pnt> conversao1
%type <pnt> conversao2
%type <pnt> conversaoGenerica
%type <pnt> operacaoSerie
%type <pnt> operacaoParalelo
%type <pnt> mostrando
%type <pnt> operacoes
%type <pnt> algoritmo