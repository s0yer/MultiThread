# python 3.7

from random import randint
from time import time
from multiprocessing.pool import ThreadPool

global size_list
size_list = 1000

# create an aleatory list
def randon_list():
    r_list = []
    i = 0
    while i < size_list:
        r_list.append(randint(1,500))
        i += 1
    return r_list

# create a fibonacci list
def fibonacci():
    list_fib = [0,1]
    i = 0
    while i <= (size_list-3):
        elem = list_fib[i] + list_fib[i+1]
        list_fib.append(elem)
        i+=1
    return list_fib

# create a geometric progression
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

# receive the 3 lists and sum
def sum_lists(r_list, fibo, gp):
    sum_list = []
    i = 0
    while i < size_list:
        sum_list.append(r_list[i] + fibo[i] + gp[i])
        i += 1
    return sum_list

# test the list functions
print(len(randon_list()))
print(randon_list())
print(len(fibonacci()))
print(fibonacci())
print(len(geometric_progression()))
print(geometric_progression())

def mono_thread():
    print('-----------------------------------------------------')
    print('MonoThread: ')
    start = time()
    print(sum_lists(randon_list(),fibonacci(),geometric_progression()))
    end = time()
    dif = end - start
    print('Time of processament: ' + str(dif))

def multi_thread():
    print('-----------------------------------------------------')
    print('MultiThread: ')

    # runtime = []
    threads = []
    pool = ThreadPool(processes=4)

    start = time()
    async_answer = pool.map_async(sum_lists(randon_list(),fibonacci(),geometric_progression()), (randon_list(),fibonacci(),geometric_progression()))
    print(async_answer)
    obj_answer = threads.append(async_answer)

    end = time()
    dif = end - start
    print('Time of processament: ' + str(dif))

mono_thread()
multi_thread()