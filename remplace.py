import os

def intro():
    print('*'*80+'\n\t\t\tProgramme Parrainage 3.0\n\n\t\tInstitut Polytechnique de Saint-Louis\n')
    logo = """
                         _        _             __
                        (_) __ _ (_) ___ _   _ / _|
                        | |/ _` || |/ _ \ | | | |_ 
                        | | (_| || |  __/ |_| |  _|
                       _/ |\__,_|/ |\___|\__,_|_|  
                      |__/     |__/               
    """
    print(logo,"\n\n")

def get_num(line):
    pos = line.find(' ')
    return line[:pos+1]

def get_bleu(line):
    return line[line.find(' ')+1:line.find('- ***')]

os.system('clear')
intro()
print('Parît qu\'il y\'a eu un probleme.')
nom,ind = input('Nom svp ? '),0
domaine = int(input('1: CPI\t2: ING EM\t3: ING GC\t4: ING INFO '))
os.system('clear')
intro()
if domaine==1:
    with open('tirage/CPI.txt','r') as file:
        tab = file.readlines()
elif domaine in [2,3,4]:
    with open('tirage/ING.txt','r') as file:
        tab = file.readlines()
for i,line in enumerate(tab):
    if nom.lower() in line.lower():
        os.system('clear')
        intro()
        print('Voulez vous parler de cette lingne ?\n\n{}'.format(line[:-1]))
        while True:
            rep = input('oui / non ? ')
            if rep=='oui' or rep=='non':
                break
        if rep=='oui':
            ind = i
            capture = line[:-1]
            break
else:
    print('Parît que le nom n\'est pas de dans')
if ind != 0:
    if domaine==1:
        with open('ipsl_cpis/ances.txt','r') as file:
            noms = file.readlines()
    elif domaine==2:
        with open('ipsl_pub/em.txt','r') as file:
            noms = file.readlines()
    elif domaine==3:
        with open('ipsl_pub/gc.txt','r') as file:
            noms = file.readlines()
    elif domaine==4:
        with open('ipsl_pub/inf.txt','r') as file:
            noms = file.readlines()
    for nom in noms:
        ret = False
        for line in tab:
            if nom.lower() in line.lower():
                ret=True
                break
        if not ret:
            os.system('clear')
            intro()
            print('\nSuggestion : {} '.format(nom[:-1]))
            while True:
                reponse = input('oui / non ? ')
                if reponse=='oui' or reponse=='non':
                    break
            if reponse=='oui':
                rect = tab[ind][:tab[ind].find('- *** -')+8]
                rect += nom
                print('*'*60,'\nLa ligne',rect[:rect.find(' ')],'a été modifiée avec succés :')
                print('avant = {}\napres = {}'.format(tab[ind][:-1],rect))
                tab[ind]=rect
                if domaine==1:
                    with open('tirage/CPI.txt','w') as file:
                        for _ in tab:
                            file.write(_)
                elif domaine in [2,3,4]:
                    with open('tirage/ING.txt','w') as file:
                        for _ in tab:
                            file.write(_)
                break
    else:
        print('*'*60)
        print('Aucun nom à proposer, Parît qu\'il n\'ya plus d\'ances libres')
        choice = input('1 pour doubler 2 pour choisir manuellement ')
        if choice=="2":
            nom = input('Donnez un nom manuellement ')
            rect = tab[ind][:tab[ind].find('- *** -')+8]
            rect += nom
            print('*'*60,'\nLa ligne',rect[:rect.find(' ')],'a été modifiée avec succés :')
            print('avant = {}\napres = {}'.format(tab[ind][:-1],rect))
            tab[ind]=rect+'\n'
            if domaine==1:
                with open('tirage/CPI.txt','w') as file:
                    for _ in tab:
                        file.write(_)
            elif domaine in [2,3,4]:
                with open('tirage/ING.txt','w') as file:
                    for _ in tab:
                        file.write(_)
        elif choice=="1":
            with open('tirage/CPI.txt','r') as file:
                tab = file.readlines()
            for i,line in enumerate(tab):
                if (not ',' in line) and i!=0 and line != '\n':
                    ind = i
                    break
            rect = tab[ind][:-1]
            rect = get_num(rect)+get_bleu(capture)+' , '+rect[rect.find(' '):]
            tab[ind]= rect+'\n'
            for i,line in enumerate(tab):
                if capture in line:
                    print('DEL : {}'.format(line))
                    tab.pop(i)
            with open('tirage/CPI.txt','w') as file:
                for line in tab:
                    file.write(line)
            print('Nouvelle ligne :\n',rect)
        else:
            print('Choix non valide !')