#1- having string 'hello' use indexing and reverse indexing to get the letter 'e'
myvar1 = 'hello'
print(myvar1[1])
print(myvar1[-4])

#2- [1,2,[3,4,'dog']]  change the word 'dog' to 'cat'
myvar2 = [1,2,[3,4,'dog']]
myvar2[2][2] = 'cat'
print(myvar2)

#3- grap the word 'hello' from these dictionaries:
#  {'k':'hello'}
myvar3 = {'k':'hello'}
result = myvar3['k']
print(result)
#  {'k1':{'k2':'hello'}}
myvar4 = {'k1':{'k2':'hello'}}
result = myvar4['k1']['k2']
print(result)
#  {'k1':[1,2,{'k2':{'k3':'hello'}}]}
myvar5 = {'k1':[1,2,{'k2':{'k3':'hello'}}]}
result = myvar5['k1'][2]['k2']['k3']
print(result)