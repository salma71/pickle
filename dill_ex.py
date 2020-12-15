import dill
import math
square = lambda x:pow(x, 2)

a = square(3)
b = math.sqrt(9)

dill.dump_session('dill_test.pkl')
