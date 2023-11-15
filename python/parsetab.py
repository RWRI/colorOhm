
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_COLCHETES ATRIBUICAO CONVERSAO_RESISTOR CONVERSAO_VALOR COR FECHA_COLCHETES FIM INICIO MOSTRAR PARALELO PONTO RESISTOR SERIE TERMINADOR_LINHA VALOR VALOR_RESISTOR VARIAVEL VIRGULAprograma : INICIO operacoes FIM\n        operacao : declarando \n                  | definicaoValor\n                  | operacaoParalelo\n                  | operacaoSerie\n                  | mostrar\n    \n        operacoes : operacao \n    \n        operacoes : operacoes operacao \n    \n        tipo : RESISTOR \n             | VALOR_RESISTOR\n    \n        declarando : tipo VARIAVEL TERMINADOR_LINHA\n    \n        definicaoValor : VARIAVEL ATRIBUICAO VALOR TERMINADOR_LINHA\n    \n        operacaoParalelo : VARIAVEL ATRIBUICAO VARIAVEL PARALELO VARIAVEL TERMINADOR_LINHA\n    \n        operacaoSerie : VARIAVEL ATRIBUICAO VARIAVEL SERIE VARIAVEL TERMINADOR_LINHA\n    \n        mostrar : MOSTRAR ABRE_COLCHETES VARIAVEL FECHA_COLCHETES TERMINADOR_LINHA\n    '
    
_lr_action_items = {'INICIO':([0,],[2,]),'$end':([1,15,],[0,-1,]),'VARIAVEL':([2,3,4,5,6,7,8,9,10,13,14,16,18,19,20,24,25,26,30,31,32,],[11,11,-7,-2,-3,-4,-5,-6,17,-9,-10,-8,21,23,-11,28,29,-12,-15,-13,-14,]),'MOSTRAR':([2,3,4,5,6,7,8,9,16,20,26,30,31,32,],[12,12,-7,-2,-3,-4,-5,-6,-8,-11,-12,-15,-13,-14,]),'RESISTOR':([2,3,4,5,6,7,8,9,16,20,26,30,31,32,],[13,13,-7,-2,-3,-4,-5,-6,-8,-11,-12,-15,-13,-14,]),'VALOR_RESISTOR':([2,3,4,5,6,7,8,9,16,20,26,30,31,32,],[14,14,-7,-2,-3,-4,-5,-6,-8,-11,-12,-15,-13,-14,]),'FIM':([3,4,5,6,7,8,9,16,20,26,30,31,32,],[15,-7,-2,-3,-4,-5,-6,-8,-11,-12,-15,-13,-14,]),'ATRIBUICAO':([11,],[18,]),'ABRE_COLCHETES':([12,],[19,]),'TERMINADOR_LINHA':([17,22,27,28,29,],[20,26,30,31,32,]),'VALOR':([18,],[22,]),'PARALELO':([21,],[24,]),'SERIE':([21,],[25,]),'FECHA_COLCHETES':([23,],[27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'operacoes':([2,],[3,]),'operacao':([2,3,],[4,16,]),'declarando':([2,3,],[5,5,]),'definicaoValor':([2,3,],[6,6,]),'operacaoParalelo':([2,3,],[7,7,]),'operacaoSerie':([2,3,],[8,8,]),'mostrar':([2,3,],[9,9,]),'tipo':([2,3,],[10,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INICIO operacoes FIM','programa',3,'p_main','colorOhm_yacc.py',16),
  ('operacao -> declarando','operacao',1,'p_operacao','colorOhm_yacc.py',23),
  ('operacao -> definicaoValor','operacao',1,'p_operacao','colorOhm_yacc.py',24),
  ('operacao -> operacaoParalelo','operacao',1,'p_operacao','colorOhm_yacc.py',25),
  ('operacao -> operacaoSerie','operacao',1,'p_operacao','colorOhm_yacc.py',26),
  ('operacao -> mostrar','operacao',1,'p_operacao','colorOhm_yacc.py',27),
  ('operacoes -> operacao','operacoes',1,'p_operacao_unica','colorOhm_yacc.py',33),
  ('operacoes -> operacoes operacao','operacoes',2,'p_operacoes','colorOhm_yacc.py',39),
  ('tipo -> RESISTOR','tipo',1,'p_tipo','colorOhm_yacc.py',45),
  ('tipo -> VALOR_RESISTOR','tipo',1,'p_tipo','colorOhm_yacc.py',46),
  ('declarando -> tipo VARIAVEL TERMINADOR_LINHA','declarando',3,'p_declarando','colorOhm_yacc.py',52),
  ('definicaoValor -> VARIAVEL ATRIBUICAO VALOR TERMINADOR_LINHA','definicaoValor',4,'p_definicaoValor','colorOhm_yacc.py',60),
  ('operacaoParalelo -> VARIAVEL ATRIBUICAO VARIAVEL PARALELO VARIAVEL TERMINADOR_LINHA','operacaoParalelo',6,'p_operacaoParalelo','colorOhm_yacc.py',69),
  ('operacaoSerie -> VARIAVEL ATRIBUICAO VARIAVEL SERIE VARIAVEL TERMINADOR_LINHA','operacaoSerie',6,'p_operacaoSerie','colorOhm_yacc.py',76),
  ('mostrar -> MOSTRAR ABRE_COLCHETES VARIAVEL FECHA_COLCHETES TERMINADOR_LINHA','mostrar',5,'p_mostrar','colorOhm_yacc.py',82),
]
