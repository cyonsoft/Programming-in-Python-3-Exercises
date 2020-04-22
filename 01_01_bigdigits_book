# Chapter 1, Sample 01

import sys

Zero = [" *** ",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        " *** "]
One = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]
Two = [" *** ",
       "*   *",
       "*  * ",
       "  *  ",
       " *   ",
       "*    ",
       "*****"]
Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four = ["    * ",
        "   ** ",
        "  * * ",
        " *  * ",
        "******",
        "    * ",
        "    * "]
Five = ["*****",
        "*    ",
        "*    ",
        " *** ",
        "    *",
        "*   *",
        " *** "]
Six = [" *** ",
       "*   *",
       "*    ",
       "**** ",
       "*   *",
       "*   *",
       " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine = [" ****",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        " *** "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]    #sys.argv[]是外部获得数列。参数0代表自身，默认；参数1代表第一个获得。
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row].replace('*', digits[column]) + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("Usage: bigdigits.py <numbers>")
except ValueError as err:
    print(err, "in", digits)
