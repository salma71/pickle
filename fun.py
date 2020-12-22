## slower than pickle, not included in the standard library
## database connection isnot serialable even for dill, it is a tough job

import dill_ex
import dill

test = open('dill', 'rb')
res = dill.load(test)

print(res)

test.close()

if __name__ == '__main__':
    print('Testing dill')


# import dill
# dill.load_session('dill_test.pkl')
# print(globals().items())
# print(a)
