import pickle
import functools
import math

class Process:
    
    def __init__(self, *args):
        self.args = args
        self.fun = lambda x: x+2
    
    @classmethod    
    def encode_col(self, col):
        """[encode columns names from letters to and ID on base 26 ]
        "D" -> returns 4
        "AA" -> 27
        "ZZ" -> 702

        Args:
            col ([string]): [columns name is alphabetic upper case base 26]
        """    
        return (functools.reduce(
            lambda res, c: res * 26 + ord(c) - ord('A') + 1, col, 0
        ))

    def __getstate__(self):

        # this method is called when you are
        # going to pickle the class, to know what to pickle
        state = self.__dict__.copy()
        
        # don't pickle the parameter fun.
        del state['fun']
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)

       
def main():
    a = Process()
    print(a.__dict__)
    with open('test_pickle.pkl', 'wb') as f:
        pickle.dump(a, f, -1)
        f.close()

if __name__=='__main__':
    main()











# pickle_in = open('example.pkl', 'rb')

# example = pickle.load(pickle_in)
# print(type(example))
