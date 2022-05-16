
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BCOM BFUNL BFUNY BGRAM BLEX BPARSER BYACC ECOM EFUNL EFUNY EGRAM EOF IGN LIT PREC TOK TS comm funL funY gram ig instructions literals preceList tokenList tsListPly-Simple : Lex EOFLex : BLEX Vars FunsVars : Vars VarVars : Var : LIT literalsVar : IGN igVar : TOK tokenListFuns : Funs Fun EFUNLFuns : Fun : BFUNL funL'
    
_lr_action_items = {'BLEX':([0,],[3,]),'$end':([1,4,],[0,-1,]),'EOF':([2,3,5,6,7,13,14,15,16,],[4,-4,-9,-2,-3,-5,-6,-7,-8,]),'LIT':([3,5,7,13,14,15,],[-4,8,-3,-5,-6,-7,]),'IGN':([3,5,7,13,14,15,],[-4,9,-3,-5,-6,-7,]),'TOK':([3,5,7,13,14,15,],[-4,10,-3,-5,-6,-7,]),'BFUNL':([3,5,6,7,13,14,15,16,],[-4,-9,12,-3,-5,-6,-7,-8,]),'literals':([8,],[13,]),'ig':([9,],[14,]),'tokenList':([10,],[15,]),'EFUNL':([11,17,],[16,-10,]),'funL':([12,],[17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Ply-Simple':([0,],[1,]),'Lex':([0,],[2,]),'Vars':([3,],[5,]),'Funs':([5,],[6,]),'Var':([5,],[7,]),'Fun':([6,],[11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Ply-Simple","S'",1,None,None,None),
  ('Ply-Simple -> Lex EOF','Ply-Simple',2,'p_plySimple_BLEX','plySimple_yacc.py',7),
  ('Lex -> BLEX Vars Funs','Lex',3,'p_Lex','plySimple_yacc.py',10),
  ('Vars -> Vars Var','Vars',2,'p_Vars_notEmpty','plySimple_yacc.py',13),
  ('Vars -> <empty>','Vars',0,'p_Vars_Empty','plySimple_yacc.py',16),
  ('Var -> LIT literals','Var',2,'p_Var_Literals','plySimple_yacc.py',19),
  ('Var -> IGN ig','Var',2,'p_Var_Ignore','plySimple_yacc.py',22),
  ('Var -> TOK tokenList','Var',2,'p_Var_ListTok','plySimple_yacc.py',25),
  ('Funs -> Funs Fun EFUNL','Funs',3,'p_Funs_notEmpty','plySimple_yacc.py',28),
  ('Funs -> <empty>','Funs',0,'p_Funs_Empty','plySimple_yacc.py',31),
  ('Fun -> BFUNL funL','Fun',2,'p_Fun','plySimple_yacc.py',34),
]
