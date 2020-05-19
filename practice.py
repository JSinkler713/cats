# reads whatever is in the .txt file and saves it to a variable
#with open('./secrets.txt') as f:
#  TEST_VAR = f.read().strip()

# lets check the output of TEST_VAR
#print(TEST_VAR)


# from .zshrc
import os
TEST_VAR = os.environ['TEST_VAR']

print(TEST_VAR)
