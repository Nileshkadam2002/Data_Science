# %%
#Even or Odd
def Even_or_Odd(n):
    return ['even' if i%2==0 else 'odd' for i in n ]
Even_or_Odd([78,67,44,1,3,2])   

# %%
#Sum of Positive Numbers
def sum_of_positive(n):
    return sum(num for num in n if num>0 )

sum_of_positive([2,3,4,5,66,-55,-44,-67])
    

# %%
#Reversed String
def reversed_string(s):
    return s[::-1]
reversed_string("121")  
reversed_string("Nilesh")

# %%
#Count Vowels
def Count_Vowels(g):
    counte=0
    g.lower()
    vowel='aeiou'
    for i in g:
        if i in vowel:
            counte+=1
    return counte   
Count_Vowels("kales")      

# %%
#Find the Smallest Integer
def find_smallest_int(i):
    return min(i)
find_smallest_int([2,3,4,5,6,6])    

# %%
#Square Every Digit
def Square_Every_Digit(s):
    n=str(s)
    result=""
    for i in n:
        p=int(i)**2 
        result+=str(p)
    return int(result)    
Square_Every_Digit(567)        
    

# %%
#Remove space
def Remove_Spaces(s):
    t=s.replace(" ","")
    return t

Remove_Spaces(" Hello THIS IS ")
    

# %%
#Sum Without Highest and Lowest Number
def Sum_Number(n):
    return sum(n[1:-1])
Sum_Number([1,2,3,4,5,100])    

# %%
#Find the Middle Character(s)
def Middle_char(s):
    l=len(s)
    mid=l//2
    if l%2==0:
        return s[mid-1:mid+1]
    else:
        return s[mid]
Middle_char("Nilesh")        

# %%
#Sum of Multiples of 3 or 5
def Multiples_of_3_or_5(n):
    total=0
    for i in range(n):
        if i%3==0 or i%5==0:
            total+=i
    return total        

Multiples_of_3_or_5(10)


# %%
def has_repeted_char(s):
    return len(s)!=len(set(s))

has_repeted_char("Happy")
        

# %%
print("hi")

# %%
#Remove First and Last Character
def remove_f_l(s):
    return s[1:-1]
remove_f_l("Python")

# %%
def opposite_num(n):
    if n<0:
        return abs(n)
    else:
        return -n
print(opposite_num(-9)) 
opposite_num(9)   
    
    

# %%
#Convert String to Number
def convert_to_Number(s):
    return int(s)

convert_to_Number("475")

# %%
#Sum of Differences in Array
def sum_of_difference(n):
    if len(n)<2:
        return 0
    n.sort(reverse=True)
    total=0
    for i in range(len(n)-1):
        total+=n[i]-n[i+1]
    return total    
sum_of_difference([1,2,34,3,22])





# %%
#remove the smallest number
def remove_smallest_num(n):
    n.sort()
    return n[1:]
remove_smallest_num([6,5,4,3,4,544,33])

# %%
def count_digit(n):
    return len(str(abs(n)))
count_digit(234)


# %%
def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result

# Examples
print(double_char("abc"))    # Output: aabbcc
print(double_char("Hi!"))    # Output: HHii!!


# %%
def opposite_number(n):
    return -n

# Examples
print(opposite_number(14))   # Output: -14
print(opposite_number(-34))  # Output: 34
print(opposite_number(0))    # Output: 0


# %% [markdown]
# # Basic Python

# %%
## Add Two Numbers in Python
a=57
b=76
c=a+b
print(c)

# %%
def validate_hello(greeting):
    #your code here
    greetings=["hello","ciao","salut","hallo","hola","ahoj","czesc"]
    greeting=greeting.lower()    
    return any(word in greeting for word in greetings)
validate_hello("hello")

# %%
def lovefunc(flower1,flower2):
    return (flower1+flower2)%2==1
lovefunc(23,4)

# %%
def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)    

maximum([1,55,44,33,44,56])
minimum([66,55,44,3,22])

# %%
#9 — Opposite Number
def opposite_number(n):
    return -n
opposite_number(-9)
opposite_number(9)

# %%
f=[45,32,45,6,4,22,55,66]
f.sort()
max(f)-min(f)


# %%
#Find the Difference Between Max and Min
def dif_max_min(n):
    return max(n)-min(n)


dif_max_min([45,32,45,6,4,22,55,66])    

# %%
#Number to Reversed List of Digits
def Reversed_List_Digits(n):
    n.replace('',' ')
    l=list(map(int,n))
    return l[::-1]
Reversed_List_Digits("78278")    

# %%
#Number to Reversed List of Digits
t=5674
t=str(t)
t.replace('',' ')
p=list(map(int,t))
p[::-1]

# %%
def digitize(n):
    return [int(i) for i in str(n)][::-1]

# Examples
print(digitize(348597))  # Output: [7, 9, 5, 8, 4, 3]
print(digitize(12345))   # Output: [5, 4, 3, 2, 1]
print(digitize(0))       # Output: [0]


# %%
#count the Number of Words
def count_Num_of_Words(s):
    return len(s.split())
count_Num_of_Words("Python is awesome")


# %%
#Count the Number of Words
l="Python is awesome"
m=l.split()
len(m)



# %%
#Find the Average of a List
def Average_of_List(l):
    return l


# %%
l=[2,56,7,8,'hjjg']


# %%
def count_case(s):
    upper = 0
    lower = 0

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower

# Examples
u, l = count_case("Hello World")
print("Uppercase:", u, "Lowercase:", l)

u, l = count_case("Python ROCKS")
print("Uppercase:", u, "Lowercase:", l)

u, l = count_case("123 @!")
print("Uppercase:", u, "Lowercase:", l)

        


# %%
#Check Palindrome
def Check_Palindrome(s):
    return s[::-1]==s

Check_Palindrome("nayan")
Check_Palindrome("madam")
Check_Palindrome("123")


# %%
#Find the Longest Word
def Longest_Word(s):
    word=s.split()
    Longest_w=''
    max_len=0
    for i in word:
        current_len=len(i)
        if current_len>max_len:
            max_len=current_len
            Longest_w=i
    return Longest_w

Longest_Word("i THINK YOU ARE LIER")
            

    

# %%
l="I hate programming"

p=l.split()
Longest_Word=''
max_len=0
for i in p:
    current_len=len(i)
    if current_len>max_len:
        max_len=current_len
        Longest_Word=i
print(Longest_Word)        
   


# %%
#Sum of Cubes
def Sum_of_Cubes(n):
    result=0
    for i in range(0,n):
        i+=1
        result+=i**3
        
    return result
Sum_of_Cubes(3)   

# %%
def Sum_of_Cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

print(Sum_of_Cubes(3))  # Output: 36


# %%



