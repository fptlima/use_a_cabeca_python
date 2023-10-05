count = 0
movies = ["The Holy grail", "The Life of Brian", "The Meaning of Life"]
print("Usando While:")
while count < len(movies):
    print(movies[count])
    count = count + 1

print("\nUsando o For")
for each_item in movies:
    print(each_item)
