import sys

Zero = ["  ***  ",
        " *   * ",
        " *   * ",
        " *   * ",
        " *   * ",
        " *   * ",
        "  ***  "]
One = ["  *  ",
       " **  ",
       "  *  ",
       "  *  ",
       "  *  ",
       "  *  ",
       " *** "]
Two = ["  ***  ",
       " *   * ",
       " *  *  ",
       "   *   ",
       "  *    ",
       " *     ",
       " ***** "]
Three = ["  ***  ",
         " *   * ",
         "     * ",
         "   **  ",
         "     *" ,
         " *   * ",
         "  ***  "]
Four = ["     *  ",
        "    **  ",
        "   * *  ",
        "  *  *  ",
        " ****** ",
        "     *  ",
        "     *  "]
Five = [" ***** ",
        " *     ",
        " *     ",
        "  ***  ",
        "     * ",
        " *   * ",
        "  ***  "]
Six = ["  ***  ",
       " *   * ",
       " *     ",
       " ****  ",
       " *   * ",
       " *   * ",
       "  ***  "]
Seven = [" ***** ",
         "     * ",
         "    *  ",
         "   *   ",
         "  *    ",
         " *     ",
         " *     "]
Eight = ["  ***  ",
         " *   * ",
         " *   * ",
         "  ***  ",
         " *   * ",
         " *   * ",
         "  ***  "]
Nine = ["  **** ",
        " *   * ",
        " *   * ",
        "  **** ",
        "     * ",
        "     * ",
        "  ***  "]
number = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

original_number = sys.argv[1] #input('input your integer')
line = 0

try:
    while line < 7:
        printing_number = ''
        for each_number in original_number:
            number_location = int(each_number)
            printing_number += number[number_location][line]
            printing_number = printing_number.replace('*',each_number) + ' '
        print(printing_number)
        line += 1

except ValueError as err:
    print(err)
