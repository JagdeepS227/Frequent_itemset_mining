import os
import csv
import time

def createCandidateSet(data, minSupport, total_transactions, setData):
    cand = []
    for row in data:
        for itm in row:
            if [itm] not in cand:
                if itm != '':
                    cand.append([itm])
    cand.sort()
    candidates_map=map(frozenset, cand)
    candSet = list(candidates_map)
    lstCands = Prune_step(setData, candSet, minSupport, total_transactions)
    lstCands = [lstCands]

    return lstCands


def Prune_step(data, candidateSet, minSupport, total_transactions):
    subsetCount = {}
    for curSet in data:
        for cand in candidateSet:
            #removes empty element from candidate set if any exists as it will come in groceries - groceries.csv dataset
            if cand.issubset(curSet) and cand != '':
                #initialise a new itemset set counting
                if not cand in subsetCount:
                    subsetCount[cand] = 1
                #increment count of added itemset
                else:
                    subsetCount[cand] += 1

    valid = []
    #pruning itemsets with support less than min_support
    for key in subsetCount:
        # print(key,"LLLLLLL")
        sup = subsetCount[key]
        if sup >= total_transactions * (minSupport):
            valid.insert(0, key)
    return valid

#generates new candidate sets based on final candidate sets of previous level
#UNION step of our algorithm
def genApriori(freqSets, k):
    valid = []
    nFreqSets = len(freqSets)
    for i in range(nFreqSets):
        for j in range(i + 1, nFreqSets):
            lstCands1 = list(freqSets[i])[:k - 2]
            lstCands2 = list(freqSets[j])[:k - 2]
            lstCands1.sort()
            lstCands2.sort()
            # if all elements except last one are equal
            if lstCands1 == lstCands2:
                valid.append(freqSets[i] | freqSets[j])  # union
    return valid


def apriori(data, minSupport, total_transactions):
    setData = list(map(set, data))
    # create C1 and subset count for first level
    lstCands = createCandidateSet(data, minSupport, total_transactions, setData)
    print("1st level freq itemsets : ")
    print(lstCands)
    k = 2
    while (len(lstCands[k - 2]) > 0):
        #sending just previous candidate set to Union Step along with current level for generating new candidate set
        candSetX = genApriori(lstCands[k - 2], k)
        #sending newly generated candidate set to prune step for filtering out frequent itemsets only
        lstCandsX =Prune_step(setData, candSetX, minSupport, total_transactions)

        print(k, " level freq item set: ")
        print(lstCandsX)
        lstCands.append(lstCandsX)
        # print(lstCands)
        k += 1

    return lstCands


def read_data(file_name, first_row, first_element):
    data = []
    a = 0
    if not os.path.isfile(file_name):
        print("Not found")
        return None

    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip().split(' '))
            a = a + 1
    # print(data)
    print("numb of trans", a)
    return data, a


def read_data1(file_name, first_row, first_element):
    data = []
    a = 0
    if not os.path.isfile(file_name):
        print("Not found")
        return None

    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
            a = a + 1
    # print(data)
    print("numb of trans", a)
    return data, a


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
    # print(data)
    print("numbe of trans is ", a)
    return data, a


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
if choice == 1:
    data, a = read_data("T40I10D100K", "false", "false")
    start_time = time.time()
    sets = apriori(data, minSupp, a)
    end_time = time.time()

    print("\n**** Apriori with minSupport = {} ****".format(minSupp))
    print("\nSets:\n")
    cntt = 0
    for x in sets:
        for y in x:
            cntt = cntt + 1
            print(y)
    print(cntt)
    print("Total time taken : ", end_time - start_time)

if choice == 2:
    data, a = read_data("T10I4D100K", "false", "false")
    start_time = time.time()
    sets = apriori(data, minSupp, a)
    end_time = time.time()

    print("\n**** Apriori with minSupport = {} ****".format(minSupp))
    print("\nSets:\n")
    cntt = 0
    for x in sets:
        for y in x:
            cntt = cntt + 1
            print(y)
    print(cntt)
    print("Total time taken : ",end_time-start_time)
if choice == 3:
    data, a = read_data("retail", "false", "false")
    start_time = time.time()
    sets = apriori(data, minSupp, a)
    end_time = time.time()

    print("\n**** Apriori with minSupport = {} ****".format(minSupp))
    print("\nSets:\n")
    cntt = 0
    for x in sets:
        for y in x:
            cntt = cntt + 1
            print(y)
    print(cntt)
    print("Total time taken : ", end_time - start_time)
if choice == 4:
    data, a = read_data2("groceries - groceries.csv", "true", "true")
    start_time = time.time()
    sets = apriori(data, minSupp, a)
    end_time = time.time()
    print("\n**** Apriori with minSupport = {} ****".format(minSupp))
    print("\nSets:\n")
    cntt = 0
    for x in sets:
        for y in x:
            cntt = cntt + 1
            print(y)
    print(cntt)
    print("Total time taken : ", end_time - start_time)
if choice == 5:
    data, a = read_data1("groceries.csv", "false", "false")
    start_time = time.time()
    sets = apriori(data, minSupp, a)
    end_time = time.time()
    #print(data)
    print("\n**** Apriori with minSupport = {} ****".format(minSupp))
    print("\nSets:\n")
    cntt = 0
    for x in sets:
        for y in x:
            cntt = cntt + 1
            print(y)
    print(cntt)
    print("Total time taken : ", end_time - start_time)
if choice == 6:
    data, a = read_data("dataset", "false", "false")
    start_time = time.time()
    sets = apriori(data, minSupp, a)
    end_time = time.time()

    print("\n**** Apriori with minSupport = {} ****".format(minSupp))
    print("\nSets:\n")
    cntt = 0
    for x in sets:
        for y in x:
            cntt = cntt + 1
            print(y)
    print(cntt)
    print("Total time taken : ", end_time - start_time)