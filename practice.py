# reads whatever is in the .txt file and saves it to a variable
try:
  with open('./secret.txt') as f:
    TEST_VAR = f.read().strip()
except:
    print('did not load')
    # if no secret.txt look for env variable in os.environ
    # if in Heroku should look at whatever we set for env variables
    import os
    TEST_VAR = os.environ['TEST_VAR']
    print(TEST_VAR)
    pass



# lets check the output of TEST_VAR
# print(TEST_VAR)

#########################################
# from .zshrc
#import os
#TEST_VAR = os.environ['TEST_VAR']

#print(TEST_VAR)
