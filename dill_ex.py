import multiprocessing as mp
from multiprocessing import Pool, Manager
import dill
import math



class Dill:
    
    def __init__(self, *args):
        self.args = args 
#     # declare the number of processors to use
    
    def lmd_functions(self):
        # open a pool of 4 core
        pool = mp.Pool(4)
        # a series of lambda functions or what ever you want
        pool.map(lambda x: pow(2, x), range(10))
        pool.map_async(lambda x: sin(x**x), range(10))

        
def main():
    # Create the Task manager as Global
    tasks = mp.Manager()
    # Pass the Manager to your class Dill
    c = Dill(tasks)
    # open the file as binary
    dil = open('dill_test', 'wb')
    # convert into a dill object
    lam = dill.dumps(dil)
        
if __name__ == "__main__":
    main()
