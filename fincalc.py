#!/usr/bin/env python

# LOAN AND ANNUITY MODULE

# Copyright (c) 2017 Sheldon Barry


import math


def pv(i,n,fv,pmt):
    """Calculate the present value of an annuity"""
    pv = fv*(1/(1+i)**n) - pmt*((1-(1/(1+i)**n))/i)
    return pv
    

def fv(i,n,pv,pmt):
    """Calculate the future value of an annuity"""
    fv = pv*((1+i)**n) + pmt*((1+i)**n-1)/i
    return fv
    

def pmt(i,n,pv,fv):
    """Calculate the annuity payment value"""
    pmt = fv/(((1+i)**n-1)/i) - pv/((1-(1/(1+i)**n))/i) 
    return pmt
    

def n(i,pv,fv,pmt):
    """Calculate the number of periods in an annuity"""
    n = math.log((fv*i+pmt)/(pv*i+pmt)) / math.log(1+i) 
    return n

# (need to improve this algorithm)
def i(n,pv,fv,pmt):
    """Calculate the interest rate of an annuity"""
    i=0.0000001
    a=0
    while a <= fv:
        a = pv*((1+i)**n) + pmt*((1+i)**n-1)/i
        if a<fv:
            pass
            i=i+0.0000001
        else:
            return i
            # prevent next iteration
            break                   
    
    
