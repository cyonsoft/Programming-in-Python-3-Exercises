import random

while True:
    try:
        rows = int(input('rows: '))
        cols = int(input('columns: '))
        minimum_input = input('minimum (or enter for 0): ')
        maximum_input = input('maximum (or enter for 1000): ')

        if minimum_input != '':
            min = int(minimum_input)
        else:
            min = 0

        if maximum_input != '':
            max = int(maximum_input)
        else:
            max = 1000

        row = 0
        while row < rows:
            col = 0
            line = []
            while col < cols:
                line.append(random.randint(min,max))
                col += 1
            print(line)
            row += 1
        break

    except ValueError as Err:
        print(Err)
        continue
