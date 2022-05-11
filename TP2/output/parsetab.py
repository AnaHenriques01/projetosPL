
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "FIM numZ : Exp FIMExp : '(' '+' Lista Exp ')'Exp : '(' '*' Lista Exp ')'Exp : numLista : Lista ExpLista : Exp"
    
_lr_action_items = {'(':([0,4,6,7,8,9,10,11,12,13,14,],[3,-4,3,3,3,-6,3,-5,-5,-2,-3,]),'num':([0,4,6,7,8,9,10,11,12,13,14,],[4,-4,4,4,4,-6,4,-5,-5,-2,-3,]),'$end':([1,5,],[0,-1,]),'FIM':([2,4,13,14,],[5,-4,-2,-3,]),'+':([3,],[6,]),'*':([3,],[7,]),')':([4,11,12,13,14,],[-4,13,14,-2,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Z':([0,],[1,]),'Exp':([0,6,7,8,10,],[2,9,9,11,12,]),'Lista':([6,7,],[8,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Z","S'",1,None,None,None),
  ('Z -> Exp FIM','Z',2,'p_Z_p1','example4_yacc.py',27),
  ('Exp -> ( + Lista Exp )','Exp',5,'p_Exp_p2','example4_yacc.py',31),
  ('Exp -> ( * Lista Exp )','Exp',5,'p_Exp_p3','example4_yacc.py',35),
  ('Exp -> num','Exp',1,'p_Exp_p4','example4_yacc.py',39),
  ('Lista -> Lista Exp','Lista',2,'p_Lista_p5','example4_yacc.py',43),
  ('Lista -> Exp','Lista',1,'p_Lista_p6','example4_yacc.py',47),
]