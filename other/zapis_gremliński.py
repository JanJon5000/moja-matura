def zapisGremlinski(num: int):
    strNUM = str(num)
    strNUMrearanged = ''
    zeros = 0
    charsToCompress = ''
    for char in strNUM:
        if char != '0':
            if zeros != 0:
                strNUMrearanged += str(zeros)
                strNUMrearanged += ':'
                zeros = 0
            charsToCompress += char
        else:
            if charsToCompress != '':
                strNUMrearanged += charsToCompress + ':'
                charsToCompress = ''
            zeros += 1

    if zeros >= 3:
        strNUMrearanged += str(zeros)
    else:
        strNUMrearanged = strNUMrearanged.removesuffix(':')
        for _ in range(zeros):
            strNUMrearanged += '0'
    return strNUMrearanged

def zapisNormalny(num: str):
    numRearanged = ''
    mode = ""
    return int(numRearanged)

