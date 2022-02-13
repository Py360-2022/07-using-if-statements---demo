# using functions from another file
# pmcampbell
# 2022-02-05

import funcs  

num = int(input('Enter a number: '))

print(funcs.square(num))

print(f'square of 5: {funcs.square(5)}')
print(f'square of 11.1: {funcs.square(11.1)}')

# note you can also  import as follows   
#
# import all functions in func.py, use:
# from funcs import * 
# squre(15)
# 
# import only square from func.py, use: 
# with this you cannot use greeting()
# from funcs import square   
# square(10)