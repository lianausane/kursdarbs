import math
from re import L

def rinka_lauk(r):
    s = math.pi * r**2
    return s

def rinka_perimets(r):
    n = 2*math.pi*r
    return n

def rinka_diamet(r):
    l = r*r
    return l

def trijs_laukums(h, a):
    v = h*a/2
    return v

def trijs_perimetrs(a, b, c):
    p = a+b+c
    return p

def cetrusturis_laukums(a, b,):
    l = a*b
    return L

def cetrusturis_perimetrs(a, b):
    h = 2*(a + b)
    return h