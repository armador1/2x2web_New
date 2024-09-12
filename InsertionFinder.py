import _2x2Main as main
from TranslatedSolver import TranslateStList as tr, fixCorner
import ast
a = open('EG.txt')
rots = ['x2','z','x3','','z3','x']
for str in a:
    st = ast.literal_eval(str)
    stt = tr(st)
    for i in range(0,6):
        fp = i
        if stt[4*i]==stt[4*i+1] and stt[4*i]==stt[4*i+2] and stt[4*i]==stt[4*i+3]:
            break

    rot = getattr(main,rots(fp))
    newst = fixCorner(tr(main.s2sList(rot(main.sList2s(st)))))
    
    