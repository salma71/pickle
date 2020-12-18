import pickle
import functools

import multiprocessing as mp
from math import sqrt

class Process:
    
    def __init__(self, *args):
        self.args = args
    
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


    
def main():
    process = Process()
    with open('test_pickle.pkl', 'wb') as f:
        pickle.dump(process, f, -1)
        f.close()

if __name__=='__main__':
    main()











# pickle_in = open('example.pkl', 'rb')

# example = pickle.load(pickle_in)
# print(type(example))
