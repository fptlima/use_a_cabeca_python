import os
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/05_cap')
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
clear_james = []
clear_julie = []
clear_mikey = []
clear_sarah = []
for x in james:
    clear_james.append(sanitize(x))
for x in julie:
    clear_julie.append(sanitize(x))
for x in mikey:
    clear_mikey.append(sanitize(x))
for x in sarah:
    clear_sarah.append(sanitize(x))

print(sorted(clear_james))
print(sorted(clear_julie))
print(sorted(clear_mikey))
print(sorted(clear_sarah))
