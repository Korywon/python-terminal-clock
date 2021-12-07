#!/usr/bin/python3

import time

if __name__ == '__main__':
    time_str = str(input('Enter starting time: '))

    tokens = time_str.split(':')                        #split time into tokens

    hours = int(tokens[0])
    minutes = int(tokens[1])
    seconds = int(tokens[2])

    while True:
        print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
        time.sleep(1)
        seconds += 1

        if seconds > 59:                                          #wrap seconds
            seconds = 0
            minutes +=1
        if minutes > 59:                                          #wrap minutes
            minutes = 0
            hours += 1
        if hours > 23:                                              #wrap hours
            hours = 0
