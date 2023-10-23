movies = ["The Holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
    ["Graham Chapman",
    ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

for each_item in movies:                        #para cada item na lista movies
    if isinstance(each_item, list):             #se o item dentro da lista movies for uma lista faça:

        for nested_item in each_item:           #para cada item dentro da lista dentro da lista movies:
            if isinstance(nested_item, list):   #se o item dentro da lista dentro da lista movies for uma lista faça:

                for deeper_item in nested_item: #para cada item dentro da lista dentro da lista que esta dentro da lista movies:
                        print(deeper_item)      #imprimir o item dentro da lista, que ta dentro da lista que esta dentro da lista movies

            else:                               #se o item dentro da lista que esta dentro de movies não for lista então:
                print(nested_item)              #imprima o item dentro da lista que esta dentro de movies

    else:                                       #se o item dentro da lista movies não for uma lista então:
        print(each_item)                        #imprime os itens de movies
