import time
import random
import sys

sys.setrecursionlimit(1500)

#<----------------------------RANDROM NUMBER GENERATOR------------------------->
def number_generator(size):
    # Open a file
    file = open(str(size)+".txt", "w")

    # Generating random numbers
    for i in range(size):
        no = random.randrange(1,1000,1)
        # Writing random numbers in the file
        file.write(str(no)+" ");

    # Close opend file
    file.close()



#<---------------------------- OUTPUT LIST ------------------------>
def writeList(list,type):

    # Checking Sort type
    if type == "m":
        name = "MergeSort_"

    elif type == "i":
        name = "InsertionSort_"

    elif type == "q":
        name ="QuickSort_"

    # Open a file
    file = open(name+str(len(list))+".txt", "w")

    # Generating random numbers
    for i in list:
        # Writing the number in sorted list
        file.write(str(i)+" ");

    # Close opend file
    file.close()


#<------------------------------------ MERGE SORT --------------------------------->
def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]      # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]           # copy of first half
    S2 = S[mid:n]           # copy of second half
    # conquer (with recursion)
    merge_sort(S1)          # sort copy of first half
    merge_sort(S2)          # sort copy of second half
    # merge results
    merge(S1, S2, S)        # merge sorted halves back into S

#<----------------------------------INSERTION SORT ------------------->

def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

#<--------------------------- QUICKSORT ---------------------------------->

def quicksort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

# <----------------- METHOD TO MAKE LIST FROM FILE ----------------->

def read_filenum(file):
    list=[]
    for line in file:
        line = line.strip()
        list= line.split()
        list = [int(i) for i in list]
    return list

# <------------------ METHOD TO MEASURE PROCESS TIME ----------------->

def process_time(method):
    t0 = time.clock()
    method
    processTime = (time.clock() - t0) * 1000
    return processTime

#<---------------------------------- GENERATING NUMBERS ------------------------------------------>
number_generator(10)
number_generator(100)
number_generator(1000)
number_generator(10000)
number_generator(100000)

#<---------------------------------- OPENING FILES ----------------------------------------------->
file1 = open('10.txt','r')
file2 = open('100.txt','r')
file3 = open('1000.txt','r')
file4 = open('10000.txt','r')
file5 = open('100000.txt','r')

#<---------------------------------- CREATING LIST FROM FILE -------------------------------------->

list1 = read_filenum(file1)
list2 = read_filenum(file2)
list3 = read_filenum(file3)
list4 = read_filenum(file4)
list5 = read_filenum(file5)

# <------------------------------------ MERGE-SORT -------------------------------------------------->

merge_time1 = process_time(merge_sort(list1))
merge_time2 = process_time(merge_sort(list2))
merge_time3 = process_time(merge_sort(list3))
merge_time4 = process_time(merge_sort(list4))
merge_time5 = process_time(merge_sort(list5))

writeList(list1,"m")
writeList(list2,"m")
writeList(list3,"m")
writeList(list4,"m")
writeList(list5,"m")

# <------------------------------------ INSERTION SORT ----------------------------------------------->

insert_time1 = process_time(insertionSort(list1))
insert_time2 = process_time(insertionSort(list2))
insert_time3 = process_time(insertionSort(list3))
insert_time4 = process_time(insertionSort(list4))
insert_time5 = process_time(insertionSort(list5))

writeList(list1,"i")
writeList(list2,"i")
writeList(list3,"i")
writeList(list4,"i")
writeList(list5,"i")

# <------------------------------------ QUICKSORT ----------------------------------------------->

quick_time1 = process_time(quicksort(list1))
quick_time2 = process_time(quicksort(list2))
quick_time3 = process_time(quicksort(list3))
quick_time4 = process_time(quicksort(list4))
quick_time5 = process_time(quicksort(list5))

writeList(list1,"q")
writeList(list2,"q")
writeList(list3,"q")
writeList(list4,"q")
writeList(list5,"q")
# <-------------------------------------- CLOSING FILE --------------------------------------------------->

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()

# <-------------------------------------- PRINTING OUTPUT --------------------------------------------------->

# <------------------------------------ MERGE SORT ---------------------------------------->
print("MergeSort")
print("Input size (N): (# of numbers) \t\t Time cost:")
print("10 \t\t\t\t\t", merge_time1, "milliseconds")
print("100 \t\t\t\t\t", merge_time2, "milliseconds")
print("1000 \t\t\t\t\t", merge_time3, "milliseconds")
print("10000 \t\t\t\t\t", merge_time4, "milliseconds")
print("100000 \t\t\t\t\t", merge_time5, "milliseconds")

print("===================================================================================================================")
print()

# <------------------------------------ INSERTION SORT ---------------------------------------->
print("Insertion Sort")
print("Input size (N): (# of numbers) \t\t Time cost:")
print("10 \t\t\t\t\t", insert_time1, "milliseconds")
print("100 \t\t\t\t\t", insert_time2, "milliseconds")
print("1000 \t\t\t\t\t", insert_time3, "milliseconds")
print("10000 \t\t\t\t\t", insert_time4, "milliseconds")
print("100000 \t\t\t\t\t", insert_time5, "milliseconds")

print("===================================================================================================================")
print()

# <------------------------------------ QUICKSORT ---------------------------------------->
print("Quick Sort")
print("Input size (N): (# of numbers) \t\t Time cost:")
print("10 \t\t\t\t\t", quick_time1, "milliseconds")
print("100 \t\t\t\t\t", quick_time2, "milliseconds")
print("1000 \t\t\t\t\t", quick_time3, "milliseconds")
print("10000 \t\t\t\t\t", quick_time4, "milliseconds")
print("100000 \t\t\t\t\t", quick_time5, "milliseconds")

print("===================================================================================================================")
print()
