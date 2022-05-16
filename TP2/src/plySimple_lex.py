from ast import arg
import ply.lex as lex
from helper import *

tokens = [
    'BLEX',
    'EOF',
    'LIT',
    'IGN',
    'TOK',
    'literals',
    'tokenList',
    'BLFUN',
    'funL',
    'BYACC',
    'PREC',
    'preceList',
    'TS',
    'tsList',
    'BGRAM',
    'EGRAM',
    'gram',
    'EFUNY',
    'BFUNY',
    'funY',
    'BPARSER',
    'instructions',
    'BCOM',
    'ECOM',
    'comm',
    ]

states = [
    ("lex", 'inclusive'),
    ("lexFun", 'inclusive'),
    ("yacc", 'inclusive'),
    ("yaccFun", 'inclusive'),
    ("grammar", 'inclusive'),
    ("parser", 'inclusive'),
    ("comment", 'exclusive')
    ]

t_ANY_ignore = " \t\n"

### TREATING COMMENTS ###
def t_ANY_BCOM(t):
    r'\<\#\>'
    t.lexer.begin("comment")
    return t

def t_ANY_ECOM(t):
    r'\>\#\<'
    t.lexer.begin("INITIAL")
    return t

def t_comment_comm(t):
    r'(:?\s*:?[A-z]+:?\s*)+'
    return t

### MARKER FOR EOF ###
def t_ANY_EOF(t):
    r'\$\$'
    return t

### PARSER INFORMATION AND INSTRUCTIONS ###
def t_yacc_BPARSER(t):
    r'%%\s*PARSER\s*%%'
    t.lexer.begin("parser")
    return t

def t_parser_instructions(t):
    r'.*parse(.*).*'
    return t

### YACC SECTION ###
def t_ANY_BYACC(t):
    r'%%\s*YACC\s*%%'
    t.lexer.begin("yacc")
    return t

def t_yacc_PREC(t):
    r'%\s*precedence\s*=\s*'
    return t

def t_yacc_preceList(t):
    r'\[\(.*\]'
    return t

def t_yacc_TS(t):
    r'%\s*ts\s*=\s*'
    return t

def t_yacc_tsList(t):
    r'\{\}'
    return t

### GRAMMAR ###
def t_yacc_BGRAM(t):
    r'/%\\'
    t.lexer.begin("grammar")
    return t

def t_grammar_EGRAM(t):
    r'/%%\\'
    t.lexer.begin("yacc")
    return t

def t_grammar_gram(t):
    r'(.*\{.*\})'
    return t

### YACC FUNCTIONS ###
def t_yacc_EFUNY(t):
    r'%\)'
    t.lexer.begin("yaccFun")
    return t

def t_yaccFun_EFUNY(t):
    r'\(%'
    t.lexer.begin("yacc")
    return t

def t_yaccFun_funY(t):
    r'def .*'
    return t

### LEX SECTION ###
def t_ANY_BLEX(t):
    r'%%\s*LEX\s*%%'
    t.lexer.begin("lex")
    return t

def t_lex_LIT(t):
    r'%\s*literals\s*=\s*'
    return t

def t_lex_literals(t):
    r'\".*\"'
    return t

def t_lex_IGN(t):
    r'%\s*ignore\s*=\s*'
    return t

def t_lex_TOK(t):
    r'%\s*tokens\s*=\s*'
    return t

def t_lex_tokenList(t):
    r'\[(\'*.*\')+\]'
    return t

### LEX FUNCTIONS ###
def t_lex_BLFUN(t):
    r'\s*%\)\s*'
    t.lexer.begin("lexFun")
    return t

def t_lexFun_funL(t):
    r'.*(return|error).*'
    t.lexer.begin("lex")
    return t

### ERRO FUNCTION ###
def t_ANY_error(t):
    print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
    t.lexer.skip(1)

lexer = lex.lex()

"""import sys
files = sys.argv[1:]

for file_name in files:
    try:
        lines = open_file(file_name)
    except FileNotFoundError:
        lines = ''
        print("\033[91m[ERROR] file "+ file_name + " not found.\033[0m")
    for line in lines:
        lexer.input(line)
        for tok in lexer:
            print(tok)
    print("###### END LEX PROCESSING ######")"""
