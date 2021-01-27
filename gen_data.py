from random import randint
import random


def random_array(m, n):
    arr = [0] * m
    for i in range(n):
        arr[randint(0, n) % m] += 1
    return arr


print("Enter Number of Transactions to be in dataset : ")
m=int(input())
print("Enter Average width of transaction for dataset : ")
w=int(input())
print("Enter upper limit for item values in dataset: ")
limit=int(input())
arr=random_array(m, w*m)
f = open("dataset", "w+")
for i in range(m):
    line=""
    for j in range(arr[i]):
        line+=str(random.randint(1, limit))
        line+=" "
    line+='\n'
    f.write(line)

