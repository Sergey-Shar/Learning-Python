num = 0
array = [1, 1, 2, 3, 5, 8]
for i in array:
    num += i
    print(num)

fib1 = 1
fib2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n) - 2

i = 0
while i < n:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение этого элемента:", fib2)

name = input('Ваше имя:')

print('Привет,', name)


def say_hi(name_user):
    print(name_user)


say_hi(name)
