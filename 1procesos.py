#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:32:18 2022

@author: artutaraperegmail.com
"""
import time 
import random
from multiprocessing import Process
def f(value):
    for i in range(3):
        print (f"hola soy {value} vuelta {i}")
        time.sleep(random.random()/3) 
def g():
    print ("adios")
    
if __name__ == "__main__": 
    N = 10
    lp = []
    for i in range(N):
        lp.append(Process(target=f,args=(f"ana {i}",))) 
    for p in lp:
        p.start()
        
    q = Process(target=g) 
    q.start()
    print ("fin")
