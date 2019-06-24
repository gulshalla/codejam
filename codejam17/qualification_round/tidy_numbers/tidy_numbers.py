'''
Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils 
are sorted from shortest to longest and her computers from oldest to newest. One day, when 
practicing her counting skills, she noticed that some integers, when written in base 10 with 
no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 
8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this 
property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the 
last tidy number she counted?
'''

def tidy_numbers(n):
    n = [int(char) for char in n]
    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]:
            n[i] -= 1
            for j in range(i + 1, len(n)):
                n[j] = 9
    return int(''.join([str(x) for x in n]))

t = int(input())
for i in range(1, t + 1):
    n = input()
    result = tidy_numbers(n)
    print('Case #{}: {}'.format(i, result))


