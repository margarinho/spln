from lark import Lark, Transformer

grammar = r"""
start: definition+

definition: "defr" WORD ":" NEWLINE expression+

expression: (simple | complex) NEWLINE

simple: TERM TRANSFORM TERM
complex: TERM TRANSFORM_E /[^\n]+/

TERM: WORD | /[^ ]+/

TRANSFORM: "==>"
TRANSFORM_E: "=e=>"

%import common.NEWLINE
%import common.WS
%import common.WORD 
%ignore WS
"""

example = """
defr one:
    the ==> o
    cat ==> gato

defr two:
    chicken ==> galinha
    (\\w+) =e=> lambda x: dicionario.get(x[1], x[1])
"""

class Transformer(Transformer):
    def start(self, items):
        output = ""
        for definition in items:
            output += definition
        return output
    
    def definition(self,items):
        name, _, *exprs = items
        output= f"def transform_{name}(t):\n"
        for e in exprs:
            output += f"\t{e}\n"
        output += "return t\n"
        return output
    
    def expression(self,items):
        expression,_ = items
        return expression
    
    def simple(self,items):
        term1, _, term2  = items
        return f"t = re.sub/r'\\b{term1}\\b','{term2}',t)"
    
    def complex(self,items):
        term1,_, term2 = items
        return f"t = re.sub/r'\\b{term1}\\b','{term2}',t)"

parser = Lark(grammar, parser='lalr', transformer=Transformer())

python_code = parser.parse(example)
print(python_code)