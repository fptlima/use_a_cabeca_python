import pickle
from athletelist import AthleteList
import os

os.chdir("E:/piton/Use_a_cabeca_python/use_a_cabeca_python/07_cap")

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(",")
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print("File error" + str(ioerr))
        return(None)
    
def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath

    try:
        with open("athletes.pickle", "wb") as athf:
          pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print("File Error (put to store):" + str(ioerr))
    return(all_athletes)
    
def get_from_store():
    all_athletes = {}
    try:
        with open("athletes.pickle", "rb") as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print("File error (get_from_store):" + str(ioerr))
    return(all_athletes)
