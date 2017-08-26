#Enemy class
#Justin Vicinte, Christopher Campos
# 13 may, 2017
class Enemy():

    def __init__(self,EnemyType,EnemySpeed,EnemyHealth):

        self.type = EnemyType
        self.speed = EnemySpeed
        self.health = EnemyHealth

    def heal(self):
        self.health += self.health
