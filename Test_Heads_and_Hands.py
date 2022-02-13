from random import Random

MINIMUM_RANDOM_NUMBER = 2
MAXIMUM_RANDOM_NUMBER = 20

def getRandomNumber(arrayCount):
    _random = Random()
    _min = MINIMUM_RANDOM_NUMBER
    _max = MAXIMUM_RANDOM_NUMBER+arrayCount
    return _random.randint(_min,_max)

def isRandomNumbersAreRepeated(randomNumbersList):
    setRandomNumbersList = set(randomNumbersList)
    return False if len(randomNumbersList) == len(setRandomNumbersList) else True

def fillAllArrays(arraysCount,arraysLengths):
    arrays = [[] for _ in range(arraysCount)]
    for i in range(arraysCount):
        lengthCurrentArray = arraysLengths[i]
        arrays[i]=generateRandomArray(length=lengthCurrentArray)
    return arrays

def generateRandomArray(length):
    array = []
    for _ in range(length):
        randomNumber = getRandomNumber(length)
        array.append(randomNumber)
    return array

def generateRandomArraysLengths(arraysCount):
    arraysLengths = generateRandomArray(length=arraysCount)
    while isRandomNumbersAreRepeated(arraysLengths):
        arraysLengths = generateRandomArray(length=arraysCount)
    return arraysLengths

def sortByEvenOdd(array,ordinalNumber):
    condition = ordinalNumber % 2 != 0
    return sorted(array,reverse=condition)

def sortingArrays(arrays):
    for ordinalNumber in range(len(arrays)):
        currentArray = arrays[ordinalNumber]
        arrays[ordinalNumber] = sortByEvenOdd(currentArray,ordinalNumber)
    return arrays

def func(n):
    arraysCount = n

    arraysLengths = generateRandomArraysLengths(arraysCount)
    arrays = fillAllArrays(arraysCount,arraysLengths)
    
    arrays = sortingArrays(arrays)

    return arrays

n = 10
arrays = func(n)

for i in range(n):
    print(arrays[i])