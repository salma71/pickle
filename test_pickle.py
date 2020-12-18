import pickle
import cleaning
from cleaning import Process

test = open('test_pickle.pkl', 'rb')
methods = pickle.load(test)

print(methods.encode_col('ZZ'))
print(methods.encode_col('AA'))
print(methods.encode_col('D'))

test.close()
if __name__=='__main__':
    print('inside test_pickle')
        
        
















# pickle_in = open('example.pkl', 'rb')

# example = pickle.load(pickle_in)
# print(type(example))

# if __name__ == "__main__":
#     pass
