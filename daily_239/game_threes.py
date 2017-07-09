import sys

# parse commandline args

if (len(sys.argv) != 2):
    start_num = int(input("Please enter starting number: "))
else:
    start_num = int(sys.argv[1])

# initialize variables
cur_num = start_num
num_steps = 0

# while loop to increment through each step
# since the loop stops at 1 and does not go negative, testing for divisibility by 3
# yields only three possible cases.
while (cur_num > 1):
    # if number has a remainder of 2, add 1 to make it divisible by 3
    if (cur_num % 3 == 2):
        print(str(cur_num) + ': +1')
        cur_num += 1
    # if number has a remainder of 1, add subtract 1 to make it divisible by 3
    elif (cur_num % 3 == 1):
        print(str(cur_num) + ': -1')
        cur_num -= 1
    # if number has a remainder of 0, it is divisible by 3
    else:
        print(str(cur_num) + ':  0')
        cur_num /= 3
    num_steps += 1
if(num_steps<1):
    print("Invalid input, please try again.")
else:
    print("Completed in " + str(num_steps) + " step(s)")
