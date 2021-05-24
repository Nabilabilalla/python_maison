from turtle import *
# Pour nommer la fenêtre de jeu
title("Le jeu du pendu !")

# Rayon du cercle utilisé pour la tête du pendu
rayon=20

# Vitesse d'éxécution du dessin
speed("fast")


# Corde
width(3)
right(90)


# Tête
color("pink")
right(90)
begin_fill()
circle(rayon)
end_fill()

# Repositionner la flèche
up()
left(90)
fd(rayon*2)
down()

# Le corps
color("black")
right(360)
fd(100)

# Repositionner la flèche
up()
left(180)
fd(80)
down()

# Premier bras
right(125)
fd(50)

# Repositionner la flèche
up()
right(180)
fd(50)
down()

# Deuxième bras
left(75)
fd(50)

# Repositionner la flèche
up()
bk(50)
left(50)
fd(80)
down()

# Première jambe
left(45)
fd(60)

# Repositionner la flèche
up()
bk(60)
down()

# Deuxième jambe
right(90)
fd(60)
# Repositionner la flèche
up()
bk(60)
left(225)
fd(125)
left(90)
fd(8)
down()
# Oeil gauche
width(2)
left(45)
fd(8)
bk(4)
left(90)
fd(4)
bk(4)
left(180)
fd(4)
bk(4)

# Repositionner la flèche
up()
right(140)
fd(16)
down()

# Oeil droit
left(45)
fd(8)
bk(4)
left(90)
fd(4)
bk(4)
left(180)
fd(4)
bk(4)

# Message de fin
up()
right(40)
fd(300)
right(90)
fd(100)
down()
color("red")
write("PENDU !")
up()
left(90)
fd(350)