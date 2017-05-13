#Tower class
#Justin Vicinte, Christopher Campos
# 13 may, 2017
class Tower():

    #Initiation for Towers
    def __init__(self,TowerType,TowerCost,dps):
        self.type = TowerType
        self.cost = TowerCost
        self.damadge = dps
        self.location = None

    def shoot(self,Enemy):
        Enemy.health -= self.damadge
        return Enemy.health