import pickle
import nester
import os
new_man = []
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/04_cap')
try:
    with open('man_data_dump.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print("IO error: " + str (err))
except pickle.PickleError as perr:
    print("Pickling error: " + str (perr))

nester.print_lol(new_man)
