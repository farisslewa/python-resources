#1- write a function that calculate the volume of a sphere (4/3 * pi * r^3) given its radius
def vol(r):
  pi = 3.14
  return 4 / 3 * pi * r**3

print(vol(2))


#2- write a function that check whether a num is within a range (inclusive low and high)
def check(num, low, high):
  return num in range(low, high + 1)

print(check(9, 1, 10))


#3- write a function that accepts a string and calculate the number of uppercase letters and number of lowercase letters
st = 'Hello Mr. Faris, hope you are good at this fine Friday.'
def up_low(s):
  lower = 0
  upper = 0
  for char in s:
    if char.islower():
      lower += 1
    elif char.isupper():
      upper +=1
  print(f'number of uppercase letters = {upper}, and number of lowercase letters = {lower}')
up_low(st)


#4- write a function that takes a list and return a list of unique items of first list
first_list = [1,1,1,1,1,2,2,2,3,3,3,4,4]
def unique_list(lst):
  return list(set(lst))

print(unique_list(first_list))


#5- write a function that takes a list of numbers and return the multiply of all numbers in a list
numlist = [2,3,5,-10]
def mulnum(lst):
  result = 1
  for num in lst:
    result *= num
  return result

print(mulnum(numlist))
