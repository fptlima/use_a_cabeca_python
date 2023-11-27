from nester import print_lol
import os
os.chdir('E:/piton/Use_a_cabeca_python/use_a_cabeca_python/04_cap')
try:
    data = open("sketch.txt")
    man = []
    other = []
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except:
    print('The data is missing!')

try:
    with open("man_data.txt", "w") as man_file, open("other_data.txt","w") as other_file:
        print_lol(man, fh = man_file)
        print_lol(other, fh = other_file)
except IOError as err:
    print("File error: " + str(err))