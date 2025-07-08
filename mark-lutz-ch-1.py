print('uday')     # The print function prints any string or variable.
print('today is saturday')
print('tomorrow is sunday')
print(2**10)

str = 'uday'
print(str)   # str is a variable and uday is a string which is the value assigned to the variable

str2 = 'debnath'
print(str2)
print('str2')   # In this case str2 will be printed as a string because of the quotation marks.

a = 2
b = 3
c = a+b
print(c)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a%b)
print(int(a/b))       # prints only the integer part of the operation
print(float(a/b))     # prints only the decimal part of the operation

print(3+2j + 2+3j)       # complex numbers (addition)
print(2+3j * 3+2j)                        # (multiplication)

import math
a = 16
b = math.sqrt(a)
print(b)
print(math.sqrt(9))     # square root of a number
print(9**0.5)            #OR
l = [123, 'abc', 2.22]
print(len(l))         #prints the length of the string
print(l)
print(l + [1,2,3])

M = [[1,2,3],[2,3,4],[3,4,3]]    #A 3by3 matrix as nested list
print(M)
print(M[1])                  #prints the 2nd row

col2 = [row[1] for row in M]           #prints column 2
print(col2)

col3 = [row[2] for row in M]           #column 3
print(col3)
print( [row[1] + 1 for row in M])         # adds 1 to each element in 2nd row

diag = [M[i][i] for i in [0, 1, 2]]          #prints diagonal elements
print(diag)
print(sum(diag))                             #sum of diagonal elements
