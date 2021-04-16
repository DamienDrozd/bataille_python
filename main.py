import random

maps = ["Bar", "Deauville", "Marseille", "Barbes", "Rio", "Chicago", "auchan"]#liste des maps (annulé)
characters = [["François Hollande", "poids", "nez", "cheveux"],#liste des personnages
              ["Obélix", "poids", "nez", "intelligence"],
              ["Cyrano de Bergerac", "nez"],
              ["Koba lad", "intelligence", "cheveux", "drogue", "alcool"],
              ["Jordan Belfort", "drogue", "alcool"],
              ["Remi sans famille", "famille", "animaux", "cheveux"],
              ["Mister Bean", "intelligence", "cheveux", "nez"]]





class player: #objet qui définissent les joueurs
    def __init__(self):
        self.sujet = 0
        self.faiblesse_sujet = 0
        self.verbe = 0
        self.faiblesse_verbe = 0
        self.complement = 0
        self.faiblesse_complement = 0
        self.liaisons = 0
        self.faiblesse_liaisons = 0
        self.tab = []
        self.phrase = []
        self.typemot = []
        self.character = ""
        self.weakness = []
        self.name = "joueur ?"
        self.used_weakness = []
        self.score = 0





    
#------------------------------------Choix de la map(projet annulé)-----------------------------------------------------
def MAP_Choice():
    print("Choisissez votre map dans cette liste:")
    x = 1
    for i in maps:
        print(x, ": ", i)
        x+=1

    selected_map = input()

    while selected_map.isdecimal() == False :
        print ("Entrez un nombre")
        selected_map = input()

    while  int(selected_map) < 0 or int(selected_map) > len(maps):
        print("Entrez un nombre valide")
        selected_map = input()
#-------------------------------------Choix des joueurs------------------------------------------------------------------
def pchoice(J):
    print(J.name, " : \nChoisissez votre personnage dans cette liste:")
    x = 1
    for i in characters:
        print(x, ": ", i[0])
        x += 1

    player = input()

    while player.isdecimal() == False or int(player) < 0 or int(player) > len(characters):#La valeur entrée doit être valide pour continuer
        print("Entrez un nombre valide")
        player = input()

    
    player = characters[int(player)-1]
    J.character = player[0]
    
    J.weakness = player[1:]
#----------------------------------------Sélection aléatoire des mots--------------------------------------------------------
def randmot(path, nbmots):

    f = open(path, "r")
    line = f.readlines()
    f.close

    rand = [""]
    listemot = []
    for i in range(0, nbmots, 1):
        n = random.randint(0, len(line)-1)

        j = 0
        while j < (len(rand)):
            if rand[j] == n:
                j = 0
                n = random.randint(0, len(line)-1)
            j += 1

        rand.append(n)
        listemot.append(line[n])

    x = 0
    faiblesse = []
    for i in range(len(listemot)):
        for j in range(len(listemot[i])):
            if listemot[i][j] == "(":
                faiblesse.append(listemot[i][j+1:])
                listemot[i] = listemot[i][0:j]
                break

            if j == len(listemot[i])-1:
                listemot[i] = listemot[i][0:j]
                faiblesse.append("")

    for i in range(len(faiblesse)):
        for j in range(len(faiblesse[i])):
            if faiblesse[i][j] == ")":
                faiblesse[i] = faiblesse[i][0:j]
                break

    return listemot, faiblesse
#----------------------------------------Lancement du jeu--------------------------------------------------------------------
def play(J) : 
    print("C'est au tour du", J.name," de jouer:\n Voici la liste de mots du ", J.name,":")
    x = 1
    print("\nliste des sujets:")
    for i in J.sujet:
        print(i)
    print("\nliste des verbes:")
    for i in J.verbe:
        print(i)
    print("\nliste des complements:")
    for i in J.complement:
        print(i)
    print("\nliste des liaisons:")
    for i in J.liaisons:
        print(i)
    
    
    type_mot=["sujet","verbe","complement","liaisons"]
    print("\nvoulez vous ajouter:\n1) un sujet\n2) un verbe\n3) un complement\n4) une liaison \n5) passer votre tour")
    choix_type_mot = input()
    # La valeur entrée doit être valide pour continuer
    while choix_type_mot.isdecimal() == False or int(choix_type_mot) < 0 or int(choix_type_mot) > 5 :
        print("Entrez un nombre valide")
        choix_type_mot = input()
        
    
    nbmot = 0
    while int(choix_type_mot) < 5:
        print("Choisissez le",type_mot[int(choix_type_mot)-1],"de votre insulte:")
        
        x=0
        for i in range(len(J.tab[int(choix_type_mot)-1])):
            x+=1
            print(str(x), ")", J.tab[int(choix_type_mot)-1][i],"\nfaiblesse:", J.faiblesse_tab[int(choix_type_mot)-1][i])
            
        wordchoose = input()
        
        # La valeur entrée doit être valide pour continuer
        while wordchoose.isdecimal() == False or int(wordchoose) < 0 or int(wordchoose) > len(J.tab[int(choix_type_mot)-1]) :
            print("Entrez un nombre valide")
            wordchoose = input()
        J.phrase.append(J.tab[int(choix_type_mot)-1][int(wordchoose)-1])
        J.typemot.append(type_mot[int(choix_type_mot)-1])
        J.used_weakness.append(J.faiblesse_tab[int(choix_type_mot)-1][int(wordchoose)-1])
        
        nbmot+=1
        print("Voici votre phrase actuelle")
        for i in J.phrase: 
            print(i, end = " ")
        print("\n")
        print("voulez vous ajouter:\n1) un sujet\n2) un verbe\n3) un complement\n4) une liaison \n5) passer votre tour")
        choix_type_mot = input()
        while choix_type_mot.isdecimal() == False or int(choix_type_mot) < 0 or int(choix_type_mot) > 5 :
            print("Entrez un nombre valide")
            choix_type_mot = input()
#-----------------------------------------Vérification de la phrase des joueurs--------------------------------------------------
def verifphrase(J):
    if J.phrase != []:
        for i in range(len(J.phrase)):
            for j in range(i, len(J.phrase)):
                if J.phrase[i] == J.phrase[j]:
                    print("Le joueur", J.name, "a utilisé deux fois le même mot")
                    return 0
    else:
        return 0
    
    if len(J.phrase)>2:
        if J.typemot[0] != "sujet":
            return 0
        if J.typemot[1] != "verbe":
            return 0
        if J.typemot[2] != "complement":
            return 0
    else :
        return 0 
    
    for i in range(len(J.typemot)):
        if i > 2:
            if i % 2 == 0:
                if J.typemot[i] != "complement":
                    return 0
            else:
                if J.typemot[i] != "liaisons":
                    return 0

    if J.typemot[len(J.typemot)-1] != "complement":
        return 0
   
    
    return 1
#------------------------------------------Comptage du score-----------------------------------------------------
def countscore(J1, J2):
    print("La phrase du", J1.name, "est:")
    for i in J1.phrase:
        print(i, end=" ")
    print("\n")
    if verifphrase(J1) == 1:
        print("Le", J1.name, "a une phrase correcte,il obtient 5 points")
        J1.score += 5
        if len(J1.phrase) > 4:
            J1.score += len(J1.phrase)-4
            print("Le", J1.name,
                  "a gagné un bonus de longueur de phrase de ", len(J1.phrase)-4)
    else:
        print("la phrase du", J1.name,
              "est gramaticalement incorrecte, il ne gagne pas de bonus de phrase correcte ni de bonus de longueur")

    for i in J1.used_weakness:
        for j in J2.weakness:
            if i == j:
                J1.score += 1
                print("Le", J1.name, "a utilisé un mot de type", i,"c'est une faiblesse du", J2.name, "\n il gagne un point supplémentaire")
    print("Le score final du", J1.name, "est:", J1.score)




#   Création du joueur 1
J1 = player()
J1.name = "joueur 1"
J1.sujet, J1.faiblesse_sujet = randmot(r"Maps\Bar\sujet.txt", 6)
J1.verbe, J1.faiblesse_verbe = randmot(r"Maps\Bar\verbe.txt", 6)
J1.complement, J1.faiblesse_complement = randmot(r"Maps\Bar\complement.txt", 6)
J1.liaisons, J1.faiblesse_liaisons = randmot(r"Maps\Bar\liaison.txt", 6)
J1.tab = [J1.sujet, J1.verbe, J1.complement, J1.liaisons]
J1.faiblesse_tab = [J1.faiblesse_sujet, J1.faiblesse_verbe, J1.faiblesse_complement, J1.faiblesse_liaisons]


#Création du joueur 2
J2 = player()
J2.name = "joueur 2"
J2.sujet, J2.faiblesse_sujet = randmot(r"Maps\Bar\sujet.txt", 6)
J2.verbe, J2.faiblesse_verbe = randmot(r"Maps\Bar\verbe.txt", 6)
J2.complement, J2.faiblesse_complement = randmot(r"Maps\Bar\complement.txt", 6)
J2.liaisons, J2.faiblesse_liaisons = randmot(r"Maps\Bar\liaison.txt", 6)
J2.tab = [J2.sujet, J2.verbe, J2.complement, J2.liaisons]
J2.faiblesse_tab = [J2.faiblesse_sujet, J2.faiblesse_verbe, J2.faiblesse_complement, J2.faiblesse_liaisons]




pchoice(J1)
pchoice(J2)
play(J1)
play(J2)
countscore(J1, J2)
countscore(J2, J1)

if J1.score>J2.score:
    print("Le joueur 1 a gagné bravo a lui")
if J1.score < J2.score:
    print("Le joueur 2 a gagné bravo a lui")
if J1.score == J2.score:
    print("Il y a égalité, cette partie n'a pas réussi a vous départager")

if J1.score < J2.score:
    print("Le joueur 2 a gagné bravo a lui")
if J1.score < J2.score:
    print("Le joueur 2 a gagné bravo a lui")
if J1.score < J2.score:
    print("Le joueur 2 a gagné bravo a lui")
