import pickle
import cleaning
from custom_unpickling import Process

test = open('test_unpickle.pkl', 'rb')
methods = pickle.load(test)
test.close()

print(methods.__dict__)
print(methods.encode_col('ZZ'))

test.close()
if __name__=='__main__':
    print('inside test_unpickle')
        
        
















# pickle_in = open('example.pkl', 'rb')

# example = pickle.load(pickle_in)
# print(type(example))

# if __name__ == "__main__":
#     pass
