import functools as ft

N = int(input())

special = ['!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

for _ in range(N):
    pair = input().split()
    pwd = pair[0]
    old = pair[1]
    lc = False
    uc = False
    dig = False
    spc = False
    sim = False
    eq = False
    for c in pwd:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            lc = True
        if ord(c) <= ord('Z') and ord(c) >= ord('A'):
            uc = True
        if c.isdigit():
            dig = True
        if c in special:
            spc = True
    
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            eq = True

    for i in range(max(len(pwd), len(old))):
        if len(pwd)>i and (pwd[:i]+pwd[i+1:])==old:
            sim = True
        if len(old)>i and (old[:i]+old[i+1:])==pwd:
            sim = True
        if len(old)>i and len(pwd)>i and (old[:i]+old[i+1:])==(pwd[:i]+pwd[i+1:]):
            sim = True

    if len(pwd)>=8 and len(pwd)<=16 and lc and uc and spc and dig and (not eq) and (not sim):
        print(1)
    else:
        print(0)
