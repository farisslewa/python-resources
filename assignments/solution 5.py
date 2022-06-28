def square():
  while True:
    try:
      num = int(input('Please enter a number: '))
    except:
      print('Wrong input, please enter a valid number')
    else:
      print(f'the squared value of {num} is {num**2}')
      break

square()