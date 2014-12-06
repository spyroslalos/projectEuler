#! /usr/bin/python2.6

max_c, max_el = 0, 0
for count in range(13,1000000):
    i = 1
    tmp = count
    while tmp > 1:
        if tmp %2 == 0:
            i += 1
            tmp /= 2
        else:
            i += 1
            tmp = 3*tmp + 1
    if i > max_c:
        max_c = i
        max_el = count

print max_el, max_c 
