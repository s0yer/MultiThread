# python 3.7

from random import randint
from time import time
from multiprocessing.pool import ThreadPool

global size_list
size_list = 1597

def randon_list():
    r_list = []

    return r_list

def fibonacci():
    list_fib = [0,1]
    i = 0
    while i <= size_list:
        elem = list_fib[i] + list_fib[i+1]
        list_fib.append(elem)
        i+=1
    return list_fib

def geometric_progression():
    q = 2
    a1 = 8
    list_gp = []
    i = 1
    while i <= size_list:
        elem = a1 * pow(q,(i-1))
        list_gp.append(elem)
        i+=1
    return list_gp

print(fibonacci())
print(geometric_progression())

def mono_thread():

    print('on going')
def multi_thread():
    print('on going')