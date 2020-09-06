class Player:

    def __init__(self, x, y, health, force, speed, job):
        save_file = open('Save.txt', 'r')
        lines = save_file.readlines()
        self.x = x
        self.y = y
        self.prevx = x
        self.prevy = y
        self.health = int(lines[2].split()[0])
        self.maxhealth = int(lines[5].split()[0])
        self.force = int(lines[3].split()[0])
        self.maxforce = int(lines[6].split()[0])
        self.speed = speed
        self.job = job
        self.attack = False
        self.dmg = int(lines[4].split()[0])
        self.isLeft = False
        self.isMove = False
        self.level = int(lines[0].split()[0])
        self.exp = int(lines[8].split()[0])
        self.abilities = []
        skills = lines[7].split()
        skills.pop()
        for ability in skills:
            self.abilities.append(ability)

        self.boltLvl = int(lines[9].split()[0])
        self.healLvl = int(lines[10].split()[0])
        self.boltCost = 25 + (self.boltLvl - 1)*5
        self.healCost = 25 + (self.healLvl - 1) * 2
        self.boltDmg = 80 + (self.boltLvl - 1) * 10
        self.healDmg = 50 + (self.healLvl - 1) * 5
        self.points = int(lines[11].split()[0])

        save_file.close()

    def move(self):
        self.x += 5

    def levelCheck(self):
        if self.exp >= (self.level * 1000):
            self.exp -= self.level * 1000
            self.health += 20
            self.maxhealth += 20
            self.maxforce += 50
            self.force = self.maxforce
            self.level += 1
            self.dmg += 5
            self.newSkill()
            if self.level%3 == 0:
                self.points += 1

    def newSkill(self):
        if self.level == 3:
            self.abilities.append('ForceBolt')

    def updateSkills(self):
        self.boltCost = 25 + (self.boltLvl - 1) * 5
        self.healCost = 25 + (self.healLvl - 1) * 2
        self.boltDmg = 80 + (self.boltLvl - 1) * 10
        self.healDmg = 50 + (self.healLvl - 1) * 5

class Trooper:

    def __init__(self):
        self.x = 50
        self.y = 100
        self.index = 0
        save_file = open('Save.txt', 'r')
        lines = save_file.readlines()
        self.lvl = int(lines[13].split()[0])
        self.health = int(lines[14].split()[0])
        self.maxhealth = (75 + (self.lvl * 25))/100
        self.dmg = 25 + (self.lvl * 5)
        self.attack = False
