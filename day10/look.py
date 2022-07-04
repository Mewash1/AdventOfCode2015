def lookAndSay(sequence:str, loops):
    numberSum = 1
    currentSequence = sequence + "x"
    nextSequence = ''
    for _ in range(loops):
        for i in range(len(currentSequence) - 1):
            if currentSequence[i] == currentSequence[i+1]:
                numberSum += 1
            else:
                nextSequence += str(numberSum) + currentSequence[i]
                numberSum = 1
        # print(currentSequence)
        currentSequence = nextSequence + "x"
        nextSequence = ''
    return len(currentSequence) - 1


if __name__ == "__main__":
    print(lookAndSay('1113222113', 50))