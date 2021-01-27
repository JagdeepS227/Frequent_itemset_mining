import os
import time

class treeNode:
    def __init__(self, name1, count2, parentNode):
        self.name = name1
        self.count1 = count2
        self.Link = None
        self.parent = parentNode
        self.children = {}


    def __lt__(self, other):
        in1 = self.count1
        in2 = other.count1
        if in1 < in2:
            return True
        else:
            return False

    def inc(self, count2):
        self.count1 += count2

def create_headertable(dataSet):
    headertable = {}
    for trans in dataSet:
        for item in trans:
            if item!='':
                headertable[item] = headertable.get(item, 0) + dataSet[trans]
    return headertable

def prune_step(headertable,minSup,cnt3):
    for k in headertable.copy().keys():
        if headertable[k] < minSup*cnt3:
            del (headertable[k])
    return headertable

def sort_update(headertable,dataSet,freqItemSet):

    retTree = treeNode('Null Set', 1, None)
    for tranSet, count1 in dataSet.items():
        localID = {}
        for item in tranSet:
            if item in freqItemSet:
                localID[item] = headertable[item][0]
        if len(localID) > 0:
            orderedItems = [v[0] for v in sorted(localID.items(),key=lambda p: p, reverse=True)]
            updateTree(orderedItems, retTree, headertable, count1)

    return headertable,freqItemSet,retTree

def createTree(dataSet, minSup,cnt3):
    headertable=create_headertable(dataSet)
    headertable=prune_step(headertable, minSup, cnt3)
    freqItemSet = set(headertable.keys())
    # if no items meet minsup then return None
    if len(freqItemSet) == 0:
        return None, None
    for k in headertable:
        headertable[k] = [headertable[k], None]
    #Sort and update tree if there are new freqitemsets found
    headertable, freqItemSet, retTree=sort_update(headertable,dataSet,freqItemSet)
    return retTree, headertable


def updateHeader(nodeToTest, targetNode):
    while (nodeToTest.Link != None):
        nodeToTest = nodeToTest.Link
    nodeToTest.Link = targetNode
def set_header(headertable,inTree,items):
    if headertable[items[0]][1] == None:
        headertable[items[0]][1] = inTree.children[items[0]]
    else:
        updateHeader(headertable[items[0]][1], inTree.children[items[0]])
    return headertable,inTree


def updateTree(items, inTree, headertable, count1):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count1)
    else:
        inTree.children[items[0]] = treeNode(items[0], count1, inTree)
        headertable,inTree=set_header(headertable,inTree,items)
    if len(items) > 1:
        updateTree(items[1:], inTree.children[items[0]], headertable, count1)

def read_data(file_name):
    data = []
    a = 0
    if not os.path.isfile(file_name):
        print("Not found")
        return None
    cnnt=0
    with open(file_name, 'r') as file:
        for line in file:
            z = []
            for x in line.split(' '):
                if x!='\n':
                    z.append(x)
                    cnnt+=1
            data.append(z)
            a = a + 1
    #print(data)
    print("numb of trans", a)
    print("total items: ",cnnt)
    return data,a



def read_data1(file_name):
    data = []
    a = 0
    if not os.path.isfile(file_name):
        print("Not found")
        return None
    cnnt = 0
    with open(file_name, 'r') as file:
        for line in file:
            z = []
            for x in line.strip().split(','):
                #print(x)
                z.append(x)
                cnnt+=1
            data.append(z)
            a = a + 1
    #print(data)
    print("numb of trans", a)

    print("total items: ",cnnt)
    return data,a


def read_data2(file_name, first_row, first_element):
    data = []
    a = 0
    if not os.path.isfile(file_name):
        print("Not found")
        return None
    with open(file_name, 'r') as file:
        if first_row:
            next(file, None)
        if first_element:
            reader = [x.strip().split(',')[1:] for x in file]
        for row in reader:
            data.append(row)
            a = a + 1
    #print(data)
    print("numb of trans", a)

    return data,a


def loadSimpDat(az):
    if az==1:
        simpDat,cnt3 = read_data("T40I10D100K")
        return simpDat,cnt3
    if az == 2:
        simpDat,cnt3 = read_data("T10I4D100K")
        return simpDat,cnt3
    if az == 3:
        simpDat,cnt3 = read_data("retail")
        return simpDat,cnt3
    if az == 4:
        simpDat,cnt3 = read_data2("groceries - groceries.csv", "true", "true")
        return simpDat,cnt3
    if az == 5:
        simpDat,cnt3 = read_data1("groceries.csv")
        return simpDat,cnt3
    if az == 6:
        simpDat,cnt3 = read_data("dataset")
        return simpDat,cnt3

    """simpDat = [['18', '26', '8', '10', '16'],
               ['26', '25', '24', '23', '22', '21', '20', '19'],
               ['26'],
               ['18', '23', '14', '15', '19'],
               ['25', '18', '23', '26', '17', '20', '16'],
               ['25', '26', '23', '5', '17', '19', '20', '13']]"""
    #print(simpDat)




def ascendTree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def cal_path(prefixPath,condPats,treeNode):
    if len(prefixPath) > 1:
        condPats[frozenset(prefixPath[1:])] = treeNode.count1
    treeNode = treeNode.Link
    return condPats,treeNode


def findPrefixPath(basePat, treeNode):
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        condPats, treeNode=cal_path(prefixPath,condPats,treeNode)
    return condPats


def mineTree(inTree, headertable, minSup, preFix, freqItemList,cnt3):
    bigL = [v[0] for v in sorted(headertable.items(),key=lambda p: p)]
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headertable[basePat][1])
        myCondTree, myHead = createTree(condPattBases, minSup,cnt3)
        #print(myHead)
        if myHead :
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList,cnt3)



print("Enter 1 for dataset T40I10D100K ")
print("Enter 2 for dataset  T10I4D100K ")
print("Enter 3 for dataset  retail ")
print("Enter 4 for dataset  groceries - groceries.csv ")
print("Enter 5 for dataset  groceries.csv ")
print("Enter 6 for dataset  dataset ")
choice = int(input())
print("Enter minimum support value betweeen 0 to 1: ")
minSupp = input()
minSupp = float(minSupp)
simpleDat,cnt3 = loadSimpDat(choice)
#print(simpleDat)
print(minSupp,"  ",cnt3)
#simpleDat.pop('\n')
retDict = {}
for trans in simpleDat:
    retDict[frozenset(trans)] = 1
import time

# print(initSet)
start_time=time.time()
myFPtree, myHeaderTab = createTree(retDict,minSupp,cnt3)
freqItems = []
if myFPtree is not None:
    mineTree(myFPtree, myHeaderTab, minSupp, set(), freqItems,cnt3)
end_time=time.time()
print(freqItems)
print("Number of freq patterns generated: ",len(freqItems))

max_len=0
for x in freqItems:
    if len(x)>max_len:
        max_len=len(x)


counttt=0
for x in freqItems:
    if len(x)==max_len:
        counttt+=1

print("maximum size: ",max_len)
print("number of maximal itemsets is : ",counttt)
print("Number of freq patterns generated: ",len(freqItems))
print("Total time taken : ", end_time - start_time)
