"""Data types"""
"NUMBERS"
integer_num = int(1)
float_num = float(1.1)
float_num_e = float(0.1e4)
complex_num = complex(1 +float_num) # (2.1+0j)
"STRINGS"
string_a = str('A')
string_b = 'B'
"F-string"
string_f = f'{string_a}, {2*2}'; print(string_f)
"LISTS"
list_name = [1,2,3,4,5]; print(list_name)
list_name_add = list_name.append(6) ; print(list_name)
list_name_remove = list_name.remove(3); print(list_name)
"TUPLE"
tuple_name = (1,2,3)
print(1 in tuple_name)
"LIST Comprehension"
new_list = [x+1 for x in list_name]; print(new_list)
"RANGE"
x = list(range(1,10))
print(x)
x = list(range(1,10,2))
print(x)
"Dictionaries"
dict1 = {"a":1,
         "b":2,
         "c":3}
dict1['d'] = 4
print(dict1)
print("c" in dict1)
del dict1['a']
print(dict1)
print('a' not in dict1)
"SETS"
a_set = {"1", 2, 3, 4, (1, 2)}
b_set = {'a', 'b', 'c'}
print(a_set, b_set) #numbers are formed sequentially
c_list = [1,1,2,3,4,4,5]
c_set = set(c_list); print(c_set) #excluding all nonunique elements

"Cycle for"
# define vowel(гласные) from input string:
possible_vowel = ['a','e','o','u','i','y']
vowel_count = 0   # creating counter of possible vowel letters
word = input('write any word:')
for each in word:
    if each in possible_vowel:
        vowel_count += 1
print(vowel_count)

#or my solution:
possible_vowel = ['a','e','o','u','i','y']
vowels_count = []   # creating a list of vowels we found in inputed word, and instantly add them to the list
word = input('write any word:')
for each in word:
    if each in possible_vowel:
        vowels_count.append(each)

print(len(vowels_count))