
## using dupms and loads -> to return a string without generating a file

import pickle

class Example:
    
    def __init__(self, num=35, strg='hello', lis=[1,2,3], dic={1:'f', 2:'two'}, tup=(33,56)):
        self.num = num
        self.strg = strg
        self.lis = lis
        self.dic = dic
        self.tup = tup
        

## this method is to return a string not write to a file
my_object = Example() # inistantiate the object
pickle_obj = pickle.dumps(my_object, protocol=3) # pickling the object -> dumps returns a string
# you have to specify the protocol to specify which version to pickle and unpickle
unpickle = pickle.loads(pickle_obj) # load the object

print(f'this is my class object:\n{unpickle.strg}\n') # print the output

## this method is to write to a file