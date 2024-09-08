#!/usr/bin/python3
# creating pascal triangle
''' pascal triangle '''


def pascal_triangle(n):
    """ the only function """
    # i = 0
    holder = []
    if n <= 0:
        return []
    else:
        for i in range(1, n+1):
            C = 1
            subholder = []
            for j in range(1, i+1):
                subholder.append(C)
                C = C * (i - j) // j
            holder.append(subholder)
    return holder
