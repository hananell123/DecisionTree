import sys
import numpy as np


counter = 1
tempTree = []
resTree = []
minErr = sys.maxsize
# globVec = []

def init_brute_force(k):
    allVec = init_data()
    list = [0]* (2**k-1 - (2**(k-1)))
    brute_force(list,0,k,allVec)
    print('Min ERROR:',(minErr/len(allVec)))
    print('Min error tree:',resTree)

def brute_force(list,index,k,allVec):
    if len(list)==index:
        global tempTree
        tempTree=list
        leaves = [0]*(2**(k-1))
        all_leaves(leaves,0,allVec,k)
    else:
        for i in range(0, 8):
            list[index] = i
            brute_force(list,index+1,k,allVec)


def all_leaves(list,index,allVec,k):
    if len(list)==index:
        global tempTree,counter
        fullTree = tempTree + list
        treeError,leaves = find_error(fullTree,allVec,k)
        global minErr
        if treeError<minErr:
            minErr = treeError
            for i in range(len (leaves)):
                if leaves[i] == False:
                    fullTree[(2**k-1 - (2**(k-1)))+i]= -1
            global resTree

            resTree = fullTree
            print(resTree)
    else:
        for i in range(0, 2):
            list[index] = i
            all_leaves(list,index+1,allVec,k)



def find_label(tree,vector,k):
    treeIndex = 0
    leafeIndex = 0
    for i in range(k-1):
        vecCord = vector[tree[treeIndex]]
        treeIndex = (treeIndex*2) + vecCord + 1

    return tree[treeIndex],treeIndex





def find_error(tree,allVec,k):
    leaves = [False] * (2**(k-1))
    errorCounter = 0
    one = two = three = four = False
    for vec in allVec:
        treeLabel,nodeIndex =  find_label(tree,vec,k)
        leaves[nodeIndex-(2**k -1)] = True



        if treeLabel != vec[8]:
            errorCounter+=1

    return errorCounter,leaves

def init_data():
    data = open('vectors.txt')
    globVec = []
    counter = 0
    for vec in data:
        globVec.append(np.fromstring(vec, dtype=int, sep=' '))
    return globVec


if __name__ == '__main__':
   init_brute_force(k=3)







