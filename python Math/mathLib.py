import numpy as np
import os

class mathClass():

    euler = 2.7182818284590452353602874713527
    pi = 3.1415926535897932384626433832795

    def sigmoid(x):
        return 1 / (1 + pow(euler, -x))

    def factorial(x):
        result = 1
        for i in range(x):
            result = result * (x - i)
        return result       

    def listOfNumsToFactorialize(x):
        for i in range(x + 1):
            result = mathClass.factorial(i)
            print(str(i) + "!" + " = " + str(result))

    def oddNum(y):
        x = y
        for i in range(y + 1):
            if i == x - 1:
                return 2 * i + 1

    def triangularNums(x):
        for i in range(x):
            result = 0
            result = (i * (i + 1)) / 2
            if i == x - 1:
                return int(result)

    def calculatePi(x):
        piOn4 = 0
        oneTrue = False
        writeInFile = False

        # make function open

        for i in range(x):
            filename = os.path.isfile("num" + str(i) + ".txt")
            # print(filename)
            # print(str(filename) + str(i))
            if (str(filename) + str(i)) == "True" + str(i):
                oneTrue = True
                num = i
            if not oneTrue:
                textFile = open("num0.txt", "w") # creates a txt file 
                textFile.write("")
            if oneTrue and i + 1 == x and not os.path.getsize("num" + str(num) + ".txt") == 0:
                textFile = open("num" + str(num + 1) + ".txt", "w")
                textFile.write("")
            elif oneTrue and i + 1 == x:
                # os.remove("num" + str(num) + ".txt")
                textFile = open("num" + str(num) + ".txt", "a")
                textFile.write("")
                break

            
        

        value = 0
            
        for i in range(x):
            piOn4 = piOn4 + (2 / (3 + mathClass.triangularNums(i + 1) * 32))
            # piOn4 = piOn4 + (4 / ((3 + triangularNums(i + 1) * 32) * (3 + triangularNums(i + 1) * 32)))

            # print(piOn4 * 4)
            # print("seconds : " + str(int(((x - i)/100)))) # approximate seconds left (slow)
            # print(x - i) # how much calculations left (fast)

            # value = (2 / (3 + triangularNums(i + 1) * 32))

            # value = value + (4 / ((3 + triangularNums(i + 1) * 32) * (3 + triangularNums(i + 1) * 32)))
            formatted_string = "{:.100f}".format(float(piOn4 * 4))
            print(formatted_string)
 
            if i == x - 1: # if calculations are done print calculated pi and save some text
            #   print(i + 1)
                # print(piOn4 * 4)
                writeInFile = True
            # print("this is " + str(i + 1) + " calculation")
            # import os
            # os.system('cls') # to clear shit and show realtime py calculations (take a lot of memory)

        #make function close

        if writeInFile:
            # textFile.write(str(piOn4 * 4) + " this is " + str(i + 1) + " calculation")
            print("yyy")
            textFile.write("yo")
            textFile.close()

    def pow(base, exponent):
        result =  1;
        for i in range(exponent):
            result = result * base
            if i == exponent - 1:
                return result

    def log(baseNum, numToLog):
        result = 1
        alt_i = 1
        for i in range(mathClass.pow(baseNum, alt_i + 1)):
            alt_i = i
            if(numToLog / mathClass.pow(baseNum, i + 1) == 1):
                result = i
                return result + 1

    def log10(numToLog):
        return mathClass.log(10, numToLog)
    # def fileSystem(): # put it in pi and add var for text file for pi to write

    # def main():
        # inputNum = int(input())
        # print()

    # if __name__ == "__main__":
    #   main()

    # inputshit = int(input())
    # myPI(inputshit)
    # pause = input()