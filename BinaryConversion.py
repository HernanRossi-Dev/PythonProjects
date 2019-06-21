def BinaryConversion(str):
    splitStr = list(str)
    charCount = len(str) - 1
    sum = 0
    for x, y in zip(range(charCount, -1, -1), splitStr):
        sum += int(y) * 2 ** x
    return sum

print(BinaryConversion("100101"))
print(BinaryConversion("011"))
print(BinaryConversion("1000"))
