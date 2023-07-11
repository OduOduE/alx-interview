#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    ''' Finds fewest possible ops for n H chars in a file. '''
    pasted_chars = 1 # number of chars in file
    clipboard = 0   # number of copied H
    counter = 0     # ops counter

    while pasted_chars < n:     # Looping through to n
        if clipboard == 0:  # if nothing is copied yet
            clipboard = pasted_chars    # copyall
            counter += 1    # increment ops counter

        if pasted_chars == 1:    # if no pasting yet
            pasted_chars += clipboard    # paste
            counter += 1    # increment ops counter
            continue        # go to the next loop

        remaining = n - pasted_chars  # remaining chars to paste
        ''' Check if its possible to copy and paste accordingly, by
        looking if clipboard has more than the required capacity; or
        if num of chars in file is equal or more than in clipboard.
        '''
        if remaining < clipboard:
            return 0

        if remaining % pasted_chars:    # if its indivisible
            pasted_chars += clipboard   # paste current clipboard
            counter += 1   # increment counter

        else:       # if it is divisible
            clipboard = pasted_chars    # copy
            pasted_chars += clipboard   # paste
            counter += 2    # increment by the 2 previous steps

    if pasted_chars == n:   # For desired result
        return counter      # return number of ops
    else:                   # Failure
        return 0
