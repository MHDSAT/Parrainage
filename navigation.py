import os

def get_bleu(line):
    return line[line.find(' ')+1:line.find('- ***')]

def get_ance(line):
    return line[line.find('- ***')+8:-1]

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

os.system('clear')
intro()
compt = 0
choix = input('Salut, voulez vous afficher la liste des CPI ou ING ?\n>>> ')  
while True:
    if choix in ["cpi",'ing']:
        break
    else:
        choix=input('>>> ')
if choix=="cpi":
    with open('tirage/CPI.txt','r') as file:
        lines = file.readlines()
else:
    with open('tirage/ING.txt','r') as file:
        lines = file.readlines()
while True:
    if lines[compt]=='\n':
        compt+=1
        continue
    action = input('> ')
    if not action:
        if lines[compt][:5]=='*****':
            print(lines[compt][:-1])
        else:
            os.system('clear')
            intro()
            print('**Id {}** \t\t\t\t**No {}**\nBleu :\t\t\t{}'.format(compt,lines[compt][:lines[compt].find(' ')+1],get_bleu(lines[compt][:-1])))
            key = input()
            print('Ance :\t\t\t{}\n\n'.format(get_ance(lines[compt])))
        compt+=1

    elif action[:7]=="goto id":
        compt = int(action[8:])
    elif action=='previous':
        compt-=4
    else:
        print('commande introuvable')
    if compt==len(lines)-1:
        break

#os.system('clear')
