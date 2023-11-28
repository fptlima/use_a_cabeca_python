import os
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/05_cap')

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

print(james)
print(julie)
print(mikey)
print(sarah)
#nester.print_lol(james)
