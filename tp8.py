#!usr/bin/python3

#-*- coding:utf-8 -*-
import subprocess
import csv



def creer_CSV():
	"""
	BUT		Fonction permettant de créer un fichier CSV avec son en-tête
	"""
	f = open("note.csv", "w+")
	fichier_csv = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	fichier_csv.writerow(['prenom', 'nom', 'compilation', 'warning', 'test', 'documentation', 'note_compilation', 'note_finale'])
	
	valeurs_test = [(0, 0), (1, 0), (0, 1), (1, 1), (12, 12), (12, -43), (-1, -52)]
	fichiers_c = lecture_dossier("eleves_bis")
	selection_fichier(fichiers_c, valeurs_test, fichier_csv)

	f.close()



def lecture_dossier(nom_dossier):
	"""
	BUT		Fonction permettant de lire et récupérer la liste des fichiers contenus dans nom_dossier grace à ls
	PARAM	nom_dossier : Le dossier dont on veut récupérer le contenu
	RETOUR	La liste des fichiers
	"""
	p = subprocess.run(["ls", nom_dossier], stdout=subprocess.PIPE)
	return p.stdout.decode("utf-8").split("\n")



def selection_fichier(fichiers_c, valeurs_test, csv):
	"""
	BUT		Fonction permettant de sélectionner le fichier à vérifier
	PARAM	fichiers_c : La liste des fichiers .c à vérifier
			valeurs_test : Les valeurs à utilisées pour vérifier le fichier
	"""
	for fichier in fichiers_c:
		succes = 0
		if fichier == "":
			return

		prenom, nom = fichier.replace(".c", "").split("_")
		compilation, warning = compiler(fichier)
		documentation = compter_documentation(fichier)

		for couple in valeurs_test:
			succes += execution_tests(couple[0], couple[1])

		note_compilation, note_finale = calculer_note(compilation, warning, succes, documentation)

		ecriture_CSV(csv, prenom, nom, compilation, warning, succes, documentation, note_compilation, note_finale)




def compiler(nom_fichier):
	"""
	BUT		Fonction permettant de compiler nom_fichier, et de compter le nombre de warning
	PARAM	nom_fichier : Le fichier .c à compiler
	RETOUR	compilation : 1 si la compilation échoue, 0 sinon
			warning : Le nombre de warning apparaissant lors de la compilation
	"""
	warning = 0

	sortie = subprocess.run(["gcc", "eleves_bis/{0}".format(nom_fichier), '-Wall', '-ansi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# On compte le nombre de warning
	for chaine in sortie.stderr.decode("utf-8").split(" "):
		if "warning:" == chaine:
			warning += 1

	# On récupère le code de retour, qui correspond au succès de la compilation
	if sortie.returncode == 0:
		compilation = 1;
	else:
		compilation = 0;

	return compilation, warning




def compter_documentation(nom_fichier):
	"""
	BUT		Fonction permettant de compter le nombre de lignes de documentation du fichier nom_fichier, en combinant cat, grep et wc
	PARAM	nom_fichier : Le fichier dans lequel on veut compter le nombre de lignes de documentation
	RETOUR	Le nombre de lignes de documentation
	"""
	# Utiliser des pipes (|) directement dans les commandes mène à des erreurs.
	# La méthode suivante permet d'appeler les commandes sur le résultat de la commande précédente (stdin=p.stdout)

	# cat eleves_bis/<nomdufichier>
	p1 = subprocess.Popen(["cat", "eleves_bis/{0}".format(nom_fichier)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# grep '//*' <- On échappe le caractère /
	p2 = subprocess.Popen(["grep", '//*'], stdin=p1.stdout, stdout=subprocess.PIPE)
	p1.stdout.close()
	# wc -l
	p3 = subprocess.Popen(["wc", '-l'], stdin=p2.stdout, stdout=subprocess.PIPE)
	p2.stdout.close()
	# Au final, on aura comme commande Shell : cat eleves_bis/<nomdufichier> | grep '//*' | wc -l
	documentation = p3.communicate()[0]

	# On obtient le nombre de ligne de documentation
	return int(documentation.decode("utf-8"))



def execution_tests(entier1, entier2):
	"""
	BUT		Fonction permettant d'exécuter le fichier obtenu par la compilation de nom_fichier,
			avec les valeurs test entier1 et entier2
	PARAM	entier1 : L'un des entiers à additionner
			entier2 : L'un des entiers à additionner
	RETOUR	succes : Le nombre de tests réussis
	"""
	succes = 0
	res = entier1 + entier2
	# On vérifie si le message affiché par le programme est correct
	if subprocess.run(["./a.out", str(entier1), str(entier2)], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf-8") != "La somme de {0} et {1} vaut {2}\n".format(str(entier1), str(entier2), str(res)):
		pass
	else:
		succes += 1
	return succes



def calculer_note(compilation, nb_warning, nb_tests, nb_documentation):
	"""
	BUT		Fonction permettant de calculer la note de l'élève
	PARAM	compilation : La valeur de compilation, récupérée avec la fonction compiler
			nb_warning : Le nombre de warning, récupéré avec la fonction compiler
			nb_tests : Le nombre de tests réussis, récupéré avec la fonction execution_tests
			nb_documentation : Le nombre de lignes de documentation, récupéré avec la fonction compter_documentation
	RETOUR	note_compilation : La note de compilation
			str(note_finale) : La note finale en chaine de caractères, pour qu'elle soit lisible par le fichier CSV
	"""
	# Calcul de la note de compilation
	if compilation == 1:	# Si ça compile
		note_compilation = 3
		for i in range(nb_warning):
			if note_compilation == 0:	# Si la note est à 0, on évite de la rendre négative
				break
			note_compilation -= 0.5
	else:	# Si ça ne compile pas
		note_compilation = 0


	# Calcul de la note de tests
	note_tests = nb_tests * (5/7)


	# Calcul de la note de qualité (documentation)
	if nb_documentation >= 3:
		note_documentation = 2
	else:
		note_documentation = nb_documentation * (2/3)


	note_finale = note_compilation + note_tests + note_documentation
	return note_compilation, str(note_finale)



def ecriture_CSV(fichier_csv, prenom, nom, compilation, warning, test, documentation, note_compilation, note_finale):
	"""
	BUT		Fonction permettant d'écrire les données dans le fichier CSV fichier_csv
	PARAM	fichier_csv : Le fichier CSV dans lequel on écrit
			prenom : Le prénom de l'élève
			nom : Le nom de l'élève
			compilation : 1, si le code compile, 0 sinon
			warning : Le nombre de warning lors de la compilation
			test : Le nombre de tests fonctionnels
			documentation : Le nombre de ligne de documentation
			note_compilation : La note de compilation
			note_finale : La note finale de l'élève
	"""
	fichier_csv.writerow([prenom, nom, compilation, warning, test, documentation, note_compilation, note_finale])






if __name__ == "__main__":
	creer_CSV()
