import os
#Saida::> E:\piton\Use_a_cabeca_python\use_a_cabeca_python>
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/03_cap')
data = open("sketch.txt")

for each_line in data:
    if not each_line.find(':') == -1:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')

data.close()