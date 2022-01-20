import numpy as np
globVec = []


class Tree:

    def __init__(self,head):
        self.head = head

class Node:
    def __init__(self,path,hight):
       self.path = path
       self.cordinate = 0
       self.heigt = hight + 1
       self.right = None
       self.left = None
       self.tag = None


def find_entropy(Node,vecList):
    cordinate = []
    for i in range(8):
        cordinate.append([[0,0],[0,0]])
    # [cordinate][left/right][0,1]
    for i in range(8):
        vecCounter = 0
        for vec in vecList:
            end = True
            for j in Node.path:
                if vec[j[0]] != j[1]:
                    end = False
                    break
            if end:
               vecCounter+=1
               if vec[i]== 0:
                   if vec[8]==0:
                       cordinate[i][0][0]+=1
                   else:
                       cordinate[i][0][1]+=1
               else:
                   if vec[8] == 0:
                       cordinate[i][1][0] += 1
                   else:
                       cordinate[i][1][1] += 1

    minEntropy = 10000
    minIndex = 0
    for cord in cordinate:
        tempEntropy = find_temp_entropy(cord)
        if tempEntropy<minEntropy:
            minEntropy = tempEntropy
            minIndex = cordinate.index(cord)
    return minIndex


# -p log2(p) - (1-p)log2(1-p )

def entropy(child):
    sum = child[0]+child[1]
    if sum==0:
        return 1
    p = child[0]/sum
    return (-p*np.log2(p)) - ((1-p)*np.log2(1-p))



def find_temp_entropy(cord):
    leftEntropy = entropy(cord[0])
    rightEntropy = entropy(cord[1])

    return leftEntropy+rightEntropy




def init_data():
    data = open('vectors.txt')
    vecList = []
    counter = 0
    for vec in data:
        vecList.append(np.fromstring(vec, dtype=int, sep=' '))
    return vecList

# -p log2(p) - (1-p)log2(1-p )

def add_children(node,vecList,k):
    leftPath = list.copy(node.path)
    rightPath = list.copy(node.path)
    leftPath.append([node.cordinate,0])
    rightPath.append([node.cordinate,1])

    if node.heigt==k-1:
        leftChild = Node(leftPath, node.heigt)
        rightChild = Node(rightPath, node.heigt)
        leftChild.tag = find_label(leftChild,vecList)
        rightChild.tag = find_label(rightChild,vecList)
        node.left = leftChild
        node.right = rightChild
    else:
        leftChild = Node(leftPath,node.heigt)
        rightChild = Node(rightPath,node.heigt)
        leftChild.cordinate = find_entropy(leftChild,vecList)
        rightChild.cordinate = find_entropy(rightChild,vecList)
        node.left = leftChild
        node.right = rightChild

        add_children(leftChild,vecList,k)
        add_children(rightChild,vecList,k)



def find_label(node,vecList):
    vecCounter = 0
    oneCounter = 0
    zeroCounter = 0
    for vec in vecList:
        arriveLeafe = True
        for i in node.path:
            if vec[i[0]]!=i[1]:
                arriveLeafe = False
                break
        if arriveLeafe:
            vecCounter+=1
            if vec[8]==1:
                oneCounter+=1
            else:
                zeroCounter+=1
    if zeroCounter>oneCounter:
        return 0
    else:
        return 1






def Binary_entropy(k):
    vecList = init_data()
    head = Node([],0)
    head.cordinate = find_entropy(head,vecList)
    add_children(head,vecList,k)
    remove_stam(head)
    find_tree_entropy(head,vecList)

    # head = Node([],0)
    # cordinate = find_entropy(head,vecList)
    # head.cordinate = cordinate
    # add_children(head,vecList)
    # find_tree_entropy(head,vecList)


def find_tree_entropy(head,vecList):
    wrongCount = 0
    for vec in vecList:
        tempNode = head
        while tempNode.tag == None:
            if vec[tempNode.cordinate]==0:
                tempNode= tempNode.left
            else:
                tempNode= tempNode.right
        if vec[8]!=tempNode.tag:
            wrongCount+=1
    print(wrongCount,'/',len(vecList))


def remove_stam(node):
    if node.tag!=None:
        return

    remove_stam(node.left)
    remove_stam(node.right)

    if node.left.tag!=None and node.right.tag!=None:
        if node.left.tag==node.right.tag:
            node.tag = node.left.tag
            node.left = None
            node.right = None










if __name__ == '__main__':
   Binary_entropy(k=3)
   # vecList = init_data()
   #
   # head = Node([],0)
   #
   # index = find_entropy(head,vecList)
   # print(index)




