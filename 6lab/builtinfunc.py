import time
import math
#1task
def mult_list(n):
    return math.prod(n)
#2task
def cnt_case(txt):
    upper = sum(1 for i in txt if i.isupper())
    lwr = sum(1 for i in txt if i.islower())
    return upper, lwr
#3task
def is_palindrome(txt):
    return "palindrome" if txt == txt[::-1] else "not palindrome"
#4task
def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    return math.sqrt(num)
#5task
def all_true(m):
    return all(m)
#examples
print(mult_list([1, 2, 3, 4, 5])) 
#2 
print(cnt_case("AlmAtY"))  
#3
print(is_palindrome("wow"))
#4
print(delayed_sqrt(25100, 2123))  
#5
print(all_true((True, True, False)))  
