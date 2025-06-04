def print_list(lst):
    for i in lst:
        print(i)
print_list(["squirtle", "gengar", "charizard", "pikachu"])

def doubled(lst):
    for i in lst:
        print(2*i)
doubled([1,2,3])

def doubled_new(lst):
    new_lst = []
    for i in lst:
        new_lst.append(2 * i)
    return new_lst
    
print(doubled_new([1,2,3]))

def flip_sign(lst):
    flipped_list = []
    for i in lst:
        flipped_list.append(-1 * i)
    return flipped_list

print(flip_sign([1,-2,-3,4]))

def max_difference(lst):
    list.sort(lst)
    return lst[len(lst)-1] - lst[0]

print(max_difference([5,22,8,10,2]))

def count_less_than(numbers, threshold):
    count = 0
    for i in numbers:
        if i < threshold:
            count += 1
    return count
print(count_less_than([12,8,2,4,4,10],5))

def get_evens(lst):
    evens_lst = []
    for i in lst:
        if i % 2 == 0:
            evens_lst.append(i)
    return evens_lst

print(get_evens([1,2,3,4]))

def multiples_of_five():
    for i in range(1,101):
        if i % 5 == 0:
            print(i)

multiples_of_five()

def find_divisors(n):
    div_lst = []
    for i in range(1,n+1):
        if n % i == 0:
            div_lst.append(i)
    return div_lst

print(find_divisors(144))

        

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(13)

def print_indices(lst):
    for i in range(len(lst)):
        print(i)

print_indices([5,1,3,8,2])

def linear_search(lst, target):
    for i, num in enumerate(lst):
        if num == target:
            return i
    return -1
print(linear_search([1,4,5,2,8],5))
print(linear_search([1,4,5,2,8],10))