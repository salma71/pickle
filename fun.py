## slower than pickle, not included in the standard library
## database connection isnot serialable even for dill, it is a tough job
import dill
dill.load_session('dill_test.pkl')
print(globals().items())
print(a)