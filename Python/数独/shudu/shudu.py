# -*- coding: utf-8 -*-

import numpy as np

sudoku=np.array([
            [8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0],
            ])

def col(j):
    colu = []
    for i in xrange(9):
        colu.append(sudoku[i][j])
    return colu
def squar():
    a = []
    a.append([sudoku[i][j] for i in xrange(3) for j in xrange(3)])
    a.append([sudoku[i][j] for i in xrange(3,6) for j in xrange(3)])
    a.append([sudoku[i][j] for i in xrange(6,9) for j in xrange(3)])
    a.append([sudoku[i][j] for i in xrange(3) for j in xrange(3,6)])
    a.append([sudoku[i][j] for i in xrange(3,6) for j in xrange(3,6)])
    a.append([sudoku[i][j] for i in xrange(6,9) for j in xrange(3,6)])
    a.append([sudoku[i][j] for i in xrange(3) for j in xrange(6,9)])
    a.append([sudoku[i][j] for i in xrange(3,6) for j in xrange(6,9)])
    a.append([sudoku[i][j] for i in xrange(6,9) for j in xrange(6,9)])
    return a



def guess(i,j):
    lst = [1,2,3,4,5,6,7,8,9]
    posible = []
    for num in sudoku[i]:
        if num in lst:
            lst.remove(num)
    for  num in col(j):
        if num in lst:
            lst.remove(num)
    b = (i/3) + (j/3)
    for num in squar()[b]:
        if num in lst:
            lst.remove(num)
    return lst

def min_guess(sudoku,del_x):
    dic = {}

    for i in xrange(9):
        for j in xrange(9):
            if sudoku[i][j] == 0:
                dic[i,j] = guess(i,j)
    mini = min(dic, key = lambda c: len(dic[c]))
    x = mini[0]
    y = mini[1]

    value = dic[mini]

    for i in del_x:
        if i in value:
            value.remove(i)

    return x,y,value        #  返回最小可能（i,j,[值]） 如 （1,6,[5]）




a = {}
for i in xrange(9):
    for j in xrange(9):
        a.update(dict({(i,j):guess(i,j)}))




def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].remove(d)
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def search(a):
    "Using depth-first search and propagation, try all possible values."
    if a is False:
        return False ## Failed earlier
    if all(len(a[s]) == 1 for s in a):
        return a ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(a[s]), s) for s in a if len(a[s]) > 1)

    return some(search(assign(a.copy(), s, d))
		for d in a[s])







search(a)



"""

def goback(X):


    return X



X = sudoku

v = []

orig=[]
def select(shudu):
    global X,v
    value  = min_guess(shudu,v)[2]

    if min_guess(shudu,v)[2] != []:
        if len(min_guess(shudu,v)[2]) == 1:
            shudu[min_guess(shudu,v)[0]][min_guess(shudu,v)[1]] = value[0]

            simulation(shudu)

        else:
            orig.append( shudu)
            val = value

            x = min_guess(shudu,v)[0]
            y = min_guess(shudu,v)[1]
            va = val.pop()
            shudu[x][y] = va
            v.append([va])
            simulation(shudu)


    elif min_guess(shudu,v)[2] == []:


        goback(X)


        simulation(X)






def simulation(X):

    for i in xrange(9):
        for j in xrange(9):

            if X[i][j] == 0:
                select(X)

    return X

#simulation(sudoku)








sudoku1=np.array(

 [[8, 0, 0, 0, 0, 0 ,0 ,0, 0],
 [0, 0 ,3, 6 ,0, 0, 5, 0 ,0],
 [0 ,7 ,0 ,0, 9, 0, 2 ,5 ,0],
 [0 ,5, 0 ,0 ,0 ,7, 0, 4, 0],
 [0 ,0 ,0 ,0 ,4 ,5, 7, 8 ,0],
 [0 ,0, 0, 1 ,0 ,0 ,8 ,3 ,0],
 [0 ,0 ,1 ,0 ,0, 0, 0, 6 ,8],
 [0 ,0, 8, 5, 0 ,0, 0 ,1, 0],
 [0 ,9, 0 ,0 ,0 ,0, 4, 2, 0]]
)


sudoku3=np.array([
            [8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,5,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,8,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0],
            ])
#print min_guess(sudoku3,[8])








X = {
    1: {'A', 'B'},
    2: {'E', 'F'},
    3: {'D', 'E'},
    4: {'A', 'B', 'C'},
    5: {'C', 'D'},
    6: {'D', 'E'},
    7: {'A', 'C', 'E', 'F'}}


Y = {
    'A': [1, 4, 7],
    'B': [1, 4],
    'C': [4, 5, 7],
    'D': [3, 5, 6],
    'E': [2, 3, 6, 7],
    'F': [2, 7]}

def select(X, Y, r):
    cols = []
    for j in Y[r]:

        for i in X[j]:

            for k in Y[i]:
                #print j,i, k
                if k != j:
                    X[k].remove(i)

        cols.append(X.pop(j))
    return cols


def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)


print deselect(X,Y,'A',['B','A'])


"""