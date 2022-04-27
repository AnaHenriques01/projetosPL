import re
from typing import List


# DEVOLVE UMA LISTA COM O CONTEÚDO DO FILE LEX E OUTRA LISTA COM O CONTEÚDO DO FILE YACC
def get_lex_yacc(lines: List[str]):

    pos = 0
    lines_for_LEX = []                      # guarda todo o conteúdo para o file lex
    lines_for_YACC = []                     # guarda todo o conteúdo para o file yacc

    for line in lines:
        if re.search(r'LEX',line):
            pos_lex = pos                   # pos em que começa o conteúdo para o file lex
        if re.search(r'YACC',line):
            pos_yacc = pos                  # pos em que começa o conteúdo para o file yacc
        pos = pos + 1

    for line in lines[pos_lex+1:pos_yacc]:
        if not re.search(r'^$',line) and not re.match(r'^%+$',line):          # remove empty lines or lines like %%
            lines_for_LEX.append(line)
    
    for line in lines[pos_yacc+1:]:
        if not re.search(r'^$',line) and not re.match(r'^%+$',line):          # remove empty lines or lines like %%
            lines_for_YACC.append(line)
    
    return lines_for_LEX, lines_for_YACC


# ABRE UM FICHEIRO E DEVOLVE UMA LISTA COM O SEU CONTEÚDO
def open_file():
    input_name = input("[CSV] Insert file name (extension included): ")

    try:	
        file = open("../input/"+input_name)
    except OSError:
        print(f"[ERROR] Can't locate CSV file \"{input_name}\".\n")
        input("[PRESS ENTER TO CONTINUE]")
        return -1

    if file:
        lines = file.read().splitlines()
        print("[FILE] Opened successfully.")
        input("[PRESS ENTER TO CONTINUE]")
        file.close()
        return input_name, lines


# CRIA E ESCREVE NO FILE LEX
def write_file_lex(input_name:str, res0: str):

    imports = "import ply.lex as lex"
    res = imports + "\n\n" + res0

    input_name = re.sub(r'\.(.*)',r'',input_name)
    outputFile = open("../output/"+f'{input_name}_lex.py','w')
    outputFile.write(res)
    outputFile.close

    print("[FILE] Translated LEX successfully.")
    input("[PRESS ENTER TO CONTINUE]")