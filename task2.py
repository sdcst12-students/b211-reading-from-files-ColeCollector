"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""


def find():
    import math
    filename = "task02a.txt"
    file = open(filename,"r")
    data = file.read()
    lineData = data.split("\n")
    lineData = data.split("\n")
    list1 = []
    n = 0
    total = 0

    while True:
        if n >= (len(lineData)-1):
            break
        else:
            a = int(lineData[n])
            b = int(lineData[n+1])
            c = int(lineData[n+2])

            maxn = max(a,b,c)
            minn = min(a,b,c)
            mid = a+b+c - maxn-minn


            if math.sqrt((mid**2)+(minn**2)) == maxn:
                total +=1
                list1.append([maxn,mid,minn])

        n +=4

    print(list1)
    print(total)
    
find()

    

