import os
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/05_cap')

#Vai substituir - e : por .
def sanitize (time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ":"
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + "." + secs)

with open('james.txt', 'r') as jaf:
    data = jaf.readline()
james = data.strip().split(",")
with open('julie.txt', 'r') as juf:
    data = juf.readline()
julie = data.strip().split(",")
with open('mikey.txt', 'r') as mif:
    data = mif.readline()
mikey = data.strip().split(",")
with open('sarah.txt', 'r') as saf:
    data = saf.readline()
sarah = data.strip().split(",")    

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
