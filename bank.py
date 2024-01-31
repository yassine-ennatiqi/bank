import random
import json
from termspark.termspark import TermSpark

compte={}
client={}
clientcompte={}

def result(message, color="white", background="black"):
    termspark = TermSpark()
    termspark.spark_left([ f" {message} ", color, background])
    termspark.spark()

def error(message):
    result(message, background='red')

def success(message):
    result(message, background='green')

def choix(message):
    termspark = TermSpark()
    termspark.spark_left([ f" {message} ",'blue' ])
    termspark.spark()

def welcome():
    termspark = TermSpark()
    termspark.spark_center([ "                      ", 'black', 'magenta'])
    termspark.spark()
    termspark = TermSpark()
    termspark.spark_center([ " MRHBA BIKOM F LBANKA ", 'black', 'magenta'])
    termspark.spark()
    termspark = TermSpark()
    termspark.spark_center([ "                      ", 'black', 'magenta'])
    termspark.spark()

def ajouter(numCl,MPC,SoldeC,numC):
    for i in l :
        if numCl == i['n de client']:
            error("ce compte deja existe changer le numero de client")
            return False
    termspark = TermSpark()
    termspark.spark_left([ f"le némuro de votre compte est {numC}", 'black', 'magenta'])
    termspark.spark()
    dic = { "n de client" :numCl ,
            "n de compte" : numC , 
            "sold" : SoldeC ,
            "mot de passe" : MPC
            }
    f = open("file.json" , "w")    
    l.append(dic)
    f.write(json.dumps(l))
    f.close()
def suprimmer(numCl):
    for i in l :
        if numCl == i['n de client']:
            l.remove(i)
            numC = i['n de compte']
            f = open("file.json" , "w")    
            f.write(json.dumps(l))
            return numC
    return False

def neveuxMOT(numCl)  :
    for i in l :
        if numCl == i['n de client']:
            NMPC=input("entrer le neveux mot de passe: ")
            i['mot de passe'] = NMPC
            f = open("file.json" , "w")    
            f.write(json.dumps(l))
            return True
    return False
        

def affichageSOLDE(numC):
    for i in l :
        if numC == i['n de compte']:
            return i['sold']
    return False
        
def déposer(numC,soldeDéposer):
    for i in l :
        if numC == i['n de compte'] and soldeDéposer > 0 :
        
            i['sold'] = i['sold'] + soldeDéposer
            f = open("file.json" , "w")    
            f.write(json.dumps(l))
            success("L'opération s'est terminée avec succès ")
            success(f"votre solde est {i['sold']} ")
        elif numC != i['n de compte']:
            error("Le compte n'existe pas.")
        elif soldeDéposer <= 0:
            error("solde déposer incorrect")

def retirer(numC,soldeRetirer):
    for i in l :
        if numC == i['n de compte']and soldeRetirer <= i['sold'] and soldeRetirer > 0 :
            i['sold'] = i['sold'] - soldeRetirer
            f = open("file.json" , "w")    
            f.write(json.dumps(l))
            success("L'opération s'est terminée avec succès ")
            success(f"votre solde est {i['sold']} ")
        elif numC != i['n de compte']:
            error("Le compte n'existe pas.")
        elif soldeRetirer > i['sold'] or soldeRetirer <= 0:
            error("solde retirer incorrect")

genererNumCompte = lambda numCl: int(str(numCl) + str(random.randint(0, 100)))

welcome()
while True : 
    f = open("file.json" , "r")
    l = json.loads(f.read() or "[]")  
    choix("1.menu agent")
    choix("2.menu client")
    choix("3.Quitter")
    choix1=input("Choisissez une option (1, 2 ou 3): ")      
    if choix1 == "1":

        choix("1.ajouter un compte")
        choix("2.suprimer un compte")
        choix("3.Retour au Menu Principal")
        choix2=input("Choisissez une option (1, 2 ou 3): ")
        if choix2=="1":
            numCl=int(input("entrer le numéro de client: "))
            MPC=input("entrer le mot de passe: ")
            numC=genererNumCompte(numCl)
            SoldeC=float(input("entrer le sold: "))
            ajouter(numCl,MPC,SoldeC,numC)
        if choix2=="2":
            numCl=int(input("entrer le numéro de client: "))
            if dffdf := suprimmer(numCl):
                success(f"le compte {dffdf} a été supprimé avec succès.")
            else:
                error("Le compte n'existe pas.")
        if choix2=="3":
            continue
    if choix1=="2":
        choix("1.Modifier son mot de passe")
        choix("2.Afficher son solde")
        choix("3.Déposer une somme d’argent")
        choix("4.Retirer une somme d’argent")
        choix("5.Retour au Menu Principal")
        choix3=input("Choisissez une option (1, 2, 3, 4 ou 5): ")
        if choix3=="1":
            numCl=int(input("entrer le numéro de client: "))
            if neveuxMOT(numCl) :
                success("Le mot de passe a été modifié avec succès.")
            else:
                error("Le compte n'existe pas.")
        if choix3=="2":
            numC=int(input("entrer le numéro de compte: "))
            if affichageSOLDE(numC) :
                success(f"votre solde est {affichageSOLDE(numC)} ")
            else:
                error("Le compte n'existe pas.")
        if choix3=="3":
            numC=int(input("entrer le numéro de compte "))
            soldeDéposer=float(input("entrer le solde déposer: "))
            déposer(numC,soldeDéposer)
        if choix3=="4":
            numC=int(input("entrer le numéro de compte "))
            soldeRetirer=float(input("entrer le solde retirer: "))
            retirer(numC,soldeRetirer)
        if choix3=="5":
            continue
    if choix1=="3":
            exit()        
# a = {12 : 12}
# if 12 in a :
#     print("yyyyyyyyyyyyyyyyes")
# else :
#     print("nnnnnnnnnnnnon")    