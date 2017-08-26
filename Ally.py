
#Ally class

#Justin Vicinte, Christopher Campos, Ryan Schackel

# 25 Agusust, 2017

class Ally():



    def __init__(self,AllyType,AllySpeed,AllyHealth):



        self.type = AllyType

        self.speed = AllySpeed

        self.health = AllyHealth



    def heal(self):

        self.health += self.health
