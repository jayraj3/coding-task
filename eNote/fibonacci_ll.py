from linked_list import SinglyLinkedList

def fibonacci(arr):
    """
    calculate fibonacci sequence

    :param arr: length of fibonacci sequence
    :return: generator object
    """
    f1, f2 = 0, 1
    for i in range(0,arr):
        if i == 0:
            yield f1
        elif i == 1:
            yield f2
        else:
            f1, f2 = f2, f1 + f2
            yield f2

def fib(arr):
    """
    calculate fibonacci sequence
    :param arr: number of sequence
    :return: list of fibonacci sequence
    """
    sequence = [0,1]

    if arr==0:
        return [0]
    elif arr==1:
        return  sequence

    for i in range(arr):
        ans = sequence[i] + sequence[i+1]
        sequence.append(ans)

    return sequence

List = SinglyLinkedList()   # create linked list object
List1 = SinglyLinkedList()

cal_fib = fibonacci(100)
#List.insert(next(cal_fib))

for i in range(100):
    List.insert(next(cal_fib)) # add data in linked list

print(List) # print linked list data
List.reverse()  # reverse linked list
print(List) #print revrse linked list

list_1 = fib(2)
for i in range(4):
    List1.insert(list_1[i])

print(List1)
List1.reverse()
print(List1)

