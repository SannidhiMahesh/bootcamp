#itterator 
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Counter(1, 10)
for number in counter:
    print(number) 

print("-----------------------------")
print("square of number\n")
#generator
#square of numbers from 1 to n

def simple_generator(n):
    for i in range(1, n + 1):
        yield i * i


for square in simple_generator(8):
    print(square) 


print("----------------------------------\n")

#decorator
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello! this is a example of decorator")


say_hello()

print("------------------------------------")


#filters

print("this if filter\n")
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  

print("------------------------------------")

print("map function\n")
#map

numbers = [1, 2, 3, 4,5,6]
doubled_numbers = map(lambda x: x * 2, numbers)

print(list(doubled_numbers)) 

print("--------------------------------------")
print("reduce function\n")
#reduce
from functools import reduce

numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_of_numbers)  




