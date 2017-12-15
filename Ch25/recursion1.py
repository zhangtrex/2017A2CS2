# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:24:03 2017

@author: Kevin Young
"""

def count(x):
    if x == 12:
        return
    print(x)
    count (x+2)

def factorial (x):
    if x == 1:
        return 1
    return x * factorial(x-1)

def BunnyEars(x):
    if x == 0:
        return 0 
    
    return 2 + BunnyEars(x - 1)

def Fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1 
    return Fibonacci(x-1) + Fibonacci(x-2)

def BunnyEars2(x):
    if x == 0:
        return 0
    elif x % 2 == 1:
        return 2 + BunnyEars2(x-1)
    elif x % 2 == 0:
        return 3 + BunnyEars2(x-1)

def Triangle (x):
    if x == 0:
        return 0
    return x + Triangle(x-1)

def SumDigit(x):
    if x == 0:
        return 0
    return (x % 10) + SumDigit(x//10)

def Count7(x):
    if x == 0:
        return 0 
    if x % 10 == 7 :
        return 1 + Count7(x // 10)
    else: 
        return 0 + Count7(x // 10)

def Count8(x):
    if x == 0:
        return 0
    if (x // 10) % 10 == 8 and x % 10 == 8:
        return 2 + Count8(x // 10)
    elif (x // 10) % 10 != 8 and x % 10 == 8:
        return 1 + Count8(x // 10)
    return Count8(x // 10)

def PowerN(x,n):
    if x == 0 and n == 0:
        return 1
    elif x == 0:
        return 0
    elif n == 0:
        return 1
    return x * PowerN(x,n-1)

def CountX(s):
    if s == '':
        return 0 
    if s[-1:] == 'x':
        return 1 + CountX(s[:-1])
    else:
        return CountX(s[:-1])

def CountHi(s):
    if s == '':
        return 0 
    if s[-2:] == 'hi':
        return 1 + CountX(s[:-1])
    else:
        return CountX(s[:-1])
    
def ChangeXY(s):
    if s == '':
        return ''
    if s[-1:] == 'x':
        return ChangeXY(s[:-1]) + 'y'
    else:
        return ChangeXY(s[:-1]) + s[-1]
    
def ChangePi(s):
    if s == '':
        return ''
    if s[-2:] == 'pi':
        return ChangePi(s[:-2]) + '3.14'
    else:
        return ChangePi(s[:-1]) + s[-1]
    
def NoX(s):
    if s == '':
        return ''
    if s[-1:] == 'x':
        return NoX(s[:-1]) 
    else:
        return NoX(s[:-1]) + s[-1]   
    
def Array6(s,i):
    if i == len(s):
        return False
    if s[-1:] == '6':
        return True
    else:
        return Array6(s[:-1], i+1)
    
def Array11(s,i):
    if i == len(s):
        return 0
    if s[i] == 11:
        return 1 + Array11(s,i+1)
    else:
        return Array11(s,i+1)

def Array220(s,i):
    if i == len(s)-1:
        return False
    if s[i]/s[i-1]== 10:
        return True
    else:
        return Array220(s,i+1)
   
def AllStar(s):
    if len(s) == 1:
        return s
    return AllStar(s[:-1])+'*'+s[-1:]

def PairStar(s):
    if s == '':
        return ''
    if len(s) == 1:
        return s
    if s[-1:] == s[len(s)-2]:
        return PairStar(s[:-1])+'*'+s[-1:]
    else:
        return PairStar(s[:-1])+s[-1:]
   
def EndX(s):
    if s == '':
        return ''
    if len (s) == 1:
        return s
    if s[:1] == 'x':
        return EndX(s[1:])+'x'
    else:
        return s[:1]+EndX(s[1:])

def CountPairs(s):
    if len(s) == 2:
        return 0 
    if s[-1:] == s[len(s) - 3]:
        return 1 + CountPairs(s[:-1])
    else:
        return CountPairs(s[:-1])
    
def CountAbc(s):
    if len(s) == 2:
        return 0 
    if s[-3:] == 'aba' or s[-3:] == 'abc':
        return 1 + CountAbc(s[:-1])
    else:
        return CountAbc(s[:-1])
    
def Count11(s):
    if len(s) == 1:
        return 0 
    if s[-2:] == '11':
        return 1 + Count11(s[:-2])
    else:
        return Count11(s[:-1])
    
def StringClean(s):
    if s == '':
        return ''
    if len(s) == 1:
        return s
    if s[-1] == s[-2]:
        return StringClean(s[:-1])
    else:
        return StringClean(s[:-1])+s[-1]

def CountHi2(s):
    if len(s) == 2:
        return 0 
    if s[-2:] == 'hi' and s[-3] != 'x':
        return 1 + CountHi2(s[:-1])
    else:
        return CountHi2(s[:-1])

def ParenBit(s):
    if s == '':
        return ''
    if ')' in s[:-1]:
        return ParenBit(s[:-1])
    elif '(' in s:
        return ParenBit(s[:-1]) + s[-1]
    return ParenBit(s[:-1])

def NestParen(s):
    if s == '':
        return True 
    elif len(s) % 2 == 1:
        return False 
    if s[0] == '(' and s[-1] == ')':
        return NestParen(s[1:-1])
    else:
        return False
    
def StrCount(s,sf):
    if len(s) < len(sf):
        return 0
    if s[-len(sf):] == sf :
        return 1 + StrCount(s[:-len(sf)],sf)
    else:
        return StrCount(s[:-1],sf)
 
def StrCopies(s,sf,n):
    if s == '' and n == 0:
        return True
    if len(s) < len(sf):
        return False
    if s[-len(sf):] == sf :
        return StrCopies(s[:-len(sf)],sf,n-1)
    else:
        return StrCopies(s[:-1],sf,n)
    
def StrDist(s,sf):
    if s == '':
        return 0
    if s[:len(sf)] == sf:
        if s[:-len(sf)] == sf:
            return 2*len(s) + StrDist(s[len(sf):-len(sf)],sf)
        else:
            return len(s) + StrDist(s[len(sf):-1], sf)
    elif s[:len(sf)] != sf:
        if s[:-len(sf)] == sf:
            return len(s) + StrDist(s[1:-len(sf)],sf)
        else:
            return StrDist(s[1:-1], sf)
        
def GroupSum()