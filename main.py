<<<<<<< HEAD
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
=======
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
>>>>>>> 0459d33a4868dcc4aba7ef67a99de75ef0ed02f6
