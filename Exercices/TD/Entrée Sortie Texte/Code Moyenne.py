ficR = open("notes.txt", "r")
ficW = open("moyenne.txt", "w")

for ligne in ficR:
    list = (ligne.split())
    moyenne = 0
    for i in range(1, len(list)):
        moyenne += int(list[i])
    moyenne = moyenne // (len(list) - 1)
    ficW.write(ligne.strip())
    ficW.write(" ")
    ficW.write(str(moyenne))
    ficW.write("\n")
ficW.close()