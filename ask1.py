myList = ([[1,5], [10, 20], [1, 6], [16,19], [5,11]])

def sumIntervals(inputList):
    output = []

    for keyIndex in range(len(inputList)):
        for keyDifference in range(inputList[keyIndex][0], inputList[keyIndex][1]):
            output.append(keyDifference)

    output = set(output)
    print(len(output))

sumIntervals(myList)