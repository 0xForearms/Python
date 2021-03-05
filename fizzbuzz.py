#!/usr/bin/env python3

#some people in discord were talking about fizzbuzz and I had no idea what it was
#so I looked it up and wanted to write my own iteration of it.

#write the numbers from 1 to 100
#for multiples of three, print Fizz instead
#for multiples of five, print Buzz
#for multiples of both three and five, print FizzBuzz


for num in range(1,101):
    if num % 3==0 and num % 5==0:
        print(str(num) + " FizzBuzz")

    elif num % 5==0:
        print(str(num) + " Buzz")
    
    elif num % 3==0:
        print(str(num) + " Fizz")

    else:
        print(str(num))
