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
    #out = open("data.out","w")
    man_data = open("man_data.txt", "w")
    other_data = open("other_data.txt", "w")

    print(man,file=man_data)
    print(other,file=other_data)
except IOError:
    print("File Error.")

finally:
    man_data.close()
    other_data.close()
