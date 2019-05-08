'''

Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate 
chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite 
efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly K
 consecutive pancakes. That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side 
 pancake, and vice versa; it does not change the left-to-right order of those pancakes.

You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row (since there are raised 
borders on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first K - 1 
pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some 
individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. 
You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy 
side up, so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to 
leave all pancakes happy side up, or state that there is no way to do it.
'''

def oversized_pancake(s, k):
    count_flipped = 0
    s = [char for char in s]

    for index, char in enumerate(s):
        if index + k > len(s): break
        if s[index] == '-':
            for i in range(index, index + k):
                s[i] = '+' if s[i] == '-' else '-'
            count_flipped += 1

    return 'IMPOSSIBLE' if '-' in s[len(s) - k:len(s)] else count_flipped

t = int(input())
for i in range(1, t + 1):
    s, k = input().split(' ')
    result = oversized_pancake(s, int(k))
    print('Case #{}: {}'.format(i, result))