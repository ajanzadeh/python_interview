0, 1, 1, 2, 3, 5, 8, 13, 21,

def sequence(a, b, x):
    result = [a,b]

    def calculate(a, b, result, end, counter):
        if counter == None:
            counter = 0
        c = a + b
        counter += 1
        result.append(c)
        if counter < end:
            calculate(b,c,result,end,counter)
        else:
            return result

    calculate(a, b, result, x,None)

    printable = ", ".join(map(str,result))
    return printable

print(sequence(0,1,100))
