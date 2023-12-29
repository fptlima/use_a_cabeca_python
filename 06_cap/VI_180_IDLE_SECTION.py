cleese = {}
palin = dict()
print("Tipo: ",type(cleese))
print("Tipo: ",type(palin),"\n")

cleese['Name'] = 'John Cleese'
cleese["Occupations"] = ["Actor", "comedian","writer","film producer"]
palin = {'Name': "Michael Palin", "Occupations": ["comedian","actor", "writer", "tv"]}
print(palin["Name"])
print(cleese["Occupations"][-1])

palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare, North somerset, England"

print(palin)
print(cleese)
