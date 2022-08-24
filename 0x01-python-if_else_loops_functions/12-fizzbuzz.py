#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print(f"FizzBuzz", end=" ")
        elif i % 5 == 0:
            print(f"Buzz", end=" ")
        elif i % 3 == 0:
            print(f"Fizz", end=" ")
        else:
            print(f"{i}", end=" ")
