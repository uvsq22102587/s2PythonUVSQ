from multiprocessing.dummy import active_children
import random as rdm


def nb_lignes(nomfichier: str):
    fic = open(nomfichier, "r")
    res = 0
    for lignes in fic:
        res += 1
    return res


def ecrit_mots_n_lettre(fichier: str, n: int):
    ficR = open(fichier, "r")
    ficW = open(fichier + f"{n}_mots", "w")
    res = 0
    for lignes in ficR:
        l = lignes.strip()
        o = tuple(lignes)
        if len(o) == n + 1:
            ficW.write(lignes)
    ficW.close()
    return fichier + f"{n}_mots"


def ecrit_liste_mots(n: int):
    ficR = open("words.txt", "r")
    res = 0
    for lignes in ficR:
        lignes.strip()
        o = tuple(lignes)
        if len(o) == n:
            res += 1
    ficW = open("wordsn.txt", "w")
    ficW.write(str(res))
    ficW.close()


def melange_mots(fichier: str):
    ficR = open(fichier, "r")
    ficW = open(f"{fichier}.mel", "w")
    mots = ficR.readlines()
    rdm.shuffle(mots)
    for elem in mots:
        ficW.write(str(elem))
    ficW.close()
    ficR.close()


def compare_mots(mTest: str, mRef: str):
    if mTest == "" or mRef == "":
        return
    mTest = mTest.strip()
    mTest = list(mTest)
    mRef = list(mRef)
    assert len(mTest) == len(mRef), "Les deux mots ne sont pas de la même taille." 
    res = []
    for i in range(0, len(mTest)):
        if mTest[i] == mRef[i]:
            res.append(1)
            mRef[i] = ""
        elif mTest[i] in mRef:
            loc = mRef.index(mTest[i])
            if mRef[loc] == mTest[loc]:
                res.append(0)
            else:
                mRef[loc] = ""
                res.append(2)
        else:
            res.append(0)
    return res


def ecrit_liste_compatible(fichier: str, m: str, profil: list):
    ficW = open(fichier + ".comp", "w")
    ficR = open(fichier, "r")
    for ligne in ficR:
        ligne = ligne.strip()
        l = compare_mots(m, ligne)
        if l == profil:
            ficW.write(ligne + "\n")


ecrit_liste_compatible("words.txt5_mots.comp", "aloed", [2, 1, 0, 0, 1])
