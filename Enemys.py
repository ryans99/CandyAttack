#Tower class
#Justin Vicinte, Christopher Campos
# 13 may, 2017
class Enemy():

    def __init__(self,EnemyType,EnemySpeed,EnemyHealth,EnemyCoordinates):

        self.type = EnemyType
        self.speed = EnemySpeed
        self.Total_health = EnemyHealth
        self.Current_health = EnemyHealth
        self.x = EnemyCoordinates.x
        self.y = EnemyCoordinates.y


    def Move_Forward(self):
        self.y += 1

    def Move_Left(self):
        self.x += 1

    def Move_Right(self):
        self.x -= 1

    #def Move_Possible(self):