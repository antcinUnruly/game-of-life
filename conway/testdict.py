def print_ab():
    print('a, b')

def printfail():
    print('fail')

def printfailagain():
    print('fail again')

d = {
    (-1, 1): print_ab,
    (1, 0): printfail,
    (0, 0): printfail
}

a = 1
b = 0
k = (a, b)
f = d[k]
f()