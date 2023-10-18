#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def largest():
    filename = "task03.txt"
    file = open(filename,"r")
    data = file.read()
    lineData = data.split("\n")
    currentnum =0
    largestnum = 0

    for i in lineData:
        
        if i == "":
            if currentnum > largestnum:
                largestnum = currentnum
            currentnum = 0

        else:
            currentnum +=int(i)

    print("The largest number is", largestnum)

largest()