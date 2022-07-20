#1- use for .split() if and another thing to print out the word that starts with s 
st1 = 'print only the words that starts with s in this sentence like Sam'

for word in st1.split():
  if word[0].lower() == 's':
    print (word)



#2- use range to print out the even numbers from 0 to 10 (included)

print(list(range(0,11,2)))



#3- use list comprehension to create a list of numbers from 0 to 50 that are divisible by 3

mylist = [num for num in range(1,51) if num % 3 == 0]
print(mylist)




#4- go through the sentence below if the number of letters in a word is even print (the word) is EVEN
st2 = 'print every word in this sentence that has an even number of letters'

for word in st2.split():
  if len(word) % 2 == 0:
    print(f'{word} is EVEN')




#5- use list comprehension to create a list of the first letter of every word in the below sentence.
st3 = 'create a list of the first letters of every word in this sentence'

mylist = [word[0] for word in st3.split()]
print(mylist)