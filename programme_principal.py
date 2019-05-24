from tkinter import *
from os import chdir
from random import randrange
from tkinter.filedialog import *

def suiv():
    fenetre.destroy()      #en appuyant sur le bouton, on passe à la salle suivante
    return

def gameover():
    global fenetre
    if vie>0:
        fenetre.destroy()
    fenetre=Tk()
    fenetre.title("Game over")
    txt=Label(fenetre,text="Vous avez perdu. \n Votre score est de : "+str(score))  #affiche le score réalisé
    x=str(input("nom ?"))   #demande le nom
    fiche_score=open("score.txt", "a")  #inscrit le score dans le journal des scores
    fiche_score.write(x+" : " + str(score)+ "\n")
    fiche_score.close
    txt.pack()
    suivant=Button(fenetre,text="Scores",command=suiv)
    suivant.pack(pady=5)
    fenetre.mainloop()
    fichier = open("score.txt", "r")
    content = fichier.read()
    fichier.close()
    score_2=Tk()
    score_2.title("score")
    score_1=Label(score_2, text="les anciens score : \n"+content)   #affiche les anciens scores réalisés dans une fenêtre tkinter
    score_1.pack()
    score_2.mainloop()
    return

def victoire():
    global fenetre
    fenetre.destroy()
    fenetre=Tk()
    fenetre.title("Victoire !")
    description=Label(fenetre,text="Vous êtes enfin sorti du donjon. \n Votre score est de : "+str(score))
    description.pack()
    x=str(input("nom ?"))
    fiche_score=open("score.txt", "a")
    fiche_score.write(x+" : " + str(score)+ "\n")
    fiche_score.close
    suivant=Button(fenetre,text="Scores",command=suiv)
    suivant.pack(pady=5)
    fenetre.mainloop()
    fichier = open("score.txt", "r")
    content = fichier.read()
    fichier.close()
    score_2=Tk()
    score_2.title("score")
    score_1=Label(score_2, text="les anciens score : \n"+content)
    score_1.pack()
    score_2.mainloop()
    return

def franchi(rep,ch,ch2,ch3,vie):
    if rep==0:
        ch.destroy()        #reste dans la salle mais supprime le choix invalide
        global rep10
        rep10=0
    elif rep==1:
        ch.destroy()
        ch2.destroy()
        ch3.destroy()
        suivant=Button(fenetre,text="Suivante",command=suiv)
        suivant.pack()
    else:
        ch.destroy()
        ch2.destroy()
        ch3.destroy()
        suivant=Button(fenetre,text="Suivante",command=suiv)
        suivant.pack(pady=5)
    return

def rep1():
    txt.set(liste[n][4])    #appelle dans la liste salle_n les éléments de reponse
    global rep
    rep=liste[n][7]
    franchi(rep,ch1,ch2,ch3,vie)
    return rep

def rep2():
    txt.set(liste[n][5])
    global rep
    rep=liste[n][8]
    franchi(rep,ch2,ch1,ch3,vie)
    return

def rep3():
    txt.set(liste[n][6])
    global rep
    rep=liste[n][9]
    franchi(rep,ch3,ch1,ch2,vie)
    return

def coffrenon():
    txt.set("Vous avez sérieusement fait tout le donjon pour arriver à la fin sans prendre votre récompense ?")
    non.destroy()
    oui.destroy()
    suivant=Button(fenetre,text="Bon, vous l'ouvrez du coup ?",command=suiv)
    suivant.pack(pady=5)
    return

def suite():
    global pvmoi
    pvlost=randrange(30,45)
    pvmoi=pvmoi-pvlost
    text.set("Le prof de math vous inflinge "+str(pvlost))
    pvprof.set("Le prof a "+str(pvboss)+" pv")
    pvjoueur.set("Vous avez "+str(pvmoi)+" pv")
    if pvmoi<=0:
        attaque.destroy()
        soin.destroy()
        continuer=Button(fenetre,text="Vous avez perdu !",command=gameover)
        continuer.pack(pady=5)
    elif pvboss<=0:
        attaque.destroy()
        soin.destroy()
        continuer=Button(fenetre,text="Vous avez gagné !",command=victoire)
        continuer.pack(pady=5)
    return

def att():  #fonction attaque pour le combat contre le boss
    n=randrange(len(listeatt))
    global pvboss
    pvdamage=randrange(40,60)
    pvboss=pvboss-pvdamage
    txt.set("Vous utilisez "+listeatt[n]+" et infliger "+str(pvdamage)+" de dégâts au prof de math.")
    suite()
    return

def soin():     #fonction soin pour le combat
    global pvmoi
    pvmoi=pvmoi+40
    txt.set("Vous vous soignez et regagnez 40 points de vie.")
    suite()
    return

score=10000
vie=3
salle_a_franchir=5
rep10=1
commencer=1
#mettre liste de salle
salle01=[0,0,0,0,0,0,0,0,0,0,0]           #permet d'initialiser une liste avec la bonne longueur
salle01[0]="Vous entrez dans une salle. Il y a un bouton pressoir rouge au milieu."+"\n"+"Vous décidez de :"        #choix 1
salle01[1]="Le presser délicatement"                                                                          
salle01[2]="L'utiliser comme un buzzer de Question pour un champion en vous défoulant dessus"                    
salle01[3]="De le contourner et d'essayer d'ouvrir la porte"                                                        #réponse 1
salle01[4]="Cela ne fait rien du tout"                                                                              
salle01[5]="Vous y êtes allé un peu fort. \n Vous le cassez, trébuchez sur le socle et perdez une vie. \n Dans votre mésaventure, vous avez défoncé la porte et pouvez passer à la salle suivante."
salle01[6]="Elle s'ouvre normalement et vous partez"                                                                #réponse 3
salle01[7]=0                                                                                                        #indice de passage
salle01[8]=1
salle01[9]=2
salle01[10]="image_gif/salle_bois.gif"  #adresse de l'image correspondente

salle02=[0,0,0,0,0,0,0,0,0,0,0]
salle02[0]="Un golem de pierre portant un magnifique noeud papillon vous attend de pied ferme."
salle02[1]="Vous le complimentez sur son noeud papillon rouge"
salle02[2]="Vous l'attaquez en visant la tête"
salle02[3]="Vous faîtes comme si ce n'était qu'une statue en voulant le contournez"
salle02[4]="Il est très flatté et vous laisse passer"
salle02[5]="Ce n'est pas très efficace mais après une bataille acharnée, vous arrivez à fuir. \n Vous avez perdu une vie."
salle02[6]="Il vous bloque la porte et vous lance un regard noir"
salle02[7]=2
salle02[8]=1
salle02[9]=0
salle02[10]="image_gif/Salle_golem.gif"

salle03=[0,0,0,0,0,0,0,0,0,0,0]
salle03[0]="Un dragon est endormi près d'une porte en bois. A vos pieds se trouve une salade et une grande épée."
salle03[1]="Vous essayez de l'enjamber en étant le plus discret possible"
salle03[2]="Vous ramassez la salade et lui lancez dessus."
salle03[3]="Vous prenez l'épée et votre courage à deux mains pour aller ocsire le dragon pendant qu'il est encore endormi."
salle03[4]="Il n'était pas vraiment endormi et vous regarde fixement. Vous décidez de faire autre chose."
salle03[5]="Il relève la tête, observe la salade et la mange en vous laissant passer. Vous êtes content d'avoir eu affaire à un dragon végétarien."
salle03[6]="L'épée était rouillée et se casse. Le dragon semble irité et inonde la pièce d'un souffle ardent. \n Vous réussissez à passer à travers la porte en flamme mais vous perdez une vie."
salle03[7]=0
salle03[8]=2
salle03[9]=1
salle03[10]="image_gif/salle_dragon.gif"

salle04=[0,0,0,0,0,0,0,0,0,0,0]
salle04[0]="Vous arrivez devant une porte blindée et devant vous se trouve du matériel étrange. \n Vous prenez:"
salle04[1]="Le matériel de crochetage"
salle04[2]="Un genre de bouteille d'acide"
salle04[3]="Une pelle"
salle04[4]="Le crochet se casse à force de vous acharnez dessus. Vous ne savez même pas crocheter les serrures."
salle04[5]="La porte est dissoute mais vous vous êtes blessés en manipulant l'acide sans protection. \n Vous perdez une vie."
salle04[6]="Vous creusez un trou dans la terre meuble du donjon sous la porte et vous sortez de la salle sans problème."
salle04[7]=0
salle04[8]=1
salle04[9]=2
salle04[10]="image_gif/salle_blindee.gif"

salle05=[0,0,0,0,0,0,0,0,0,0,0]
salle05[0]="Un gladiateur vous attends depuis des lustres et vous provoque en duel en vous tendant 3 armes. \n Vous choisissez:"
salle05[1]="Une massue assez lourde"
salle05[2]="Une rapière souple"
salle05[3]="Un gantelet vraiment classe"
salle05[4]="Vous n'arrivez même pas à la soulever. Il vous demande de prendre une autre arme."
salle05[5]="Vos quelques années d'escrimes vous servent enfin à quelque chose ! \n Vous le battez à plate couture et passez à la salle suivante."
salle05[6]="Il est plus fort que vous et vous perdez. Cependant il est admiratif de votre courage et vous laisse passer à la salle suivante. \n Vous perdez tout de même une vie."
salle05[7]=0
salle05[8]=2
salle05[9]=1
salle05[10]="image_gif/salle_gladiateur.gif"

salle06=[0,0,0,0,0,0,0,0,0,0,0]
salle06[0]="La porte que vous devez atteindre se trouve derrière une rivière marécageuse infestée de crocodiles."
salle06[1]="Vous prenez un grapin qui se trouve à vos pieds et l'accrocher sur un petit crochet au plafond."
salle06[2]="Vous tentez de marcher sur les crocodiles comme si c'était des rondins de bois."
salle06[3]="Vous escaladez le mur pour arriver de l'autre côté de la rive"
salle06[4]="Le crochet s'est cassé alors que vous étiez en cours de traverser. \n Votre petit séjour chez les crocodiles vous a fait perdre une vie."
salle06[5]="Vous vous approchez de l'eau et les crocodiles vous regardent d'un air affamé. Vous vous abstenez de leur sauter dessus."
salle06[6]="Vous y êtes arrivé malgré le peu de force que vous avez dans les bras. Vous les massez doucement alors que vous entrez dans la pièce suivante."
salle06[7]=1
salle06[8]=0
salle06[9]=2
salle06[10]="image_gif/salle_croco.gif"

salle07=[0,0,0,0,0,0,0,0,0,0,0]
salle07[0]="La porte que vous cherchez à atteindre se trouve derrière un gouffre. \n Un pont branlant fait de cordes tressées le traverse. \n Que faites-vous ?"
salle07[1]="Vous traversez le pont très peu engageant."
salle07[2]="Vous accrochez le grappin au-dessus de la porte et vous en servez pour passer le gouffre."
salle07[3]="Vous testez avec votre pied s'il n'y a pas un chemin invisible comme dans tous les bons jeux d'aventures."
salle07[4]="Il a étonnement tenu bon et vous êtes arrivés sain et sauf."
salle07[5]="Le grappin vous a propulsé un peu trop fort et vous vous écrasés sur la paroi d'en face. \n Vous perdez un point de vie."
salle07[6]="Vous regardez par-dessus le bord de la falaise et vous vous dites qu'il vaut mieux faire autre chose."
salle07[7]=2
salle07[8]=1
salle07[9]=0
salle07[10]="image_gif/salle_gouffre.gif"

salle08=[0,0,0,0,0,0,0,0,0,0,0]
salle08[0]="Vous entrez dans une salle comportant trois issues. \n Laquelle choisissez-vous ?"
salle08[1]="Ouvrir la porte en vieux bois vermoulue."
salle08[2]="Un muret en pierre franchissable."
salle08[3]="Une paroi lisse sous laquelle passe un tunnel."
salle08[4]="Vous passez la porte et entrez dans une grange qui ne tenait que grâce à la porte, vous sortez in extremis."
salle08[5]="Vous escaladez le muret et sautez de l'autre côté mais une pierre vous tombe sur la tête. \n Vous perdez un point de vie."
salle08[6]="Vous rampez dans le tunnel et ressortez de l'autre côté sain et sauf à part une tache de boue sur les genoux."
salle08[7]=0
salle08[8]=1
salle08[9]=2
salle08[10]="image_gif/salle_3issues.gif"

salle09=[0,0,0,0,0,0,0,0,0,0,0]
salle09[0]="Une porte se dresse devant vous. \n Pour l'ouvrir, vous devez répondre à l'égnime écrite dessus : \n Pinischo, oua nischba, hibou niche où ?"
salle09[1]="Ibounischnioniba. Ibounischlaba."
salle09[2]="Euh dans un arbre ?"
salle09[3]="L'hibou niche haut."
salle09[4]="Votre charabia s'averre être la bonne réponse. La porte s'ouvre."
salle09[5]="Ca n'a pas l'air d'être ça."
salle09[6]="Une pie vous attaque. Vous perdez une vie mais au moins la porte s'ouvre."
salle09[7]=2
salle09[8]=0
salle09[9]=1
salle09[10]="image_gif/salle_enigme.gif"

salle10=[0,0,0,0,0,0,0,0,0,0,0]
salle10[0]="Vous vous trouvez devant une porte en bois. \n Que faites-vous ?"
salle10[1]="Vous tentez de l'ouvrir."
salle10[2]="Vous essayez de l'enfoncer à coups d'épaule."
salle10[3]="Vous tocquez à la porte."
salle10[4]="Vous ouvrez la porte et tombez sur une bande d'orques contre lesquels vous jouez à papier-caillou-ciseaux. \n Vous gagnez car vous arrivez à les convaincre que les ciseaux coupent la pierre."
salle10[5]="Vous enfoncez la porte mais vous vous faites mal et perdez un point de vie en trébuchant."
salle10[6]="Vous tocquez à la porte et attendez jusqu'au soir mais personne ne répond."
salle10[7]=2
salle10[8]=1
salle10[9]=0
salle10[10]="image_gif/salle_bois.gif"

salle11=[0,0,0,0,0,0,0,0,0,0,0]
salle11[0]="Vous vous retrouvez devant un troll, il à l'air d'être occupé à réfléchir au sens de la vie, ce qui ne doit pas arriver souvent... \n Que faites vous ?"
salle11[1]="Je l'attaque en criant"
salle11[2]="Je passe comme si de rien n'était."
salle11[3]="Je me faufile en esperant passer inaperçu"
salle11[4]="Il n'a pas apprecié que vous l'embétiez et vous donne un coup qui vous propulse à la sortie et vous fait perdre un point de vie."
salle11[5]="Il vous fait un salut en vous voyant."
salle11[6]="Vous marcher sur une brindille, ce qui révèle votre présence, par esprit de survie vous prenez vos jambes à votre cou et vous vous retrouvez au point initial."
salle11[7]=1
salle11[8]=2
salle11[9]=0
salle11[10]="image_gif/Salle_troll.gif"

salle12=[0,0,0,0,0,0,0,0,0,0,0]
salle12[0]="Vous êtes devant un mur avec trois portes, laquelle ouvrez-vous ?"
salle12[1]="Première porte: Lions affamés depuis trois ans"
salle12[2]="Deuxième porte: Dojo remplie de ninja"
salle12[3]="Troisième porte: Ne pas déranger !"
salle12[4]="En effet, les lions étaient tellement affamé qu'il en sont mort. Vous passez."
salle12[5]="Vous dérangez les ninja en plein exercice. Ils vous filent une raclée et vous laissent tranquile. Vous pouvez passer."
salle12[6]="Vous tombez sur une famille de nains barbus jusqu'aux genoux. Ils sont complétement saoul et un peu agressif. Il vaut mieux que vous sortiez vite de là avant que ça ne dégénère."
salle12[7]=2
salle12[8]=1
salle12[9]=0
salle12[10]="image_gif/salle_lionninja.gif"

salle13=[0,0,0,0,0,0,0,0,0,0,0]
salle13[0]="Vous avancez dans la salle et tombez nez à nez avec un Tyranosaure. \n Que faîtes vous ?"
salle13[1]="Je cours en espérant allez plus vite"
salle13[2]="Je prend un bâton. Le lance et lui dit d'aller le chercher."
salle13[3]="Je ne bouge pas d'un cheveux"
salle13[4]="Et bien non ! Il va plus vite et vous écrase, puis continue son chemin. \n Vous perdez un point de vie."
salle13[5]="Il court après, et le rapporte. Ce dino est bien dressé et vous laisse donc passer. "
salle13[6]=" Il reste plantez devant vous tant qu'il n'a pas vu quelque chose bouger. En effet, son accuité visuelle est basé sur le mouvement !"
salle13[7]=1
salle13[8]=2
salle13[9]=0
salle13[10]="image_gif/salle_trex.gif"

liste=[salle01,salle02,salle03,salle04,salle05,salle06,salle07,salle08,salle09,salle10,salle11,salle12,salle13] #liste des salles. Chaque salle est une liste dont on appelle chaque élément
if commencer==1:
    commencer=0
    fenetre=Tk()    #indique le fait que la variable fenetre est un objet tkinter
    fenetre.title("présenation jeu")    #titre de la fenêtre
    image_fond=PhotoImage(file="image_gif/salle_bois_1.gif")    #va chercher l'image à la destination indiquée
    canvas=Canvas(fenetre,width=1000,height=500)    #créer un cadre tkinter
    canvas.create_image(500, 250, image=image_fond) #met l'image en fond de fenêtre
    canvas.pack()   #permet d'afficher la zone "canvas"
    txte = StringVar()  #indique que txte est une variable de type string
    txte.set("Bienvenue dans Troll's Dungeon. \n Ce donjon est composé de cinq salles changeant en permanence. \n Afin de passer une salle vous avez le choix entre trois réponses à chaque fois. \n Vous possédez trois points de vie, dans chaque salle une action vous fait perdre un point de vie, \n une autre vous empêche de passer et vous propose de choisir une autre action \n et enfin, la dernière, vous permet de passer sans perte de point de vie. \n Le but est d'arriver à la salle finale et de récupérer le coffre au trésor du donjon. \n Bonne chance Aventurier !")
    présentation=Label(fenetre,textvariable=txte)   #créer une zone de texte dans la fenêtre
    présentation.pack() #affiche cette zone
    commencer_donjon=Button(fenetre,text="commencer",command=suiv)  #créer un bouton qui utilise la fonction suiv quand il est pressé
    commencer_donjon.pack(pady=5)   #affiche le bouton avec une certaine marge
    fenetre.mainloop()  #affiche la fenêtre
while vie>0 and salle_a_franchir>0:
        n=randrange(len(liste)) #prend une salle aléatoire dans la liste des salles
        salle_a_franchir=salle_a_franchir-1
        fenetre=Tk()
        fenetre.title("essai jeu")
        imagefond=PhotoImage(file=liste[n][10])
        canvas=Canvas(fenetre,width=600,height=350)
        canvas.create_image(300, 175, image=imagefond)
        canvas.pack()
        txt = StringVar()
        txt.set(liste[n][0])
        description=Label(fenetre,textvariable=txt)
        description.pack()
        ch1=Button(fenetre,text=liste[n][1],command=rep1)   #appelle la fonction rep1
        ch1.pack(pady=5)
        ch2=Button(fenetre,text=liste[n][2],command=rep2)   #appelle la fonction rep2
        ch2.pack(pady=5)
        ch3=Button(fenetre,text=liste[n][3],command=rep3)   #appelle la fonction rep3
        ch3.pack(pady=5)
        fenetre.mainloop()
        del(liste[n])   #supprime de la liste la salle que l'on vient de visiter
        if rep==1:
            vie=vie-1
            score=score-1000    #gestion du score
        if rep10==0:
            score=score-500
            rep10=1

if vie>0:
    fenetre=Tk()
    fenetre.title("Fin ?")
    txt = StringVar()
    imagefond=PhotoImage(file="image_gif/salle_coffre.gif")
    txt.set("Il y a un coffre devant vous. L'ouvrez-vous ?")
    canvas=Canvas(fenetre,width=700,height=300)
    canvas.create_image(350, 150, image=imagefond)
    canvas.pack()
    description=Label(fenetre,textvariable=txt)
    description.pack()
    oui=Button(fenetre,text="oui",command=suiv)
    oui.pack(pady=5)
    non=Button(fenetre,text="non",command=coffrenon)
    non.pack(pady=5)
    fenetre.mainloop()
    pvmoi=200
    pvboss=300
    listeatt=["Le Théorème de Thalès","Le Théorème de Pythagore","Le Théorème des valeurs intermédiaires","la Loi de Bernoulli","La Recurrence","La Loi Binomiale"]
    fenetre=Tk()    
    fenetre.title("Boss final")    
    imagefond=PhotoImage(file="image_gif/salle_boss.gif")
    canvas=Canvas(fenetre,width=800,height=400)
    canvas.create_image(400, 200, image=imagefond)
    canvas.pack()
    pvjoueur=StringVar()
    pvjoueur.set("Vous avez "+str(pvmoi)+" pv")
    pvprof=StringVar()
    pvprof.set("Le prof a "+str(pvboss)+" pv")
    pv=Label(fenetre,textvariable=pvjoueur)
    pv.pack(side=LEFT,padx=5,pady=5)    #side=left : met à gauche de la fenêtre
    pv2=Label(fenetre,textvariable=pvprof)
    pv2.pack(side=RIGHT,padx=5,pady=5)
    txt = StringVar()
    txt.set("Le coffre vous fait tomber dans une grande salle. \n Un stagiaire voulant devenir prof de maths apparaît et entame le combat avec vous.")
    description=Label(fenetre,textvariable=txt)
    description.pack()
    text=StringVar()
    text.set("")
    degat=Label(fenetre,textvariable=text)
    degat.pack()
    attaque=Button(fenetre,text="Attaque",command=att)
    attaque.pack(pady=5)
    soin=Button(fenetre,text="Soin",command=soin)
    soin.pack(pady=5)
    fenetre.mainloop()


else:
    score=score-(salle_a_franchir*2000)
    gameover()
