import ply.lex as lex

# List of token names.   This is always required
tokens = (
  'L_PAREN',
  'R_PAREN',
  'L_PAREN_C',
  'R_PAREN_C',
  'L_PAREN_R',
  'R_PAREN_R',

  'SEP',
  'FIM',
  'IGUAL',
  'MAIOR',
  'MENOR',
  'MULT',
  'DIV',
  'MAIS',
  'MENOS',
  'INTER',

  'NUM',
  'TYPE',
  'FUNC',
  'PROG', 
  'FOR',
  'IN',
  'WHILE',
  'ID'
)

# Regular expression rules for simple tokens   
t_L_PAREN = r'\{'
t_R_PAREN = r'\}'
t_L_PAREN_C = r'\('
t_R_PAREN_C = r'\)'
t_L_PAREN_R = r'\['
t_R_PAREN_R = r'\]'
t_SEP = r','
t_FIM = r';'
t_IGUAL = r'='
t_MAIOR = r'>'
t_MENOR = r'<'
t_MULT = r'\*'
t_DIV = r'\/'
t_MAIS = r'\+'
t_MENOS = r'\-'
t_INTER = r'\.\.'
t_NUM = r'\d+'
t_TYPE = r'int|double|float|long|char|string|bool'
t_FUNC = r'function'
t_PROG = r'program'
t_FOR = r'for'
t_IN = r'in'
t_WHILE = r'while'
t_ID = r'\w+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore multi-line comments
def t_ignore_MULTICOM(t):
    r'/\*(.|\n)*?\*/'
    pass

#Ignore comments
t_ignore_COM = r'//.*'

# Ignore spaces and tabs
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
exemplo1 = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''

exemplo2 = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''
def main():
# Give the lexer some input
  lexer.input(exemplo1)

  print("\n" + "Exemplo 1" + "\n")

  for tok in lexer:
      print(tok)
      #print(tok.type, tok.value, tok.lineno, tok.lexpos)

  lexer.input(exemplo2)

  print("\n" + "Exemplo 2" + "\n")

  for tok in lexer:
      print(tok)

main()