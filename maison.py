from turtle import *

# Pour nommer la fenêtre de jeu
title("Le jeu du Nabila !")

def house():
    
    begin_fill()
    color('black', 'pink')
    forward(141)
    left(90)
    forward(100)
    left(45)
    forward(100)
    left(90)
    forward(100)
    left(45)
    forward(100)
    left(90)
    goto(140, 100,)
    forward(-141)
    left(90)
    goto(140, 0)
    end_fill()
    
#     end_fill()

width(4)
house()
up()
right(90)
fd(110)

down()
color('black', 'pink')
forward(141)
left(90)
forward(100)
left(45)
forward(100)
left(90)
forward(100)
left(45)
forward(100)

# draw a door
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
left(90)
up()
right(0)
fd(-110)
down()

down()
color('black')
forward(141)
left(90)
forward(100)
left(45)
forward(100)
left(90)
forward(100)
left(45)
forward(100)

# draw a door
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
left(90)

down()
up()
right(0)
fd(-110)
# house()

up()
right(0)
fd(-110)

# Rayon du cercle utilisé pour la tête du pendu
rayon=25

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
end_fill()
up()
right(-50)
fd(110)
#arbre
# Rayon du cercle utilisé pour la tête du pendu
rayon=25

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

#article derccc
end_fill()
up()
right(-50)
fd(250)

down()
color('black')
forward(141)
left(90)
forward(100)
left(45)
forward(100)
left(90)
forward(100)
left(45)
forward(100)

# draw a door
left(90)
forward(50)
left(90)
color('pink')
forward(50)
right(90)
forward(30)
right(90)
forward(50)
left(90)
width(4)
end_fill()



end_fill()
up()
right(0)
fd(-750)

down()
color('black')
forward(141)
left(90)
forward(100)
left(45)
forward(100)
left(90)
forward(100)
left(45)
forward(100)

# draw a door
left(90)
forward(50)
left(90)
color('pink')
forward(50)
right(90)
forward(30)
right(90)
forward(50)
left(90)
width(4)
end_fill()
down()
up()
right(0)
fd(-110)


# Message de fin
up()
right(140)
fd(30)
right(90)
fd(100)
down()
color("black")
write("Nabila !")
up()
left(290)
fd(450)
turtle.bgcolor("blue")
