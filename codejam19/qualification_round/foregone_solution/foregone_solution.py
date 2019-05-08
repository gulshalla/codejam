'''
Problem
Someone just won the Code Jam lottery, and we owe them N jamcoins! However, when we tried to print out an oversized 
check, we encountered a problem. The value of N, which is an integer, includes at least one digit that is a 4... and 
the 4 key on the keyboard of our oversized check printer is broken.

Fortunately, we have a workaround: we will send our winner two checks for positive integer amounts A and B, such that
neither A nor B contains any digit that is a 4, and A + B = N. Please help us find any pair of values A and B that satisfy 
these conditions.
'''

def forgone_solution(n): 
    b = ['0'] * len(n)

    for i in range(len(n)):
        if n[i] == '4': b[i] = '1'

    b = int(''.join(b))
    a = int(n) - b 

    return (a, b)

t = int(input())
for i in range(1, t + 1):
    n  = input()
    A, B = forgone_solution(n)
    print("Case #{}: {} {}".format(i, A, B))
