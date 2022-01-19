# Exercises from Prof Amir Jafari

#%%
# =================================================================
# Class_Ex1: 
# Write python program that converts seconds to 
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------
userin = int(input("How many seconds?"))
print(f'You said {userin} seconds')
print(f'That is the same as {userin /60} minutes\n')
print(f'That is the same as {userin /3600} hours\n')



#%%
# =================================================================
# Class_Ex2: 
# Write a python program to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
# ----------------------------------------------------------------
my_list = ['A','B','C']
for index, value in enumerate(my_list):
    print(my_list[index%3] + my_list[(index+1)%3] + my_list[(index+2)%3])
    print(my_list[index%3] + my_list[(index-1)%3] + my_list[(index-2)%3])



#%%
# =================================================================
# Class_Ex3: 
# Write a python program to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
# ----------------------------------------------------------------
my_list_4 = ['A', 'B', 'C', 'D']
for index, value in enumerate(my_list_4):
    




#%%
# =================================================================
# Class_Ex4: 
# Suppose we wish to draw a triangular tree, and its height is provided 
# by the user, like this, for a height of 5:
#      *
#     ***
#    *****
#   *******
#  *********
# ----------------------------------------------------------------

#%%
userin = int(input("How tall do you want your pyramid?"))
for i <= f'{userin}':
    print('1+i*\*'\n)
    i+=1


#%%
# =================================================================
# Class_Ex5: 
# Write python program to print prime numbers up to a specified values.
# ----------------------------------------------------------------
userin = int(input("How high should we check?"))
def primes_below(top):
    i = 1
    if i < top:
        for j in range(2,top):
            list_j = []
            if i % j = 0:
                continue
            elseif len(list_j) == len(range(2,top)):
                print(i)
    i += 1

primes_below(3)


# =================================================================