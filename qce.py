from random import randint
from pathlib import Path
import os

#SETUP
os.chdir(Path.home() + "\\Measurements")

fin = open("0-SETUP\\Setup.txt", "r")
howManyTimes = 0
words = []
while True:
    string = fin.readline()
    if not string:
        break
    words.append(string)
    howManyTimes += 1

for k in range(howManyTimes):
    word = words[k]
    while True:
        file = str(k + 1) + "-" + word[0] + word[1] + word[2] + word[3] + '-Measurements.txt'

        flag = 0

        def BitSum(a, b):
            for j in range(5):
                if a[j] == b[j]:
                    return 0
                else:
                    return 1

        def BitsFromBasis(Abas, Abit, Bbas):
            if Abas == 0 and Bbas == 0 and Abit == 0:
                return 1
            elif Abas == 0 and Bbas == 0 and Abit == 1:
                return 0
            elif Abas == 0 and Bbas == 1 and Abit == 0:
                return randint(0, 1)
            elif Abas == 0 and Bbas == 1 and Abit == 1:
                return randint(0, 1)
            elif Abas == 1 and Bbas == 0 and Abit == 0:
                return randint(0, 1)
            elif Abas == 1 and Bbas == 0 and Abit == 1:
                return randint(0, 1)
            elif Abas == 1 and Bbas == 1 and Abit == 0:
                return 0
            elif Abas == 1 and Bbas == 1 and Abit == 1:
                return 1


        def BitsToLetter(c):
            if c == "00000":
                return ("A")
            elif c == "00001":
                return ("B")
            elif c == "00010":
                return ("C")
            elif c == "00011":
                return ("D")
            elif c == "00100":
                return ("E")
            elif c == "00101":
                return ("F")
            elif c == "00110":
                return ("G")
            elif c == "00111":
                return ("H")
            elif c == "01000":
                return ("I")
            elif c == "01001":
                return ("J")
            elif c == "01010":
                return ("K")
            elif c == "01011":
                return ("L")
            elif c == "01100":
                return ("M")
            elif c == "01101":
                return ("N")
            elif c == "01110":
                return ("O")
            elif c == "01111":
                return ("P")
            elif c == "10000":
                return ("Q")
            elif c == "10001":
                return ("R")
            elif c == "10010":
                return ("S")
            elif c == "10011":
                return ("T")
            elif c == "10100":
                return ("U")
            elif c == "10101":
                return ("V")
            elif c == "10110":
                return ("W")
            elif c == "10111":
                return ("X")
            elif c == "11000":
                return ("Y")
            elif c == "11001":
                return ("Z")
            else:
                return "404"



        def LetterToBits(c, b):
            if c == "A":
                b.append(0)
                b.append(0)
                b.append(0)
                b.append(0)
                b.append(0)
            elif c == "B":
                b.append(0)
                b.append(0)
                b.append(0)
                b.append(0)
                b.append(1)
            elif c == "C":
                b.append(0)
                b.append(0)
                b.append(0)
                b.append(1)
                b.append(0)
            elif c == "D":
                b.append(0)
                b.append(0)
                b.append(0)
                b.append(1)
                b.append(1)
            elif c == "E":
                b.append(0)
                b.append(0)
                b.append(1)
                b.append(0)
                b.append(0)
            elif c == "F":
                b.append(0)
                b.append(0)
                b.append(1)
                b.append(0)
                b.append(1)
            elif c == "G":
                b.append(0)
                b.append(0)
                b.append(1)
                b.append(1)
                b.append(0)
            elif c == "H":
                b.append(0)
                b.append(0)
                b.append(1)
                b.append(1)
                b.append(1)
            elif c == "I":
                b.append(0)
                b.append(1)
                b.append(0)
                b.append(0)
                b.append(0)
            elif c == "J":
                b.append(0)
                b.append(1)
                b.append(0)
                b.append(0)
                b.append(1)
            elif c == "K":
                b.append(0)
                b.append(1)
                b.append(0)
                b.append(1)
                b.append(0)
            elif c == "L":
                b.append(0)
                b.append(1)
                b.append(0)
                b.append(1)
                b.append(1)
            elif c == "M":
                b.append(0)
                b.append(1)
                b.append(1)
                b.append(0)
                b.append(0)
            elif c == "N":
                b.append(0)
                b.append(1)
                b.append(1)
                b.append(0)
                b.append(1)
            elif c == "O":
                b.append(0)
                b.append(1)
                b.append(1)
                b.append(1)
                b.append(0)
            elif c == "P":
                b.append(0)
                b.append(1)
                b.append(1)
                b.append(1)
                b.append(1)
            elif c == "Q":
                b.append(1)
                b.append(0)
                b.append(0)
                b.append(0)
                b.append(0)
            elif c == "R":
                b.append(1)
                b.append(0)
                b.append(0)
                b.append(0)
                b.append(1)
            elif c == "S":
                b.append(1)
                b.append(0)
                b.append(0)
                b.append(1)
                b.append(0)
            elif c == "T":
                b.append(1)
                b.append(0)
                b.append(0)
                b.append(1)
                b.append(1)
            elif c == "U":
                b.append(1)
                b.append(0)
                b.append(1)
                b.append(0)
                b.append(0)
            elif c == "V":
                b.append(1)
                b.append(0)
                b.append(1)
                b.append(0)
                b.append(1)
            elif c == "W":
                b.append(1)
                b.append(0)
                b.append(1)
                b.append(1)
                b.append(0)
            elif c == "X":
                b.append(1)
                b.append(0)
                b.append(1)
                b.append(1)
                b.append(1)
            elif c == "Y":
                b.append(1)
                b.append(1)
                b.append(0)
                b.append(0)
                b.append(0)
            elif c == "Z":
                b.append(1)
                b.append(1)
                b.append(0)
                b.append(0)
                b.append(1)


        print("   ", file=fout)
        print("*************************************TASK 1*************************************", file=fout)
        print("   ", file=fout)

        AliceBasis = []
        BobBasis = []
        AliceBit = []
        BobBit = []
        Key = []

        for i in range(52):
            AliceBasis.append(randint(0, 1))
            BobBasis.append(randint(0, 1))
            AliceBit.append(randint(0, 1))
            BobBit.append(0)

        for i in range(52):
            BobBit[i] = BitsFromBasis(AliceBasis[i], AliceBit[i], BobBasis[i])

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=TABLES=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)
        for i in range(52):
            a = ""
            b = ""
            if AliceBasis[i] == 0:
                a = "x"
            else:
                a = "+"

            if BobBasis[i] == 0:
                b = "x"
            else:
                b = "+"

            print(str(i + 1) + ". AliceBasis: " + a + ", AliceBit: "
                  + str(AliceBit[i]) + ", BobBasis: " + b
                  + ", BobBit: " + str(BobBit[i]), file=fout)

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=MATCHES=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)
        for i in range(52):
            if (AliceBasis[i] == BobBasis[i]) and (AliceBit[i] == BobBit[i]):
                Key.append(BobBit[i])
                print(str(i + 1) + " :   basis: +, bit: " + str(AliceBit[i]), file=fout)
        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=EXTRA TABLES=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        j = i
        if len(Key) < 20:
            print("   ", file=fout)
            print("There was not enough values. Extra measurements include:", file=fout)
            print("   ", file=fout)
            while len(Key) < 20:
                AliceBasis.append(randint(0, 1))
                BobBasis.append(randint(0, 1))
                AliceBit.append(randint(0, 1))
                BobBit.append(0)
                BobBit[i] = BitsFromBasis(AliceBasis[i], AliceBit[i], BobBasis[i])
                if AliceBasis[i] == 0:
                    a = "x"
                else:
                    a = "+"

                if BobBasis[i] == 0:
                    b = "x"
                else:
                    b = "+"
                print(str(i + 1) + ". AliceBasis: " + a + ", AliceBit: "
                    + str(AliceBit[i]) + ", BobBasis: " + b
                    + ", BobBit: " + str(BobBit[i]), file=fout)
                if (AliceBasis[i] == BobBasis[i]) and (AliceBit[i] == BobBit[i]):
                    Key.append(BobBit[i])
                i += 1

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=EXTRA MATCHES=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        for j in range(i):
            if (AliceBasis[j] == BobBasis[j]) and (AliceBit[j] == BobBit[j]):
                print(str(j + 1) + " :   basis: +, bit: " + str(AliceBit[j]), file=fout)


        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=KEY VALUE=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)
        print(Key, file=fout)
        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=LETTERS FROM KEY=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        cryptoWord = []
        for i in range(0, len(Key), 5):
            if len(Key) >= i + 4:
                letter = (str(Key[i]) + str(Key[i + 1]) + str(Key[i + 2]) + str(Key[i + 3]) + str(Key[i + 4]))
                print(letter + " : " + BitsToLetter(letter), file=fout)
                if BitsToLetter(letter) == "404":
                    flag += 1
                cryptoWord.append(letter)


        print("   ", file=fout)
        print("*************************************TASK 2*************************************", file=fout)
        print("   ", file=fout)

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=YOUR WORD=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        wordInBits = []

        for i in range(4):
            LetterToBits(word[i], wordInBits)

        print("Current word: ", file=fout)

        for i in range(4):
            print(str(i + 1) + " : " + str(word[i]), file=fout)

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=ENCRYPT WORD=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        aliceWord = []


        for i in range(20):
            if Key[i] == wordInBits[i]:
                aliceWord.append(0)
            else:
                aliceWord.append(1)
        cryptoAliceWord = []
        print("Encryption word: ", file=fout)
        for i in range(0, 20, 5):
            if len(Key) >= i + 4:
                aliceLetter = (str(aliceWord[i]) + str(aliceWord[i + 1]) + str(aliceWord[i + 2]) + str(aliceWord[i + 3]) + str(aliceWord[i + 4]))
                print(aliceLetter + " : " + BitsToLetter(aliceLetter), file=fout)
                if BitsToLetter(aliceLetter) == "404":
                    flag += 1
                cryptoAliceWord.append(aliceLetter)

        newWord = []

        for i in range(20):
            if Key[i] == aliceWord[i]:
                newWord.append(0)
            else:
                newWord.append(1)

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=BOB'S WORD=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        print("Bob's word: ", file=fout)
        for i in range(0, len(Key), 5):
            if len(Key) >= i + 4:
                letter = (str(newWord[i]) + str(newWord[i + 1]) + str(newWord[i + 2]) + str(newWord[i + 3]) + str(newWord[i + 4]))
                print(letter + " : " + BitsToLetter(letter), file=fout)
                if BitsToLetter(letter) == "404":
                    flag += 1

        print("   ", file=fout)
        print("*************************************TASK 3*************************************", file=fout)
        print("   ", file=fout)

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=TABLES=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        EvaBasis = []
        EvaBit = []
        NotEqualBits = []
        AliceBasis.clear()
        BobBasis.clear()
        BobBit.clear()
        AliceBit.clear()

        for i in range(52):
            AliceBasis.append(randint(0, 1))
            BobBasis.append(randint(0, 1))
            AliceBit.append(randint(0, 1))
            BobBit.append(0)
            EvaBit.append(0)
            EvaBasis.append(randint(0, 1))

        for i in range(52):
            EvaBit[i] = BitsFromBasis(AliceBasis[i], AliceBit[i], EvaBasis[i])
            BobBit[i] = BitsFromBasis(EvaBasis[i], EvaBit[i], BobBasis[i])
            if AliceBasis[i] == 0:
                a = "x"
            else:
                a = "+"

            if BobBasis[i] == 0:
                b = "x"
            else:
                b = "+"
            if EvaBasis[i] == 0:
                c = "x"
            else:
                c = "+"

            print(str(i + 1) + ". AliceBasis: " + a + ", AliceBit: "
                  + str(AliceBit[i]) + ", EvaBasis: " + c + ", EvaBit: " + str(EvaBit[i]) + ", BobBasis: " + b
                  + ", BobBit: " + str(BobBit[i]), file=fout)

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=MATCHES=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        matches = 0

        for i in range(52):
            if AliceBasis[i] == BobBasis[i]:
                if AliceBasis[i] == 0:
                    a = "x"
                else:
                    a = "+"
                if BobBasis[i] == 0:
                    b = "x"
                else:
                    b = "+"
                print(str(i + 1) + " :   AliceBasis: " + a + ", AliceBit: " + str(AliceBit[i]) + ", BobBasis: " +
                      b + ", BobBit:" + str(BobBit[i]), file=fout)
                matches += 1
                if (AliceBit[i] != BobBit[i] and AliceBasis[i] == 1) or (AliceBit[i] == BobBit[i] and AliceBasis[i] == 0):
                    NotEqualBits.append(i)

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=NOT EQUAL=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        for i in range(len(NotEqualBits)):
            if AliceBasis[NotEqualBits[i]] == 0:
                a = "x"
            else:
                a = "+"
            if BobBasis[NotEqualBits[i]] == 0:
                b = "x"
            else:
                b = "+"
            print(str(NotEqualBits[i] + 1) + " :   AliceBasis: " + a + ", AliceBit: " + str(AliceBit[NotEqualBits[i]]) + ", BobBasis: " +
                  b + ", BobBit:" + str(BobBit[NotEqualBits[i]]), file=fout)

        print("   ", file=fout)
        print("=-=-=-=-=-=-=-=-=-=-=-=MISTAKE CHANCE=-=-=-=-=-=-=-=-=-=-=-=-=", file=fout)
        print("   ", file=fout)

        chance = len(NotEqualBits)/matches
        print(chance, file=fout)
        if flag == 0:
            break
            fout.close()

print("-----------------------------------------")
print("Successfully!")
print("You can view your measurements by this path:")
print("   ")
print("C:\\Users\\Gregory\\Desktop\\Measurements")
print("-----------------------------------------")
