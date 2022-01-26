# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

print( "ok" if (somebody) else "not ok" )

#%%
# Let us install our first additional library.
# pip is the package management system for python. 
# If you have an older system with python 2 and python 3 installed, 
# you might need pip3 to install to your python 3 environment. 
!pip install beepy # Do this in interactive python will install in your conda env - the! asks it to go to the shell
# pip install beepy # Do this in the terminal (bash) will install in your system's default python env (system PATH)
# conda install beepy # Some of you might need conda install, depending on your system settings.

# other related commands:
# !sudo pip install beepy
# !pip freeze
# ! pip list  # space after ! is okay here
# ! pip show beepy

# You can also check the versions under Anaconda...

#pip is the Python library/program manager
#!pip freeze would freeze everything so we can see their versions
#!pip show LIBRARY will tell you what version of that particular package you have

import beepy as bp

# %%
try: 
  res = "ok" if (somebody) else "not ok"
  if type(res) == str :
    print(res)
# except NameError:
#   bp.beep("ping")
#   print('NameError with somebody')
#   somebody = "SomeBD"
#   print('Error resolved.\nok')
 
# we can continue to add other types of exceptions we want to handle 
except BaseException as e:
  bp.beep("ping")
  print(f'Unexpected error with somebody: {e}')
#This is an error clause that is skipped to if there's an error
#%%
# Use del to delete an env variable.