import copy
import re
import ast


def Solved():
    # Gives the solved state in the notation that uses the rest of functions
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]


def s2sList(st):
    # This function gets a state as an argument and returns a equivalent list of integers (instead of the list of
    # lists that we use as states)
    s = copy.deepcopy(st)
    slist = []
    for i in s:
        for j in i:
            slist.append(j)
    return slist


def sList2s(slist1):
    # This function gets a list of integers and transforms it to a state (this function is the inverse of s2sList())
    slist = copy.deepcopy(slist1)
    s = []
    for i in [0, 3, 6, 9, 12, 15, 18, 21]:
        s.append([slist[i], slist[i + 1], slist[i + 2]])
    return s


def Sol2Scr(sol):
    sp_sol = sol.split(' ')
    sp_sol.reverse()
    scr = [0] * len(sp_sol)
    k = 0
    for i in sp_sol:
        if "2" in i:
            scr[k] = i
        elif "'" in i:
            scr[k] = i.replace("'", '')
        else:
            i = i + "3"
            scr[k] = i
        k = k + 1
    return scr

def U(st):
    # Applies an U move to a given state
    s = copy.deepcopy(st)
    aux = s[0]
    for i in range(0,3):
        s[i] = s[i+1]
    s[3] = aux
    return(s)
def U2(st):
    # Applies an U2 move to a given state 
    s = copy.deepcopy(st)
    return(U(U(s)))
def U3(st):
    # Applies an U' move to a given state
    s = copy.deepcopy(st)
    return(U(U2(s)))

def R(st):
    # Applies a R move to a given state
    s = copy.deepcopy(st)
    return(z(U(z3(s))))
def R2(st):
    # Applies a R2 move to a given state
    s = copy.deepcopy(st)
    return(R(R(s)))
def R3(st):
    # Applies a R' move to a given state
    s = copy.deepcopy(st)
    return(R(R2(s)))

def F(st):
    # Applies a F move to a given state
    s = copy.deepcopy(st)
    aux = s[0][1]
    s[0][1] = s[4][2]
    s[4][2] = s[5][1]
    s[5][1] = s[1][2]
    s[1][2] = aux

    aux = s[0][0]
    s[0][0] = s[4][1]
    s[4][1] = s[5][0]
    s[5][0] = s[1][1]
    s[1][1] = aux

    aux = s[0][2]
    s[0][2] = s[4][0]
    s[4][0] = s[5][2]
    s[5][2] = s[1][0]
    s[1][0] = aux
    return(s)
def F2(st):
    # Applies a F2 move to a given state
    s = copy.deepcopy(st)
    return(F(F(s)))
def F3(st):
    # Applies a F' move to a given state
    s = copy.deepcopy(st)
    return(F(F2(s)))

# Rotations

def x(st):
    # Applies a x rotation to a given state
    s = copy.deepcopy(st)
    aux = s[0][0]
    s[0][0] = s[4][2]
    s[4][2] = s[7][0]
    s[7][0] = s[3][2]
    s[3][2] = aux
    aux = s[0][1]
    s[0][1] = s[4][0]
    s[4][0] = s[7][1]
    s[7][1] = s[3][0]
    s[3][0] = aux
    aux = s[0][2]
    s[0][2] = s[4][1]
    s[4][1] = s[7][2]
    s[7][2] = s[3][1]
    s[3][1] = aux
    aux = s[1][0]
    s[1][0] = s[5][1]
    s[5][1] = s[6][0]
    s[6][0] = s[2][1]
    s[2][1] = aux
    aux = s[1][2]
    s[1][2] = s[5][0]
    s[5][0] = s[6][2]
    s[6][2] = s[2][0]
    s[2][0] = aux
    aux = s[1][1]
    s[1][1] = s[5][2]
    s[5][2] = s[6][1]
    s[6][1] = s[2][2]
    s[2][2] = aux
    return s

def x2(st):
    # Applies a x2 rotation to a given state
    s = copy.deepcopy(st)
    return(x(x(s)))
def x3(st):
    # Applies a x' rotation to a given state
    s = copy.deepcopy(st)
    return(x(x2(s)))

def y(st):
    # Applies a y rotation to a given state
    s = copy.deepcopy(st)
    return(x2(U3(x2(U(s)))))
def y2(st):
    # Applies a y2 rotation to a given state
    s = copy.deepcopy(st)
    return(y(y(s)))
def y3(st):
    # Applies a y' rotation to a given state
    s = copy.deepcopy(st)
    return(y(y2(s)))

def z(st):
    # Applies a z rotation to a given state
    s = copy.deepcopy(st)
    return(x2(F3(x2(F(s)))))
def z2(st):
    # Applies a z2 rotation to a given state
    s = copy.deepcopy(st)
    return(z(z(s)))
def z3(st):
    # Applies a z' rotation to a given state
    s = copy.deepcopy(st)
    return(z(z2(s)))

def L(st):
    # Applies a L move to a given state
    s = copy.deepcopy(st)
    return(y2(R(y2(s))))
def L2(st):
    # Applies a L2 move to a given state
    s = copy.deepcopy(st)
    return(L(L(s)))
def L3(st):
    # Applies a L' move to a given state
    s = copy.deepcopy(st)
    return(L(L2(s)))

def B(st):
    # Applies a B move to a given state
    s = copy.deepcopy(st)
    return(y2(F(y2(s))))
def B2(st):
    # Applies a B2 move to a given state
    s = copy.deepcopy(st)
    return(B(B(s)))
def B3(st):
    # Applies a b' move to a given state
    s = copy.deepcopy(st)
    return(B(B2(s)))

def D(st):
    # Applies a L move to a given state
    s = copy.deepcopy(st)
    return(x2(U(x2(s))))
def D2(st):
    # Applies a L2 move to a given state
    s = copy.deepcopy(st)
    return(D(D(s)))
def D3(st):
    # Applies a L' move to a given state
    s = copy.deepcopy(st)
    return(D(D2(s)))


def new_orientation(alg, rotation):
    # Remove spaces and replace sequences in `alg`
    if not rotation:
        return alg
    alg = alg.replace(" ", "")
    alg = re.sub(r'U2', 'UU', alg)
    alg = re.sub(r"U'", 'UUU', alg)
    alg = re.sub(r'F2', 'FF', alg)
    alg = re.sub(r"F'", 'FFF', alg)
    alg = re.sub(r'R2', 'RR', alg)
    alg = re.sub(r"R'", 'RRR', alg)
    alg = re.sub(r'UUUU', '', alg)
    alg = re.sub(r'FFFF', '', alg)
    alg = re.sub(r'RRRR', '', alg)
    alg = list(alg)  # Convert to list of characters

    # Remove spaces and replace sequences in `rotation`
    rotation = rotation.replace(" ", "")
    rotation = re.sub(r'x2', 'xx', rotation)
    rotation = re.sub(r"x'", 'xxx', rotation)
    rotation = re.sub(r'z2', 'zz', rotation)
    rotation = re.sub(r"z'", 'zzz', rotation)
    rotation = re.sub(r'y2', 'yy', rotation)
    rotation = re.sub(r"y'", 'yyy', rotation)
    rotation = re.sub(r'y', 'xxxzx', rotation)
    rotation = re.sub(r'x', 'xxx', rotation)
    rotation = re.sub(r'z', 'zzz', rotation)
    rotation = list(rotation)  # Convert to list of characters

    for i in range(len(alg)):
        rotation_str = ''.join(rotation)
        rotation_str = re.sub(r'xxxx', '', rotation_str)
        rotation_str = re.sub(r'zzzz', '', rotation_str)
        rotation = list(rotation_str)

        aux = []
        for j in range(len(rotation)):
            if alg[i] == 'U':
                if rotation[j] == 'x':
                    alg[i] = 'F'
                    aux.append('x')
                elif rotation[j] == 'z':
                    alg[i] = 'R'
                    aux.extend(['z', 'x', 'x', 'x'])
            elif alg[i] == 'F':
                if rotation[j] == 'z':
                    alg[i] = 'F'
                    aux.append('z')
                elif rotation[j] == 'x':
                    alg[i] = 'U'
                    aux.extend(['z', 'x'])
            elif alg[i] == 'R':
                if rotation[j] == 'x':
                    alg[i] = 'R'
                    aux.append('x')
                elif rotation[j] == 'z':
                    alg[i] = 'U'
                    aux.append('z')
        rotation = aux

    alg = ''.join(alg)

    # Replace sequences back to notation
    alg = re.sub(r'UUUU', '', alg)
    alg = re.sub(r'FFFF', '', alg)
    alg = re.sub(r'RRRR', '', alg)

    alg = re.sub(r'UUU', "U'", alg)
    alg = re.sub(r'FFF', "F'", alg)
    alg = re.sub(r'RRR', "R'", alg)

    alg = re.sub(r'UU', 'U2', alg)
    alg = re.sub(r'FF', 'F2', alg)
    alg = re.sub(r'RR', 'R2', alg)

    alg = re.sub(r'U', ' U', alg)
    alg = re.sub(r'F', ' F', alg)
    alg = re.sub(r'R', ' R', alg)

    return alg.strip()


def translDB(sts):
    dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x']

    st = [0] * 24
    for i in range(0, len(sts)):
        st[i] = str(dic.index(sts[i]) + 1)
    sst = '[' + ','.join(st) + ']'

    return sst


def invtranslDB(sts):
    dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x']
    sts = ast.literal_eval(sts)
    # print(type(sts))
    # print(type(sts[0]))
    st = ''
    for i in range(0, len(sts)):
        # print(sts[i]-1)
        st = st + dic[sts[i] - 1]

    return st
