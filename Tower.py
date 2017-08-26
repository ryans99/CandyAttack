# Tower class
# Justin Vicinte, Christopher Campos
# 13 may, 2017
class Tower():

    # Initiation for Towers
    def __init__(self, TowerType, TowerCost, dps):
        self.type = TowerType
        self.cost = TowerCost
        self.damadge = dps
        self.location = None
        self.level = 1

    def shoot(self, Enemy):
        Enemy.health -= self.damadge
        return Enemy.health
        # Add Code For Animation

    def upgrade(self):
        if (self.level + 1) > 3:
            return
        else:
            self.level += 1
            self.damadge += 0.15 * (self.damadge)  # Increases in percent before multiplication
