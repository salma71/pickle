import pickle
import pickling
from pickling import Example

if __name__=='__main__':
    with open('test_pickle.pkl', 'rb') as f:
        users = pickle.load(f)
        print(users.dic)
        
        
        

# pickle_in = open('example.pkl', 'rb')

# example = pickle.load(pickle_in)
# print(type(example))

# if __name__ == "__main__":
#     pass