#ifndef _NO_H_
#define _NO_H_

struct tipoNo
{
    int token;
    double val;
    char nome[256];
    struct tipoNo *esq, *dir, *prox, *prox1, *prox2, *prox3;
};

typedef struct tipoNo tipoNo;

#endif