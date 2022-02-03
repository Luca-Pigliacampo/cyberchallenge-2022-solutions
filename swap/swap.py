#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # Output da inviare alla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
fin = sys.stdin  # input fornito dalla piattaforma
fout = sys.stdout  # Output da inviare alla piattaforma

def dedup(a):
    res=[a[0]]
    for i in a:
        if i!=res[-1]:
            res.append(i)
    return res

def swap(N, V):
    # SCRIVI QUA IL TUO CODICE
    P=dedup(V)
    for i in range(N-1):
        if V[i+1] < V[i]:
            ind = i

    if ind==N-2:
        ind = N-1
        d=-1
    elif V[ind+2]>=V[ind]:
        ind += 1
        d=-1
    else:
        d=1


    val = V[ind]
    ind0 =ind;
    ind += d
    while (V[ind]*d)<(val*d):
        ind += d
    if d == -1:
        ind += 1
    else:
        ind0 += 1

    c=len(dedup(V[min(ind0, ind):max(ind0, ind)]))

    return c


N = int(fin.readline().strip())
V = list(map(int, fin.readline().strip().split(" ")))
print(swap(N, V))
