import os
os.chdir("E:/piton/Use_a_cabeca_python/use_a_cabeca_python/06_cap")

#Vai substituir "-" e ":" por "."
def sanitize (time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + "." + secs)

class AthleteList(list):
    def __init__(self,a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(",")
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print("File error" + str(ioerr))
        return(None)

vera= AthleteList("Vera Vi")
vera.append("1.31")
vera.extend(["2.22","1-21","2:22"])

james = get_coach_data("james2.txt")
julie = get_coach_data("julie2.txt") 
mikey = get_coach_data("mikey2.txt") 
sarah = get_coach_data("sarah2.txt") 

print(vera.name + "'s fastest times are:" + str(vera.top3()))
print(james.name + "'s fastest times are:" + str(james.top3()))
print(julie.name + "'s fastest times are:" + str(julie.top3()))
print(mikey.name + "'s fastest times are:" + str(mikey.top3()))
print(sarah.name + "'s fastest times are:" + str(sarah.top3()))
