# flt
# Description:
#
# Created by Thomas John Wesolowski <wojoinc@iastate.edu> on 1/11/18
import random

num, certainty = input("Enter the number and certainty desired: ").split(' ')

num = int(num)
certainty = float(certainty)

count = 0
while 1 - 1/ pow(2, count) < certainty:
    a = random.randint(0, num)
    if(pow(a,num,num) != a):
        print(False)
        exit()
    else:
        count += 1
print(True)
print(count, "iterations to arrive at desired certainty")
