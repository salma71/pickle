import pickle

class Example:
    
    def __init__(self, num=35, strg='hello', lis=[1,2,3], dic={1:'f', 2:'two'}, tup=(33,56)):
        self.num = num
        self.strg = strg
        self.lis = lis
        self.dic = dic
        self.tup = tup
        
        

# my_object = Example()

# pickle_out = open('example.pkl', 'wb')

# pickle.dump(my_object, pickle_out)

# pickle_out.close()


pickle_in = open('example.pkl', 'rb')

example = pickle.load(pickle_in)
print(type(example))
