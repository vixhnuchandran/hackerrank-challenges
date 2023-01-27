''' 
# TIME CONVERSION

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

  s = '12:01:00PM'
  Return '12:01:00'.
  
  s = '12:01:00AM'
  Return '00:01:00'.

Function Description
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
timeConversion has the following parameter(s):

string s: a time in 12 hour format
Returns

string: the time in 24 hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.hh:mm:ssAM  or hh:mm:ssPM).


Sample Input 0
07:05:45PM
Sample Output 0
19:05:45
'''









#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s[:-2]
    hours, minutes, seconds = time.split(":")

    if "AM" in s:
        if hours == '12':
            hours = '00'
    elif "PM" in s:
        if hours != '12':
            hours = str(int(hours) + 12)
    time = ":".join([hours, minutes, seconds])
    return time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

=======
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s[:-2]
    hours, minutes, seconds = time.split(":")

    if "AM" in s:
        if hours == '12':
            hours = '00'
    elif "PM" in s:
        if hours != '12':
            hours = str(int(hours) + 12)
    time = ":".join([hours, minutes, seconds])
    return time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

>>>>>>> 12ae9d3d78172ca3677deca0f65cc9923ce987ad
