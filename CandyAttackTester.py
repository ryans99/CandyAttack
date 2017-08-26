from Enemys import Enemy
from Tower import Tower
enemy = Enemy(15,15,15)
tower = Tower("f",100,5)
print(tower.shoot(enemy))
tower.upgrade()
towers = []
enemys = []
for i in range(10):
    towers.append(Tower(i,15*i,1*(i)))
    enemys.append(Enemy(i,5,20))
print(enemys)
print(towers)