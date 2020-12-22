import dill
import math

power = lambda x: 2**x

a = map(lambda x: 2**x, range(10))

dill.dump(power, open('dill_test', 'wb'))
dill.dump_session('session.pkl')
        
