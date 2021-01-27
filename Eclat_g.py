import time

FreqItems = dict()
support = dict()


def eclat(prefix, items, dict_id ,minsup,cnt):
    while items:
        i ,itids = items.pop()
        isupp = len(itids)
        if isupp >= minsup*cnt:
            print(prefix + [i])
            FreqItems[frozenset(prefix + [i])] = isupp
            suffix = []
            for j, ojtids in items:
                jtids = itids & ojtids
                if len(jtids ) >= minsup*cnt:
                    suffix.append((j, jtids))
            dict_id += 1
            eclat(prefix +[i], sorted(suffix, key=lambda item: len(item[1]), reverse=True), dict_id ,minsup,cnt)





def Read_Data(filename, delimiter):
    data1 = {}
    trans = 0
    itemcount=0
    f = open(filename, 'r', encoding="utf8")
    for row in f:
        trans += 1
        for item in row.strip().split(','):
            if item not in data1:
                data1[item] = set()
            data1[item].add(trans)
            itemcount+=1
    f.close()

    print("total number of items: ",itemcount)
    print("numb of trans", trans)
    return data1, trans

def Read_Data4(filename, delimiter=' '):
    data = {}
    trans = 0
    itemcount=0
    f = open(filename, 'r', encoding="utf8")
    for row in f:
        trans += 1
        for item in row.split(delimiter):
            if item not in data:
                data[item] = set()
            data[item].add(trans)
            itemcount += 1
    f.close()

    print("total number of items: ",itemcount)
    print("numb of trans", trans)
    return data,trans


def Read_Data2(filename, delimiter):
    data1 = {}
    trans = 0
    itemcount=0
    f = open(filename, 'r', encoding="utf8")
    next(f, None)
    for row in f:
        trans += 1
        for item in row.strip().split(delimiter)[1:]:
            if item not in data1:
                if item!='\n':
                    data1[item] = set()
            data1[item].add(trans)
            itemcount += 1
    f.close()

    print("total number of items: ",itemcount)
    print("numb of trans", trans)
    return data1, trans
def Read_Data3(filename, delimiter):
    data1 = {}
    trans = 0
    itemcount=0
    f = open(filename, 'r', encoding="utf8")
    next(f, None)
    for row in f:
        trans += 1
        for item in row.strip().split(delimiter):
            if item not in data1:
                if item!='\n':
                    data1[item] = set()
            data1[item].add(trans)
            itemcount+=1
    f.close()

    print("numb of trans", trans)
    print("total number of items: ",itemcount)
    return data1, trans

print("Enter 1 for dataset T40I10D100K ")
print("Enter 2 for dataset  T10I4D100K ")
print("Enter 3 for dataset  retail ")
print("Enter 4 for dataset  groceries - groceries.csv ")
print("Enter 5 for dataset  groceries.csv ")
print("Enter 6 for dataset  dataset ")
choice = int(input())
print("Enter minimum support value betweeen 0 to 1: ")
minSupp = input()
minsup = float(minSupp)
dict_id = 1
if choice==1:
    data,cnt = Read_Data4('T40I10D100K', ' ')
    data.pop("\n", None)
    data.pop("", None)
    #print(data)
    print('finished reading data..... \n Starting mining .....')
    start_time=time.time()
    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True), dict_id, minsup,cnt)
    end_time=time.time()

    print("Total number of frequent item sets generated: ",len(FreqItems))
    print("Total time taken: ",end_time-start_time)

if choice==2:
    data,cnt = Read_Data4('T10I4D100K', ' ')
    data.pop("\n", None)
    data.pop("", None)
    #print(data)
    print('finished reading data..... \n Starting mining .....')
    start_time=time.time()
    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True), dict_id, minsup,cnt)
    end_time=time.time()

    print("Total number of frequent item sets generated: ",len(FreqItems))
    print("Total time taken: ",end_time-start_time)

if choice == 3:
    data ,cnt= Read_Data4('retail', ' ')
    data.pop("\n", None)
    data.pop("", None)
    #print(data)
    print('finished reading data..... \n Starting mining .....')
    start_time = time.time()
    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True), dict_id, minsup,cnt)
    end_time = time.time()
    print("Total number of frequent item sets generated: ", len(FreqItems))
    print("Total time taken: ", end_time - start_time)

if choice == 4:
    data ,trans= Read_Data2('groceries - groceries.csv', ',')
    data.pop("\n", None)
    data.pop("", None)
    # print(data)
    print('finished reading data..... \n Starting mining .....')
    start_time = time.time()
    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True), dict_id, minsup,trans)
    end_time = time.time()

    print("Total number of frequent item sets generated: ", len(FreqItems))
    print("Total time taken: ", end_time - start_time)

if choice == 5:
    data,trans = Read_Data('groceries.csv', ',')
    data.pop("\n", None)
    data.pop("", None)
    #print(data)
    print('finished reading data..... \n Starting mining .....')
    start_time = time.time()
    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True), dict_id, minsup,trans)
    end_time = time.time()

    print("Total number of frequent item sets generated: ", len(FreqItems))
    print("Total time taken: ", end_time - start_time)

if choice == 6:
    data,trans = Read_Data3('dataset',' ')
    #print(data)
    print('finished reading data..... \n Starting mining .....')
    start_time = time.time()
    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True), dict_id, minsup,trans)
    end_time = time.time()

    print("Total number of frequent item sets generated: ", len(FreqItems))
    print("Total time taken: ", end_time - start_time)