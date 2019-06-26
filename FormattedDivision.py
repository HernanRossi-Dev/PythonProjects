import re
class FormattedDivision:
    def FormatInput(self, num1, num2):
        intResult, decResult = str(num1 / num2).split('.')
        decResult = self.FormatDecimal(decResult)
        intResult = self.FormatInteger(intResult)
        result = intResult + '.' + decResult
        return result


    def FormatInteger(self, int):
        intLen = len(int) - 1
        result = []
        count = 0
        for i in range(intLen, -1, -1):
            count +=1
            if count == 3:
                result.insert(0, ','+ int[i])
                count = 0
            else:
                result.insert(0, int[i])
        return ''.join(result)

    def FormatDecimal(self, deci):
        while len(deci) < 4:
            deci += '0'
        result = deci
        if len(deci) > 4:
            result = deci[:3]
            if len(deci) > 5 and int(deci[4]) >= 5:
                result += str(int(deci[3]) + 1)
            else:
                result += deci[3]
        return result


formatedDiv = FormattedDivision()
testOne = formatedDiv.FormatInput(123456789, 100)
testTwo = formatedDiv.FormatInput(123456789, 10000)
testThree = formatedDiv.FormatInput(2, 3)
testFour = formatedDiv.FormatInput(10, 10)
print(testOne)
print(testTwo)
print(testThree)
print(testFour)
