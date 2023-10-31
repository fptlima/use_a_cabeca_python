import os
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/03_cap')
if os.path.exists("sketch.txt"):
    data = open("sketch.txt")

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:
            pass

    data.close()
else:
    print('The data is missing!')