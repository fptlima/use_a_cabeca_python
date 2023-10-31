import os
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/03_cap')
#Saida::> E:\piton\Use_a_cabeca_python\use_a_cabeca_python\03_cap>
data = open("sketch.txt")
#Saida::> Other Man: I've told you once.

for each_line in data:
    (role, line_spoken) = each_line.split(":")
    #print(role, line_spoken)
    help(each_line.split(":"))
data.close()