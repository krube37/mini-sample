#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:12:39 2020

@author: hemanthchowdary
"""
def palind(s):
    spl = "".join(reversed(s))
    if s == spl:
        return True
    else:
        return False
def remodupli(s):
    li = list(s.split())
    l = []
    for i in li:
        if i in l:
            continue
        else:
            l.append(i)
    return l
        
s = input("enter the string : ")
ren = 1
d = ""
for i in range(len(s)):
    for j in range(ren,len(s)):
        if palind(s[i:j+1]):
            d = d+" "+s[i:j+1]
    ren += 1
final = remodupli(d)
print(final)

