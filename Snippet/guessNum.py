def guessNumber(n):
    low = 1
    high = n
    myNum = (low + high) // 2
    while guess(myNum != 0):
        if(guess(myNum) > 0):
            high = myNum - 1
            myNum = (low + high) // 2
        elif(guess(myNum) < 0):
            low = myNum + 1
            myNum = (low + high) // 2
    return myNum
def guess(num):
    if num > 6:
        return 1
    elif num == 6:
        return 0
    else:
        return -1
guessNumber(10)