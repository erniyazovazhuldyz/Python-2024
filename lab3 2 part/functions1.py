def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = 200
ounces_required = grams_to_ounces(grams)

print("grams: ", grams)
print("ounces: ", ounces_required)
#task1

def f_to_c(n):
    c = (5/9) * (n-32)
    return c
F=int(input("enter Fahrenheit temperature: "))
ctemp = f_to_c(F)
print("Fahrenheit temperature to centigrade: ", ctemp)
#task2

def solve(numheads, numlegs):
    num_chikens=0
    num_rabbits=0
    for num_chikens in range(numheads+1):
        num_rabbits=numheads-num_chikens
        totalleg = 2*num_chikens + 4*num_rabbits
        if totalleg == numlegs:
            return num_rabbits, num_chikens
    return None
res=solve(35,94)
if res:
    num_rabbits, num_chikens = res
    print("number of rabbits: ", num_rabbits)
    print("number of chikens: ", num_chikens)
else:
    print("No solution")
#task3
    
def is_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15]
b=list()
for i in a:
    if is_prime(i):
        b.append(i)
    else:
        continue
for i in b:
    print(i)
#task4    

s=input("enter a string: ")
def permituation(s,c=""):
    if len(s) == 0:
        print(c)
    else:
        for i in range(len(s)):
            char=s[i]
            remining=s[:i]+s[i+1:]
            permituation(remining, c+char)
print("permituations of the string: ")
permituation(s)
#task5  

def reverse(sentence):
    words=sentence.split()
    reversed_words= reversed(words)
    reversed_sent = ""
    for word in reversed_words:
        reversed_sent += word + " "
    return reversed_sent
sentence = input("enter a sentence: ")
reverse = reverse(sentence)
print("reversed sentence: ", reverse)
#task6 

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
nums=[1, 3, 3]
print(has_33(nums))
nums=[1,3,1,3]
print(has_33(nums))
nums=[3,1,3]
print(has_33(nums))
#task7 

def spy_game(nums):
    b=[]
    c=[]
    for i in range(len(nums)):
        if nums[i]==0 or nums[i]==7:
            b.append(nums[i])
            c.append(nums[i])
    c=sorted(c)
    if b==c:
        return True
    return False
nums=[1,2,4,0,0,7,5]
print(spy_game(nums))
nums=[1,0,2,4,0,5,7]
print(spy_game(nums))
nums=[1,7,2,0,4,5,0]
print(spy_game(nums))   
#task8

def sphere(r):
    v=(3*3.14*int(r**3))/4
    return v
r=int(input())
print(sphere(r)) 
#task9

def unique(list):
    unique_list=[]
    for i in list:
        is_unique=True
        for j in unique_list:
            if i==j:
                is_unique=False
                break
        if is_unique:
            unique_list.append(i)
    return unique_list

list=[1, 3, 2, 1, 3, 5]
print(unique(list))
#task10

def is_polindrome(s):
    d=s[::-1]
    if d!=s:
        return False
    return True
s=input("enter a string: ")
print(is_polindrome(s)) 
#task11

def histogram(list):
    for i in list:
        print("*"*i)
list=[4,9,7]
histogram(list)
#task12

import random
def guess():
    secret_number=random.randint(1,20)
    print("Hello! What is your name?")
    name=input("enter your name: ")
    print("Well, "+name+", I am thinking of a number between 1 and 20.")
    sum=0
    while True:
        print("Take a guess.")
        guess=int(input())
        sum+=1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Good job, " + name+ "!You guessed my number in " +str(sum)+ " guesses!")
            break
guess() 
#task13

