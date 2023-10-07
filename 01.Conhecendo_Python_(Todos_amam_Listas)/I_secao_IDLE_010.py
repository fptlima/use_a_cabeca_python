cast = ["Cleese", "Palin", "Jones", "Idle"]
print("Elenco: (cast)", cast)
print("\nTamanho do Elenco: (len(cast))",len(cast))
print("\nPrimeiro do Elenco: (cast[1])",cast[1])
cast.append("Gilliam")
print("\nAdicionando por último no elenco (.append): ",cast)

cast.pop()
print("\nRemovendo o último do elenco (.pop): ",cast)

cast.extend(["Gilliam","Chapman"])
print("\nAdicionando uma lista de dois atores (.extend) :",cast)

cast.remove("Chapman")
print("\nRemover ator do elenco selecionado: (remove('Chapman'))",cast)

cast.insert(0, "Chapman")
print("\nInserir ator selecionado, na posição selecionada (insert(0, 'Chapman'))",cast)