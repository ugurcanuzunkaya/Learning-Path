def readFile(path):
    with open(path, 'r') as myFile:
        M = []
        for line in myFile:
            line=line.replace('\n','')
            myLine= line.split("\t")
            M.append(myLine)
    return M


def sortItem(A, indx):

    for i in range(len(A)):
        mx_in = i
        for j in range(i+1,len(A)):
            if int(A[j][indx]) > int(A[mx_in][indx]):
                mx_in = j
        A[i], A[mx_in] = A[mx_in], A[i]
    return A

def putInto(A, C, constIndx):

    selectedItems = []
    counter=0
    while len(selectedItems) < len(A) and C - int(A[counter][constIndx]) > 0:
        selectedItems.append(int(A[counter][0]))
        C= C - int(A[counter][constIndx])
        counter += 1
    return selectedItems

def writeSolution(path, Ids):
    with open(path, 'w') as myFile:
        myFile.write("The solution is:\n")
        for i in range(len(Ids)):
            myFile.write(str(Ids[i])+'\n')
    return



#you should provide paths here
filePath = "items.txt"
outputFilePath = "result.txt"
Data= readFile(filePath)
sortedData = sortItem(Data, 2)

limit= int(input("Please enter the capacity: "))
selectedIds = putInto(sortedData,limit,1)
writeSolution(outputFilePath, selectedIds)
print()