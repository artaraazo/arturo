#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:33:25 2022

@author: artutaraperegmail.com
"""
from multiprocessing import Process
from multiprocessing import current_process 
from multiprocessing import Value
import time

def f(c):
    for i in range(100):
        temp = c.value + 1
        print (f"hola soy {current_process().pid}, vuelta: {i}, contador: {c.value}") 
        time.sleep(0.1)
        c.value = temp
        
if __name__ == "__main__":
    N= 8
    lp = []
    c = Value("i", 0)  #Este i es comentado?
    for i in range(N):
        lp.append(Process(target=f, args=(c,)))
        
    print ("Valor inicial del contador", c.value) 
    for p in lp:
        p.start()