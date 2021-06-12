#mes imports
import os
import random

#petite affiche
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
    print(logo)

#Fonction pour supprimer des ances jusqu'à égalité, s'il ya plus d'ances que de bleus
def reguler(bleus,ances):
	ecart = len(ances)-len(bleus)
	if ecart>0:
		for i in range(ecart):
			ances.pop(i)
	return ances

#Fonction pour doubler des bleus jusqu'à égalité, s'il ya plus de bleus que d'ances
def doubler(bleus,ances):
	ecart = len(bleus)-len(ances)
	if ecart>0:
		for i in range(ecart):
			bleus[i] = bleus[i][:-1]+' , '+bleus[-1]
			bleus.pop(-1)
	random.shuffle(bleus)
	return bleus

#ouverture des fichiers cpi (bleus et ances) en mode lecture et recupreation du contenu
with open('ipsl_cpis/bleus.txt','r',encoding='latin-1') as rf:
	bleus_cpi=rf.readlines()
with open('ipsl_cpis/ances.txt','r',encoding='latin-1') as rf:
	ances_cpi=rf.readlines()

#mélanger aléatoirement les listes
random.shuffle(bleus_cpi)
random.shuffle(ances_cpi)

#s'il y'a plus d'ances, supprimer quelques, s'il y'a plus de bleus, en doubler quelques
ances_cpi = reguler(bleus_cpi,ances_cpi)
bleus_cpi = doubler(bleus_cpi,ances_cpi)

#ecriture sur un fichier tirage CPI
with open('tirage/CPI.txt','w') as fw:
	for i in range(len(bleus_cpi)):
		fw.write('{} {} - *** - {}\n'.format(i+1,bleus_cpi[i][:-1],ances_cpi[i]))

#lecture des noms des etudiant dans le privé
with open('ipsl_pv/em.txt','r',encoding='latin-1') as rf:
	bleus_em=rf.readlines()
with open('ipsl_pv/gc.txt','r',encoding='latin-1') as rf:
	bleus_gc=rf.readlines()
with open('ipsl_pv/inf.txt','r',encoding='latin-1') as rf:
	bleus_inf=rf.readlines()

#lecture des noms des etudiant dans le public
with open('ipsl_pub/em.txt','r',encoding='latin-1') as rf:
		ances_em=rf.readlines()
with open('ipsl_pub/gc.txt','r',encoding='latin-1') as rf:
		ances_gc=rf.readlines()
with open('ipsl_pub/inf.txt','r',encoding='latin-1') as rf:
		ances_inf=rf.readlines()

#mélanger les nouvelles listes
random.shuffle(ances_inf)
random.shuffle(bleus_inf)
random.shuffle(ances_em)
random.shuffle(bleus_em)
random.shuffle(ances_gc)
random.shuffle(bleus_gc)

#s'il y'a plus d'ances, supprimer quelques, s'il y'a plus de bleus, en doubler quelques
ances_em=reguler(bleus_em,ances_em)
bleus_em=doubler(bleus_em,ances_em)
ances_gc=reguler(bleus_gc,ances_gc)
bleus_gc=doubler(bleus_gc,ances_gc)
ances_inf=reguler(bleus_inf,ances_inf)
bleus_inf=doubler(bleus_inf,ances_inf)

#ecriture sur le fichier tirage pour ances
with open('tirage/ING.txt','w',encoding='utf-8') as fw:
	fw.write('{} {} {}\n\n'.format('*'*20,'Bleu - *** - Parrain Info','*'*20))
	for i in range(len(bleus_inf)):
		fw.write('{} {} - *** - {}\n'.format(i+1,bleus_inf[i][:-1],ances_inf[i]))

	fw.write('{} {} {}\n\n'.format('*'*20,'Bleu - *** - Parrain Electro-Meca','*'*20))
	for i in range(len(bleus_em)):
		fw.write('{} {} - *** - {}\n'.format(i+1,bleus_em[i][:-1],ances_em[i]))

	fw.write('{} {} {}\n\n'.format('*'*20,'Bleu - *** - Parrain Genie Civil','*'*20))
	for i in range(len(bleus_gc)):
		fw.write('{} {} - *** - {}\n'.format(i+1,bleus_gc[i][:-1],ances_gc[i]))
os.system('clear')
intro()
print('Tirage effectué avec succés !\n')
