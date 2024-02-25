def square_generator(N):
    for i in range(N + 1):
        yield i**2

N = 5
squares_up_to_N = square_generator(N)

for square in squares_up_to_N:
    print(square)
#task1


def even_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter the value of n: "))

even_numbers_up_to_n = even_generator(n)
result = ', '.join(map(str, even_numbers_up_to_n))
print(result)        
#task2


def divisible_by_3_and_4_generator(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 20
result_generator = divisible_by_3_and_4_generator(n)

for number in result_generator:
    print(number)
#task3


def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a, b = 1, 5  
for square in squares(a, b):
    print(square)
#task4


def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = 5
for number in countdown(n):
    print(number)
#task5    


    

