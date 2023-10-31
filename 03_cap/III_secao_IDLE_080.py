import os
os.getcwd()
#Saida::> E:\piton\Use_a_cabeca_python\use_a_cabeca_python>
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/03_cap')
os.getcwd()
#Saida::> E:\piton\Use_a_cabeca_python\use_a_cabeca_python\03_cap>
data = open("sketch.txt")
print(data.readline(), end='')
#Saida::> Man: Is this the right room for an argument?
print(data.readline(), end='')
#Saida::> Other Man: I've told you once.

for each_line in data:
    (role, line_spoken) = each_line.split(':')
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken,end="")

data.close()