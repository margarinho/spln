from lark import Lark, Transformer, v_args
import re
from tabulate import tabulate

gramatica = r"""
start: (PAR_COM_PARENTESIS|pt_tt_line|pt_line|tt_line|UNKOWN_LINE)*
pt_tt_line: pt_line tt_line 
pt_line: PT_LINE UNKOWN_LINE
tt_line: TETUM_LINE UNKOWN_LINE

PAR_COM_PARENTESIS.2: /(\b\w+\b )+\(.+\)/

PT_LINE.3: /PORTUGUÊS: .*/ 
TETUM_LINE.3: /TETUM: .*/ 

FIG.3: /Figura \d+\- (\b\w+\b)+\(.+\)/

UNKOWN_LINE.1: /.+/

%import common.WS
%ignore WS
"""

ex = r"""
Secante (Sekante) ...................................................................................................................... 115
Segmento de Reta (Segmentu Reta) .......................................................................................... 116
Semicírculo (Semisírkulu)......................................................................................................... 116
Semireta (Semireta) ................................................................................................................... 116
Seno (Senu) ............................................................................................................................... 117
Símbolo (Símbolu) .................................................................................................................... 117
Simplificação de Radicais (Simplifikasaun hosi Radikál sira).................................................. 118
Sinais (Sinál Sira) ...................................................................................................................... 119
Sistema (Sistema) ...................................................................................................................... 119
Subtração (Subtrasaun / Hasai / Kuran) .................................................................................... 119
Subtraendo (Subtraendu / Hamenus)......................................................................................... 119
Tangente (Tanjente) .................................................................................................................. 120
Tangram (Tangram) .................................................................................................................. 120
Teorema (Teorema) ................................................................................................................... 121
"""
processador = Lark(gramatica, parser='lalr')
tree = processador.parse(ex)
#print(tree.pretty())


@v_args(inline=True)
class Tranformer_intervals(Transformer):    
    def start(self,*t):
        return t
    
    def PAR_COM_PARENTESIS(self, tok):
        return ('pt-tt', re.split(r' *[(|)]',tok.value)[:-1])
    
    def PT_LINE(self,tok):
        return ('pt', tok.value.slipt(":")[-1:])
    
    def pt_line(self,tok, *l):
        return ('pt', tok[1] + '\n' + '\n'.join(tok))
    
    def TETUM_LINE(self,tok):
        return ('tt', tok.value.slipt(":")[-1:])
    
    def tt_line(self,tok, *l):
        return ('tt', tok[1] + '\n' + '\n'.join(tok))
    
    def pt_tt_line(self,tok1,tok2):
        return ('pt-tt', [tok1,tok2])
    def FIG(self,tok):
        return ('fig', tok.value)
    def UNKOWN_LINE(self,tok):
        return tok.value

tree = Tranformer_intervals().transform(tree)

unknown = [x for x in tree if isinstance(x, str)]
print('UNKNOWN: ', unknown)

data = [x[1] for x in tree if not isinstance(x, str)]

print('\nDATA: ')
print(tabulate(data))