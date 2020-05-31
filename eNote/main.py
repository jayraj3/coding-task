from linked_list import SinglyLinkedList

def fibonacci(arr):
    """
    calculate fibonacci sequence

    :param arr: length of fibonacci sequence
    :return: generator object
    """
    fibonacci_1, fibonacci_2 = 0, 1 # base cases for fibonacci sequence

    # Calculation of main Fibonacci sequence
    for i in range(arr):
        if i == 0:
            yield fibonacci_1
        elif i == 1:
            yield fibonacci_2
        else:
            fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2 # calculate next fibonacci number
            yield fibonacci_2

def main():
    List = SinglyLinkedList()  # creating list to store the main Fibonacci sequence

    count = 100
    cal_fib = fibonacci(count)  # fibonacci generator object

    # add data in linked list
    for i in range(100):
        List.insert(next(cal_fib))

    print(List)  # print linked list data
    List.reverse()  # reverse linked list
    print(List)  # print reverse linked list

if __name__ == '__main__':
    main()




