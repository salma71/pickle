import pickle

pickle_in = open('example.pkl', 'rb')

example = pickle.load(pickle_in)
print(type(example))