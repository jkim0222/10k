import random
import math
import operator

n = 10000

def show(data):
    print(data)

def fill(data):
    for i in range(n):
        data.append(random.randint(1, n))

def check_dup(data, duplicated):
    dup = 0
    for i in range(1, n):
        if data[i] != data[i - 1]:
            if dup:
                dup = 0
        else:
            if dup == 0:
                dup = 2 # Initialize with 2
            else:
                dup += 1
            duplicated.update({data[i]:dup})

def main(debug):
    data = []
    fill(data)
    if debug > 1: show(data)
    data.sort()
    if debug > 1: show(data)
    print("[1] Min, Max =", data[0], data[n-1])
    print("[2] Already sorted,", data[0], data[1], data[2], "...")

    sum = 0.0
    squared_sum = 0.0
    squared_variance_sum = 0.0
    for i in range(n):
        sum += data[i]
    average = sum / i
    for i in range(n):
        squared_sum += data[i] * data[i]
        variance = average - data[i]
        squared_variance_sum += variance * variance
    print("[3-1] Average, standard deviation =", average, math.sqrt(squared_variance_sum / n))
    print("[3-2] Average, standard deviation =", average, math.sqrt(squared_sum / n - average * average))

    duplicated = {}
    check_dup(data, duplicated)
    if debug > 1: show(duplicated)
    n_duplicated = len(duplicated)
    print("[4] There are", n_duplicated, "numbers appeard more than 2 times.")


    dup_sorted = sorted(duplicated.items(), key=operator.itemgetter(1))
    if debug > 1: show(dup_sorted)
    print("[5] ", end = '')
    tied = 0
    for i in range(1, n_duplicated):
        if dup_sorted[n_duplicated - i][1] != dup_sorted[n_duplicated - i - 1][1]:
            break
        else:
            if tied: print(", ", end = '')
            print(dup_sorted[n_duplicated - i][0], end = '')
            tied += 1
    if tied: print(" and", end = ' ')
    print(dup_sorted[n_duplicated - i][0], "appeard", dup_sorted[n_duplicated - 1][1], "times.")

    dup_sorted.reverse()
    if debug > 1: show(dup_sorted)

    print("[6] ", end = '')
    for i in range(10):
        if i > 0 and i < 10: print(", ", end = '')
        print("(" + str(dup_sorted[i][0]) +  ", " + str(dup_sorted[i][1]) + ")", end = '')
    print(" are the top 10 tuples.")

main(2)