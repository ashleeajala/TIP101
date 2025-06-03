print("Hello, World!")
print(100)
s = "Welcome to CodePath!"
num = 7
print(s)
print(num)
lst = ["TIP101", "TIP102", 102]
print(lst)
x = 5
y = 9
print(x+y)
lst = ["Feranmi", "Toni", "Irede", "Asheoluwa"]
lst_length = len(lst)
print(lst)
print(lst_length)

s = "Ashlee"
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print (fruit)

for num in range(0,10,2):
    print(num)

# lst = [1,2,3,4]
lst = [] # empty list
for i in range(10):
    lst.append(i)
print(lst)

num_lst = [4, 2, 10, -3, 99, 87]
print(num_lst)
num_lst.sort()
print(num_lst)

letter_lst = ['fe', 'xa', 'zg', 's', 't']
letter_lst.sort()
print(letter_lst)

num_lst = [1,2,3,4,5]
num_lst.insert(2,2.5)
# print(num_lst)
num_lst.remove(2.5)
# print(num_lst)
num_lst.pop(0)
# print(num_lst)
x = num_lst.copy()
# print(x)

print(abs(-64.5))

# Enumerate() in Python:
a = ["Asheoluwa", "Tanitoluwa", "Ajala"]
# Iterating list using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Converting to a lsit of tuples
print(list(enumerate(a)))

def hello_world():
    print("Hello World!")
hello_world()

def todays_mood():
    mood = "😎"
    print (f"Today's mood: {mood}")
todays_mood()

def print_menu(menu):
    print("Lunch today is: " + menu)
print_menu("Chicken wings")

def sum(a,b):
    return a + b
print(2 * sum(20,2))

def product(a,b):
    print(a * b)

product(12,2)

def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"

print(classify_age(32))

def what_time_is_it(hour):
    if hour == 2:
        return "taco time"
    elif hour == 12:
        return "peanut butter jelly time"
    else:
        return "nap time"
time = what_time_is_it(1)
print(time)

def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("Nice hand!")
    else:
        print("Hit me!")
blackjack(1)

def get_first(lst):
    if lst == []:
        return None
    else:
        return lst[0]

# print(get_first([8,0]))


def counter(stop):
    for i in range(1, stop + 1):
        print(i)

counter(4)

def sum_ten():
    sum = 0
    for i in range(1,11):
        sum += i
    return sum

print(sum_ten())

def sum_positive_range(stop):
    sum = 0
    for i in range(1,stop + 1):
        sum += i
    return sum
print(sum_positive_range(6))

def sum_range(start, stop):
    sum = 0
    for i in range (start, stop + 1):
        sum += i
    return sum

print(sum_range(3,9))

def print_negatives(lst):
    for i in lst:
        if i < 0:
            print(i)

print_negatives([3,-2,2,1,-5])


