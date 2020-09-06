import pygame
import math
import random
import enemy
import player

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Arial', 40, 'bold')
font2 = pygame.font.SysFont('Arial', 30, 'bold')

#Backgrounds
geonosis_arena1 = pygame.image.load('geonosis_arena1.png')
geonosis_arena2 = pygame.image.load('geonosis_arena2.png')
geonosis_arena3 = pygame.image.load('geonosis_arena3.png')
geonosis_arena4 = pygame.image.load('geonosis_arena4.png')
geonosis_arena5 = pygame.image.load('geonosis_arena5.png')
dfactory1 = pygame.image.load('dfactory1.png')
dfactory2 = pygame.image.load('dfactory2.png')
dfactory3 = pygame.image.load('dfactory3.png')
dfactory4 = pygame.image.load('dfactory4.png')
dfactory5 = pygame.image.load('dfactory5.png')
dfactory6 = pygame.image.load('dfactory6.png')
dfactory7 = pygame.image.load('dfactory7.png')
dfactory8 = pygame.image.load('dfactory8.png')
dfactory9 = pygame.image.load('dfactory9.png')
dfactory10 = pygame.image.load('dfactory10.png')
dfactory11 = pygame.image.load('dfactory11.png')
dfactory12 = pygame.image.load('dfactory12.png')
dfactory13 = pygame.image.load('dfactory13.png')
dfactory14 = pygame.image.load('dfactory14.png')
dfactory15 = pygame.image.load('dfactory15.png')
dfactory16 = pygame.image.load('dfactory16.png')
dfactory17 = pygame.image.load('dfactory17.png')
dfactory18 = pygame.image.load('dfactory18.png')
dfactory19 = pygame.image.load('dfactory19.png')
dfactory20 = pygame.image.load('dfactory20.png')
dfactory21 = pygame.image.load('dfactory21.png')
dfactory22 = pygame.image.load('dfactory22.png')
dfactory23 = pygame.image.load('dfactory23.png')
dfactory24 = pygame.image.load('dfactory24.png')
dfactory25 = pygame.image.load('dfactory25.png')
dfactory26 = pygame.image.load('dfactory26.png')
dfactory27 = pygame.image.load('dfactory27.png')
dfactory28 = pygame.image.load('dfactory28.png')
dfactory29 = pygame.image.load('dfactory29.png')
dfactory30 = pygame.image.load('dfactory30.png')
dfactory31 = pygame.image.load('dfactory31.png')
dfactory32 = pygame.image.load('dfactory32.png')
dfactory33 = pygame.image.load('dfactory33.png')
dfactory34 = pygame.image.load('dfactory34.png')
dfactory35 = pygame.image.load('dfactory35.png')
dfactory36 = pygame.image.load('dfactory36.png')

#Sprites
ana = pygame.image.load('anakin_1.png')
ana_win1 = pygame.image.load('anakin_win1.png')
ana_r1 = pygame.image.load('anakin_run1.png')
ana_r2 = pygame.image.load('anakin_run2.png')
ana_r3 = pygame.image.load('anakin_run3.png')
ana_r4 = pygame.image.load('anakin_run4.png')
ana_r5 = pygame.image.load('anakin_run5.png')
ana_r6 = pygame.image.load('anakin_run6.png')
ana_r7 = pygame.image.load('anakin_run7.png')
ana_r8 = pygame.image.load('anakin_run8.png')
ana_r9 = pygame.image.load('anakin_run9.png')
ana_r10 = pygame.image.load('anakin_run10.png')
ana_r11 = pygame.image.load('anakin_run11.png')
ana_r12 = pygame.image.load('anakin_run12.png')
ana_r13 = pygame.image.load('anakin_run13.png')
ana_h1 = pygame.image.load('anakin_hit1.png')
ana_h2 = pygame.image.load('anakin_hit2.png')
ana_h3 = pygame.image.load('anakin_hit3.png')
ana_h4 = pygame.image.load('anakin_hit4.png')
ana_h5 = pygame.image.load('anakin_hit5.png')
ana_h6 = pygame.image.load('anakin_hit6.png')
ana_h7 = pygame.image.load('anakin_hit7.png')
ana_h8 = pygame.image.load('anakin_hit8.png')
ana_h9 = pygame.image.load('anakin_hit9.png')
ana_heal1 = pygame.image.load('ana_heal1.png')
ana_heal2 = pygame.image.load('ana_heal2.png')
ana_heal3 = pygame.image.load('ana_heal3.png')
ana_heal4 = pygame.image.load('ana_heal4.png')
ana_heal5 = pygame.image.load('ana_heal5.png')
ana_heal6 = pygame.image.load('ana_heal6.png')
ana_heal7 = pygame.image.load('ana_heal7.png')
ana_heal8 = pygame.image.load('ana_heal8.png')
ana_heal9 = pygame.image.load('ana_heal9.png')
ana_bolt1 = pygame.image.load('ana_bolt1.png')
ana_bolt2 = pygame.image.load('ana_bolt2.png')
ana_bolt3 = pygame.image.load('ana_bolt3.png')
ana_bolt4 = pygame.image.load('ana_bolt4.png')
ana_bolt5 = pygame.image.load('ana_bolt5.png')
ana_bolt6 = pygame.image.load('ana_bolt6.png')
ana_bolt7 = pygame.image.load('ana_bolt7.png')
ana_bolt8 = pygame.image.load('ana_bolt8.png')
ana_bolt9 = pygame.image.load('ana_bolt9.png')
ana_bolt10 = pygame.image.load('ana_bolt10.png')
ana_bolt11 = pygame.image.load('ana_bolt11.png')
ana_bolt12 = pygame.image.load('ana_bolt12.png')
ana_bolt13 = pygame.image.load('ana_bolt13.png')
ana_bolt14 = pygame.image.load('ana_bolt14.png')
b_droid1 = pygame.image.load('battle_droid1.png')
bdroid_att1 = pygame.image.load('bdroid_att1.png')
bdroid_att2 = pygame.image.load('bdroid_att2.png')
bdroid_att3 = pygame.image.load('bdroid_att3.png')
bdroid_att4 = pygame.image.load('bdroid_att4.png')
bdroid_att5 = pygame.image.load('bdroid_att5.png')
bdroid_att6 = pygame.image.load('bdroid_att6.png')
bdroid_att7 = pygame.image.load('bdroid_att7.png')
bdroid_death1 = pygame.image.load('bdroid_death1.png')
bdroid_death2 = pygame.image.load('bdroid_death2.png')
bdroid_death3 = pygame.image.load('bdroid_death3.png')
bdroid_death4 = pygame.image.load('bdroid_death4.png')
bdroid_death5 = pygame.image.load('bdroid_death5.png')
bdroid_death6 = pygame.image.load('bdroid_death6.png')
bdroid_death7 = pygame.image.load('bdroid_death7.png')
bdroid_death8 = pygame.image.load('bdroid_death8.png')
bdroid_death9 = pygame.image.load('bdroid_death9.png')
sdroid_hit1 = pygame.image.load('sdroid_hit1.png')
sdroid_hit2 = pygame.image.load('sdroid_hit2.png')
sdroid_hit3 = pygame.image.load('sdroid_hit3.png')
sdroid_hit4 = pygame.image.load('sdroid_hit4.png')
sdroid_hit5 = pygame.image.load('sdroid_hit5.png')
sdroid_hit6 = pygame.image.load('sdroid_hit6.png')
sdroid_spec1 = pygame.image.load('sbdroid_spec1.png')
sdroid_spec2 = pygame.image.load('sbdroid_spec2.png')
sdroid_spec3 = pygame.image.load('sbdroid_spec3.png')
sdroid_spec4 = pygame.image.load('sbdroid_spec4.png')
sdroid_spec5 = pygame.image.load('sbdroid_spec5.png')
sdroid_spec6 = pygame.image.load('sbdroid_spec6.png')
sdroid_spec7 = pygame.image.load('sbdroid_spec7.png')
sdroid_spec8 = pygame.image.load('sbdroid_spec8.png')
sdroid_spec9 = pygame.image.load('sbdroid_spec9.png')
sbdroid_death1 = pygame.image.load('sbdroid_death1.png')
sbdroid_death2 = pygame.image.load('sbdroid_death2.png')
sbdroid_death3 = pygame.image.load('sbdroid_death3.png')
sbdroid_death4 = pygame.image.load('sbdroid_death4.png')
sbdroid_death5 = pygame.image.load('sbdroid_death5.png')
sbdroid_death6 = pygame.image.load('sbdroid_death6.png')
sbdroid_death7 = pygame.image.load('sbdroid_death7.png')
sbdroid_death8 = pygame.image.load('sbdroid_death8.png')
sbdroid_death9 = pygame.image.load('sbdroid_death9.png')
ct1 = pygame.image.load('ct1.png')
ct2 = pygame.image.load('ct2.png')
ct3 = pygame.image.load('ct3.png')
ct4 = pygame.image.load('ct4.png')
ct5 = pygame.image.load('ct5.png')
ct6 = pygame.image.load('ct6.png')

#HUD Sprites
battle_1 = pygame.image.load('battleHUD.png')
battle_1 = pygame.transform.scale(battle_1, (800, 200))
battle_done = pygame.image.load('victoryHUD.png')
battle_done = pygame.transform.scale(battle_done, (800, 200))
arrow = pygame.image.load('arrow.png')
arrow = pygame.transform.scale(arrow, (60, 30))
failRun = pygame.image.load('failedRunHUD.png')
failRun = pygame.transform.scale(failRun, (800, 200))
force_display = pygame.image.load('forceHUD.png')
force_display = pygame.transform.scale(force_display, (800, 200))
force_display2 = pygame.image.load('forceHUD2.png')
force_display2 = pygame.transform.scale(force_display2, (800, 200))
plus = pygame.image.load('plus.png')
plus = pygame.transform.scale(plus, (50, 50))

#Image lists
ana_run = [ana_r1, ana_r2, ana_r3, ana_r4, ana_r5, ana_r6, ana_r7, ana_r8, ana_r9, ana_r10, ana_r11, ana_r12, ana_r13]
geonosis_arenabg = [geonosis_arena1, geonosis_arena2, geonosis_arena3, geonosis_arena4, geonosis_arena5]
dfactory = [dfactory1, dfactory2, dfactory3, dfactory4, dfactory5, dfactory6, dfactory7, dfactory8,
            dfactory9, dfactory10, dfactory11, dfactory12, dfactory13, dfactory14, dfactory15, dfactory16,
            dfactory17, dfactory18, dfactory19, dfactory20, dfactory21, dfactory22, dfactory23, dfactory24, dfactory25,
            dfactory26, dfactory27, dfactory28, dfactory29, dfactory30, dfactory31, dfactory32, dfactory33, dfactory34,
            dfactory35, dfactory36]
ana_hit = [ana_h1, ana_h2, ana_h3, ana_h4, ana_h5, ana_h6, ana_h7, ana_h8, ana_h9]
bdroid_death = [bdroid_death1, bdroid_death2, bdroid_death3, bdroid_death4, bdroid_death5, bdroid_death6, bdroid_death7, bdroid_death8, bdroid_death9]
bdroid_att = [bdroid_att1, bdroid_att2, bdroid_att3, bdroid_att4, bdroid_att5, bdroid_att6, bdroid_att7]
sdroid_hit = [sdroid_hit1, sdroid_hit2, sdroid_hit3, sdroid_hit4, sdroid_hit5, sdroid_hit6]
sdroid_spec = [sdroid_spec1, sdroid_spec2, sdroid_spec3, sdroid_spec3, sdroid_spec4, sdroid_spec4,  sdroid_spec5, sdroid_spec6, sdroid_spec7, sdroid_spec8, sdroid_spec9]
sbdroid_death = [sbdroid_death1, sbdroid_death2, sbdroid_death3, sbdroid_death4, sbdroid_death5, sbdroid_death6, sbdroid_death7, sbdroid_death8, sbdroid_death9]
ana_heal = [ana_heal1, ana_heal2, ana_heal3, ana_heal4, ana_heal5, ana_heal6, ana_heal7, ana_heal8, ana_heal9]
ana_bolt = [ana_bolt1, ana_bolt2, ana_bolt3, ana_bolt4, ana_bolt5, ana_bolt6, ana_bolt7, ana_bolt8, ana_bolt9, ana_bolt10, ana_bolt11, ana_bolt12, ana_bolt13, ana_bolt14]
ct_hit = [ct1, ct2, ct3, ct4, ct5, ct6, ct1]

#Sounds
laser_sound = pygame.mixer.Sound('biglaser.wav')
saber_sound = pygame.mixer.Sound('lightsaber swing.wav')
heal_sound = pygame.mixer.Sound('Heal.wav')
explode_sound = pygame.mixer.Sound('Explosion.wav')
bolt_sound = pygame.mixer.Sound('force_push.wav')

#Music
music = pygame.mixer.music.load('Level 1 Track.wav')
pygame.mixer.music.play(-1)

#Read and open save
save_file = open('Save.txt', 'r')
lines = save_file.readlines()

#Variables
stage1 = False
stage2 = False
stages = [stage1, stage2]
stageindex = int(lines[12].split()[0])
stages[stageindex] = True
loopspeed = 0.1
bgindex = int(lines[1].split()[0])
i = 0
charindex = 0
enemyindex = 0
attack = False
startAttack = False
enemyAtt = False
attackOrder = []
arrowx = 20
arrowy = 430
current_arrow = ['up', 'left']
isBattle = False
enemyCount = 0
dice = 0
inFmenu = False
forceHeal = False
forceBolt = False
inMenu = False

#Objects
char = player.Player(100, 400, 100, 100, 5, 'Jedi')
b_droid = enemy.Bdroid(500, 400, 100, 2)
if bgindex == 4:
    b_droid = enemy.Sbdroid(500, 400, 300, 1)

#Close file
save_file.close()

def battle(char, enemy1):
    global charindex
    global enemyindex
    global startAttack
    global forceHeal
    global forceBolt
    global inFmenu
    global bgindex

    char.isMove = False
    char.isLeft = False

    if char.speed >= enemy1.speed:
        if isCol(char, enemy1) != True and char.attack:
            if charindex <= len(ana_run) - 1:
                charindex += loopspeed
                char.move()
            else:
                charindex = 0
            if isCol(char, enemy1):
                startAttack = True
                char.attack = False
                charindex = 0
                saber_sound.play()
        elif startAttack:
            if charindex <= len(ana_hit) - 1:
                charindex += loopspeed
            else:
                if enemy1.death != True:
                    enemy1.health -= char.dmg
                charindex = 0
                startAttack = False
                char.x = 100
                enemy1.attack = True
                if enemy1.healthCheck() != True:
                    if bgindex == 4:
                        if enemy1.mana >= 50:
                            saber_sound.play()
                        else:
                            laser_sound.play()
                    else:
                        laser_sound.play()
        elif forceHeal:
            if charindex <= len(ana_heal) - 1:
                charindex += loopspeed
            else:
                charindex = 0
                char.health += char.healDmg
                if char.health > char.maxhealth:
                    char.health = char.maxhealth
                char.force -= char.healCost
                enemy1.attack = True
                forceHeal = False
                inFmenu = False
                if enemy1.healthCheck() != True:
                    if bgindex == 4:
                        if enemy1.mana >= 50:
                            saber_sound.play()
                        else:
                            laser_sound.play()
                            print('test')
                    else:
                        laser_sound.play()
        elif forceBolt:
            if charindex <= len(ana_bolt) - 1:
                charindex += loopspeed
            else:
                charindex = 0
                char.force -= char.boltCost
                enemy1.health -= char.boltDmg
                forceBolt = False
                enemy1.attack = True
                inFmenu = False

        if enemy1.healthCheck() != True:
            if enemy1.attack:
                if bgindex == 4:
                    if enemy1.mana < 50:
                        if enemyindex < len(sdroid_hit) - 1:
                            enemyindex += loopspeed
                        else:
                            enemyindex = 0
                            char.health -= enemy1.dmg
                            enemy1.attack = False
                            enemy1.mana += 10
                    else:
                        enemy1.x = char.x + 50
                        if enemyindex < len(sdroid_spec) - 1:
                            enemyindex += loopspeed
                        else:
                            enemy1.x = 500
                            enemyindex = 0
                            char.health -= enemy1.dmg * 3
                            enemy1.mana -= 50
                            enemy1.attack = False
                else:
                    if enemyindex < len(bdroid_att) - 1:
                        enemyindex += loopspeed
                    else:
                        enemyindex = 0
                        char.health -= enemy1.dmg
                        enemy1.attack = False

        if enemy1.healthCheck() and enemy1.death != True:
            enemy1.health = 0
            explode_sound.play()
            if enemyindex <= len(bdroid_death) - 1:
                enemyindex += loopspeed
            else:
                enemyindex = 0
                char.exp += enemy1.exp
                char.levelCheck()
                b_droid.death = True

def charReset(char):
    global charindex

    char.x = 100
    char.y = 400
    charindex = 0

def draw_screen():
    screen.fill((0,0,0))
    bg = pygame.transform.scale(geonosis_arenabg[bgindex], (800, 600))
    char_image = pygame.transform.scale(ana, (100, 100))
    if char.isLeft:
        char_image = pygame.transform.flip(char_image, True, False)
    enemy_image = pygame.transform.scale(b_droid1, (100, 100))
    if bgindex == 4:
        enemy_image = pygame.transform.scale(sdroid_hit1, (100, 100))

    if isBattle and b_droid.death != True:
        screen.blit(bg, (0, -200))

        #HUD
        screen.blit(battle_1, (0, 400))
        if inFmenu:
            if 'ForceBolt' in char.abilities:
                force_HUD = force_display2
            else:
                force_HUD = force_display
            screen.blit(force_HUD, (0, 400))
        arrow.set_colorkey((255,255,255))
        screen.blit(arrow, (arrowx, arrowy))
    elif b_droid.death and isBattle:
        screen.blit(bg, (0, -200))

        # HUD
        screen.blit(battle_done, (0, 400))
    else:
        screen.blit(bg, (0,0))

    if char.attack or char.isMove:
        char_image = pygame.transform.scale(ana_run[int(charindex)], (100, 100))
        if char.isLeft:
            char_image = pygame.transform.flip(char_image, True, False)
    elif startAttack:
        char_image = pygame.transform.scale(ana_hit[int(charindex)], (100, 100))
    elif forceHeal:
        char_image = pygame.transform.scale(ana_heal[int(charindex)], (100, 100))
    elif forceBolt:
        char_image = pygame.transform.scale(ana_bolt[int(charindex)], (100, 100))

    if b_droid.healthCheck() and b_droid.death != True:
        enemy_image = pygame.transform.scale(bdroid_death[int(enemyindex)], (100, 100))
        if bgindex == 4:
            enemy_image = pygame.transform.scale(sbdroid_death[int(enemyindex)], (100, 100))
    elif b_droid.death:
        enemy_image = pygame.transform.scale(bdroid_death[8], (100, 100))
        if bgindex == 4:
            enemy_image = pygame.transform.scale(sbdroid_death[8], (100, 100))
        char_image = pygame.transform.scale(ana_win1, (100, 150))
    elif b_droid.attack:
        if bgindex == 4:
            if b_droid.mana < 50:
                enemy_image = pygame.transform.scale(sdroid_hit[int(enemyindex)], (100, 100))
            else:
                enemy_image = pygame.transform.scale(sdroid_spec[int(enemyindex)], (100, 100))
        else:
            enemy_image = pygame.transform.scale(bdroid_att[int(enemyindex)], (100, 100))

    char_image.set_colorkey((0,0,255))
    enemy_image.set_colorkey((0, 0, 255))

    screen.blit(enemy_image, (b_droid.x, b_droid.y))
    screen.blit(char_image, (char.x, char.y))

    #General HUD for char
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 175, 60))
    pygame.draw.rect(screen, (211, 211, 211), (60, 10, 100, 10))
    pygame.draw.rect(screen, (211, 211, 211), (60, 25, 100, 10))
    pygame.draw.rect(screen, (211, 211, 211), (60, 40, 100, 10))

    pygame.draw.rect(screen, (255, 0, 0), (60, 10, char.health/(char.maxhealth/100), 10))
    pygame.draw.rect(screen, (0, 0, 255), (60, 25, char.force/(char.maxforce/100), 10))
    pygame.draw.rect(screen, (0, 255, 0), (60, 40, char.exp/(char.level*10), 10))

    level_display = font.render(str(char.level), True, (0,255,0))
    screen.blit(level_display, (5, 5))

    if inMenu:
        screen.fill((127, 127, 127))
        level_display = font.render('Level: ' + str(char.level), True, (0,0,0))
        exp_display = font.render('Exp: ' + str(char.exp) + '/' + str(char.level * 1000), True, (0, 0, 0))
        power_display = font.render('Power: ' + str(char.dmg), True, (0,0,0))
        health_display = font.render('Health: ' + str(char.health) + '/' + str(char.maxhealth), True, (0, 0, 0))
        force2_display = font.render('Force: ' + str(char.force) + '/' + str(char.maxforce), True, (0, 0, 0))
        skills_display = font.render('Skill Points: ' + str(char.points), True, (0,0,0))
        heal_display = font.render('Force Heal:', True, (0,0,0))
        heal_info = font2.render('Lvl: ' + str(char.healLvl) + ' Dmg: ' + str(char.healDmg) + ' Cost: ' + str(char.healCost), True, (0,0,0))
        bolt_display = font.render('Force Bolt:', True, (0, 0, 0))
        bolt_info = font2.render('Lvl: ' + str(char.boltLvl) + ' Dmg: ' + str(char.boltDmg) + ' Cost: ' + str(char.boltCost), True, (0,0,0))


        screen.blit(level_display, (10, 10))
        screen.blit(exp_display, (10, 50))
        screen.blit(power_display, (10, 90))
        screen.blit(health_display, (10, 130))
        screen.blit(force2_display, (10, 170))
        screen.blit(skills_display, (10, 250))
        screen.blit(heal_display, (10, 290))
        screen.blit(heal_info, (10, 330))

        plus.set_colorkey((255, 255, 255))

        if 'ForceBolt' in char.abilities:
            screen.blit(bolt_display, (10, 380))
            screen.blit(bolt_info, (10, 420))
            if char.points > 0:
                screen.blit(plus, (230, 380))

        if char.points > 0:
            screen.blit(plus, (230, 290))

def draw_HUD():

    pygame.draw.rect(screen, (255, 0, 0), (b_droid.x, b_droid.y - 10, 100, 10))
    pygame.draw.rect(screen, (0, 255, 0), (b_droid.x, b_droid.y - 10, b_droid.health/b_droid.maxhealth, 10))

def isCol(t1, t2):
    distance = math.sqrt(math.pow(t1.x - t2.x, 2) + math.pow(t1.y - t2.y, 2))
    if distance < 50:
        return True
    else:
        return False

def isCol2(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distance < 50:
        return True
    else:
        return False

while stages[0]:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if isBattle:
                if event.key == pygame.K_RETURN:
                    if b_droid.healthCheck() != True and current_arrow == ['up', 'left']:
                        if inFmenu:
                            if char.force >= char.healCost and char.health < char.maxhealth:
                                charindex = 0
                                forceHeal = True
                                heal_sound.play()
                        else:
                            char.attack = True
                    elif current_arrow == ['down', 'right']:
                        if inFmenu != True:
                            dice = random.randint(0, 6)
                            if bgindex != 4:
                                if dice <= (2 + char.speed - b_droid.speed):
                                    isBattle = False
                                    char.health -= b_droid.dmg
                                    charReset(char)
                                    b_droid = enemy.Bdroid(1000, 400, 100, 2)
                                else:
                                    laser_sound.play()
                                    b_droid.attack = True
                    elif current_arrow == ['up', 'right'] and b_droid.healthCheck() != True:
                        if inFmenu != True:
                            inFmenu = True
                        elif char.force >= char.boltCost and 'ForceBolt' in char.abilities:
                            bolt_sound.play()
                            charindex = 0
                            forceBolt = True
                    elif b_droid.death:
                        isBattle = False
                        inFmenu = False
                        # Reset
                        charReset(char)
                        b_droid = enemy.Bdroid(1000, 400, 100, 2)
                        if bgindex == 2 and enemyCount == 0:
                            b_droid.x = 500
                            enemyCount += 1
                        if bgindex == 3:
                            b_droid = enemy.Sbdroid(1000, 400, 300, 1)
                elif event.key == pygame.K_RIGHT and ('right' in current_arrow) != True:
                    arrowx += 375
                    current_arrow[1] = 'right'
                elif event.key == pygame.K_LEFT and ('left' in current_arrow) != True:
                    arrowx -= 375
                    current_arrow[1] = 'left'
                elif event.key == pygame.K_UP and ('up' in current_arrow) != True:
                    arrowy -= 80
                    current_arrow[0] = 'up'
                elif event.key == pygame.K_DOWN and ('down' in current_arrow) != True:
                    arrowy += 80
                    current_arrow[0] = 'down'
                elif event.key == pygame.K_BACKSPACE:
                    inFmenu = False
            else:
                if inMenu:
                    if event.key == pygame.K_BACKSPACE:
                        inMenu = False
                    if event.key == pygame.K_s:
                        save_file = open('Save.txt', 'w').close()
                        save_file = open('Save.txt', 'w')
                        save_file.write(str(char.level) + ' (lvl)\n')
                        save_file.write(str(bgindex) + ' (bgindex)\n')
                        save_file.write(str(char.health) + ' (health)\n')
                        save_file.write(str(char.force) + ' (force)\n')
                        save_file.write(str(char.dmg) + ' (dmg)\n')
                        save_file.write(str(char.maxhealth) + ' (maxhealth)\n')
                        save_file.write(str(char.maxforce) + ' (maxhealth)\n')
                        for ability in char.abilities:
                            save_file.write(str(ability) + ' ')
                        save_file.write('(abilities)\n')
                        save_file.write(str(char.exp) + ' exp\n')
                        save_file.write(str(char.boltLvl) + ' boltlvl\n')
                        save_file.write(str(char.healLvl) + ' heallvl\n')
                        save_file.write(str(char.points) + ' skillpoints\n')
                        save_file.write(str(stageindex) + ' stage\n')
                        save_file.close()
                if event.key == pygame.K_m:
                    inMenu = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            posx = pos[0]
            posy = pos[1]
            if isCol2(posx, posy, 253, 314) and char.points > 0:
                char.healLvl += 1
                char.points -= 1
                char.updateSkills()
            elif isCol2(posx, posy, 255, 404) and char.points > 0 and 'ForceBolt' in char.abilities:
                char.boltLvl += 1
                char.points -= 1
                char.updateSkills()
            print(pos)

    draw_screen()

    if isBattle:
        battle(char, b_droid)
        draw_HUD()
    elif inMenu != True:
        keys = pygame.key.get_pressed()
        if isCol(char, b_droid):
            isBattle = True
            char.x = 100
            char.y = 200
            b_droid.x = 500
            b_droid.y = 200
        else:
            if keys[pygame.K_LEFT]:
                char.x -= char.speed
                char.isLeft = True
                char.isMove = True
                if charindex <= len(ana_run) - 1:
                    charindex += loopspeed
                else:
                    charindex = 0
            elif keys[pygame.K_RIGHT]:
                char.x += char.speed
                char.isLeft = False
                char.isMove = True
                if charindex <= len(ana_run) - 1:
                    charindex += loopspeed
                else:
                    charindex = 0
            else:
                char.isMove = False

    #Switching Rooms
    if bgindex != 0 and char.x < -10:
        bgindex -= 1
        char.x = 700
        if bgindex == 2:
            b_droid = enemy.Bdroid(200, 400, 100, 2)
            b_droid.x = 200
        else:
            b_droid.x = 500
        enemyCount = 0
        if bgindex == 3:
            b_droid = enemy.Bdroid(500, 400, 100, 2)
    elif bgindex == 0 and char.x < 10:
        char.x = 10

    if char.x > 850:
        if bgindex == 4:
            stages[stageindex] = False
            stageindex += 1
            stages[stageindex] = True
            bgindex = 0
        if bgindex == 3:
            b_droid = enemy.Sbdroid(1000, 400, 300, 1)
        char.x = 10
        bgindex += 1
        if bgindex == 2:
            b_droid.x = 200
        else:
            b_droid.x = 500
        enemyCount = 0

    if char.health <= 0:
        pygame.quit()

    pygame.display.update()






#New Var
charindex = 0
enemy1 = enemy.Bdroid(500, 200, 100, 2)
enemy2 = enemy.Bdroid(600, 100, 100, 2)
enemy3 = enemy.Bdroid(600, 300, 100, 2)
char.y = 450
troop = player.Trooper()
win = False
choose = False
choice = ''
isBolt = False

#Level 2 and updated code with improved functions
def draw_screen2():
    bg_image = pygame.transform.scale(dfactory[bgindex], (width, height))
    char_image = pygame.transform.scale(ana, (100, 100))
    if isBattle:
        if char.attack:
            char_image = pygame.transform.scale(ana_hit[int(charindex)], (100, 100))
        elif forceHeal:
            char_image = pygame.transform.scale(ana_heal[int(charindex)], (100, 100))
        elif forceBolt:
            char_image = pygame.transform.scale(ana_bolt[int(charindex)], (100, 100))
        elif win:
            char_image = pygame.transform.scale(ana_win1, (100, 100))
    elif char.isMove:
        char_image = pygame.transform.scale(ana_run[int(charindex)], (100, 100))

    if char.isLeft:
        char_image = pygame.transform.flip(char_image, True, False)


    char_image.set_colorkey((0,0,255))

    if isBattle:
        screen.fill((127, 127, 127))
        screen.blit(battle_1, (0, 400))
        if win:
            screen.blit(battle_done, (0, 400))
        elif inFmenu:
            if 'ForceBolt' in char.abilities:
                screen.blit(force_display2, (0, 400))
            else:
                screen.blit(force_display, (0, 400))
    else:
        screen.blit(bg_image, (0,0))
    screen.blit(char_image, (char.x, char.y))

    #General HUD for char
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 175, 60))
    pygame.draw.rect(screen, (211, 211, 211), (60, 10, 100, 10))
    pygame.draw.rect(screen, (211, 211, 211), (60, 25, 100, 10))
    pygame.draw.rect(screen, (211, 211, 211), (60, 40, 100, 10))

    pygame.draw.rect(screen, (255, 0, 0), (60, 10, char.health/(char.maxhealth/100), 10))
    pygame.draw.rect(screen, (0, 0, 255), (60, 25, char.force/(char.maxforce/100), 10))
    pygame.draw.rect(screen, (0, 255, 0), (60, 40, char.exp/(char.level*10), 10))

    level_display = font.render(str(char.level), True, (0,255,0))
    screen.blit(level_display, (5, 5))

    if inMenu:
        screen.fill((127, 127, 127))
        level_display = font.render('Level: ' + str(char.level), True, (0,0,0))
        exp_display = font.render('Exp: ' + str(char.exp) + '/' + str(char.level * 1000), True, (0, 0, 0))
        power_display = font.render('Power: ' + str(char.dmg), True, (0,0,0))
        health_display = font.render('Health: ' + str(char.health) + '/' + str(char.maxhealth), True, (0, 0, 0))
        force2_display = font.render('Force: ' + str(char.force) + '/' + str(char.maxforce), True, (0, 0, 0))
        skills_display = font.render('Skill Points: ' + str(char.points), True, (0,0,0))
        heal_display = font.render('Force Heal:', True, (0,0,0))
        heal_info = font2.render('Lvl: ' + str(char.healLvl) + ' Dmg: ' + str(char.healDmg) + ' Cost: ' + str(char.healCost), True, (0,0,0))
        bolt_display = font.render('Force Bolt:', True, (0, 0, 0))
        bolt_info = font2.render('Lvl: ' + str(char.boltLvl) + ' Dmg: ' + str(char.boltDmg) + ' Cost: ' + str(char.boltCost), True, (0,0,0))


        screen.blit(level_display, (10, 10))
        screen.blit(exp_display, (10, 50))
        screen.blit(power_display, (10, 90))
        screen.blit(health_display, (10, 130))
        screen.blit(force2_display, (10, 170))
        screen.blit(skills_display, (10, 250))
        screen.blit(heal_display, (10, 290))
        screen.blit(heal_info, (10, 330))

        plus.set_colorkey((255, 255, 255))

        if 'ForceBolt' in char.abilities:
            screen.blit(bolt_display, (10, 380))
            screen.blit(bolt_info, (10, 420))
            if char.points > 0:
                screen.blit(plus, (230, 380))

        if char.points > 0:
            screen.blit(plus, (230, 290))

def draw_HUD2():

    #Draw health bars
    pygame.draw.rect(screen, (255, 0, 0), (enemy1.x, enemy1.y - 10, 100, 10))
    pygame.draw.rect(screen, (0, 255, 0), (enemy1.x, enemy1.y - 10, enemy1.health/enemy1.maxhealth, 10))

    pygame.draw.rect(screen, (255, 0, 0), (enemy2.x, enemy2.y - 10, 100, 10))
    pygame.draw.rect(screen, (0, 255, 0), (enemy2.x, enemy2.y - 10, enemy2.health / enemy2.maxhealth, 10))

    pygame.draw.rect(screen, (255, 0, 0), (enemy3.x, enemy3.y - 10, 100, 10))
    pygame.draw.rect(screen, (0, 255, 0), (enemy3.x, enemy3.y - 10, enemy3.health / enemy3.maxhealth, 10))

    pygame.draw.rect(screen, (255, 0, 0), (troop.x, troop.y - 10, 100, 10))
    pygame.draw.rect(screen, (0, 255, 0), (troop.x, troop.y - 10, troop.health / troop.maxhealth, 10))

    #Draw arrow
    arrow.set_colorkey((255,255,255))
    if win == False:
        screen.blit(arrow, (arrowx, arrowy))

def draw_battle():
    #Enemy Draw
    enemy_image = pygame.transform.scale(enemy1.att_frames[int(enemy1.index)], (100, 100))
    enemy2_image = pygame.transform.scale(enemy2.att_frames[int(enemy2.index)], (100, 100))
    enemy3_image = pygame.transform.scale(enemy3.att_frames[int(enemy3.index)], (100, 100))

    #Enemy Death draw
    if enemy1.death:
        enemy_image = pygame.transform.scale(enemy1.death_frames[int(enemy1.index)], (100, 100))

    if enemy2.death:
        enemy2_image = pygame.transform.scale(enemy2.death_frames[int(enemy2.index)], (100, 100))

    if enemy3.death:
        enemy3_image = pygame.transform.scale(enemy3.death_frames[int(enemy3.index)], (100, 100))

    #Team Draw
    troop_image = pygame.transform.scale(ct_hit[int(troop.index)], (100, 100))

    #Blit
    enemy_image.set_colorkey((0, 0, 255))
    enemy2_image.set_colorkey((0,0,255))
    enemy3_image.set_colorkey((0,0,255))
    troop_image.set_colorkey((0,0,255))
    screen.blit(troop_image, (troop.x, troop.y))
    screen.blit(enemy_image, (enemy1.x, enemy1.y))
    screen.blit(enemy2_image, (enemy2.x, enemy2.y))
    screen.blit(enemy3_image, (enemy3.x, enemy3.y))

def battle2():
    global charindex
    global choice
    global win
    global forceBolt

    if char.attack:
        if charindex <= len(ana_hit) - 1:
            charindex += loopspeed
        else:
            if choice == 1:
                if enemy1.health > 0:
                    enemy1.health -= char.dmg
                elif enemy2.health > 0:
                    enemy2.health -= char.dmg
                elif enemy3.health > 0:
                    enemy3.health -= char.dmg
            elif choice == 2:
                if enemy2.health > 0:
                    enemy2.health -= char.dmg
                elif enemy1.health > 0:
                    enemy1.health -= char.dmg
                elif enemy3.health > 0:
                    enemy3.health -= char.dmg
            elif choice == 3:
                if enemy3.health > 0:
                    enemy3.health -= char.dmg
                elif enemy2.health > 0:
                    enemy2.health -= char.dmg
                elif enemy1.health > 0:
                    enemy1.health -= char.dmg
            char.attack = False
            char.x = 100
            char.y = 200
            troop.attack = True
    elif forceBolt:
        if charindex <= len(ana_bolt) - 1:
            charindex += loopspeed
        else:
            if choice == 1:
                if enemy1.health > 0:
                    enemy1.health -= char.boltDmg
                elif enemy2.health > 0:
                    enemy2.health -= char.boltDmg
                elif enemy3.health > 0:
                    enemy3.health -= char.boltDmg
            elif choice == 2:
                if enemy2.health > 0:
                    enemy2.health -= char.boltDmg
                elif enemy1.health > 0:
                    enemy1.health -= char.boltDmg
                elif enemy3.health > 0:
                    enemy3.health -= char.boltDmg
            elif choice == 3:
                if enemy3.health > 0:
                    enemy3.health -= char.boltDmg
                elif enemy2.health > 0:
                    enemy2.health -= char.boltDmg
                elif enemy1.health > 0:
                    enemy1.health -= char.boltDmg
            forceBolt = False
            char.x = 100
            char.y = 200
            troop.attack = True

    if troop.attack:
        if troop.index <= len(ct_hit) - 1:
            troop.index += loopspeed
            troop.x = 100
        else:
            laser_sound.play()
            troop.x = 50
            if choice == 1:
                if enemy1.health > 0:
                    enemy1.health -= troop.dmg
                elif enemy2.health > 0:
                    enemy2.health -= troop.dmg
                elif enemy3.health > 0:
                    enemy3.health -= troop.dmg
            elif choice == 2:
                if enemy2.health > 0:
                    enemy2.health -= troop.dmg
                elif enemy1.health > 0:
                    enemy1.health -= troop.dmg
                elif enemy3.health > 0:
                    enemy3.health -= troop.dmg
            elif choice == 3:
                if enemy3.health > 0:
                    enemy3.health -= troop.dmg
                elif enemy2.health > 0:
                    enemy2.health -= troop.dmg
                elif enemy1.health > 0:
                    enemy1.health -= troop.dmg
            troop.index = 0
            troop.attack = False
            if enemy1.death == False:
                enemy1.attack = True
            elif enemy2.death == False:
                enemy2.attack = True
            elif enemy3.death == False:
                enemy3.attack = True
            pygame.time.delay(300)

    enemy1.healthCheck()
    enemy2.healthCheck()
    enemy3.healthCheck()

    #Death animation of enemies
    if enemy1.death and enemy1.dead == False:
        if enemy1.index <= len(enemy1.death_frames) - 1:
            enemy1.index += loopspeed
        else:
            explode_sound.play()
            enemy1.index = 8
            enemy1.dead = True
            enemy1.attack = False
            if enemy2.dead == False:
                enemy2.attack = True
            elif enemy3.dead == False:
                enemy3.attack = True

    if enemy2.death and enemy2.dead == False:
        if enemy2.index <= len(enemy2.death_frames) - 1:
            enemy2.index += loopspeed
        else:
            explode_sound.play()
            enemy2.index = 8
            enemy2.dead = True
            enemy2.attack = False
            if enemy1.dead == False:
                enemy1.attack = True
            elif enemy3.dead == False:
                enemy3.attack = True

    if enemy3.death and enemy3.dead == False:
        if enemy3.index <= len(enemy3.death_frames) - 1:
            enemy3.index += loopspeed
        else:
            explode_sound.play()
            enemy3.index = 8
            enemy3.dead = True
            enemy3.attack = False
            if enemy2.dead == False:
                enemy2.attack = True
            elif enemy1.dead == False:
                enemy1.attack = True

    if enemy1.dead:
        enemy1.attack = False
    if enemy2.dead:
        enemy2.attack = False
    if enemy3.dead:
        enemy3.attack = False

    #Enemy attack
    if enemy1.attack and enemy1.death == False:
        if enemy1.index <= len(enemy1.att_frames) - 1:
            enemy1.index += loopspeed
            enemy1.x = 450
        else:
            laser_sound.play()
            enemy1.x = 500
            char.health -= enemy1.dmg
            enemy1.index = 0
            enemy1.attack = False
            enemy2.attack = True
            pygame.time.delay(300)

    if enemy2.attack and enemy2.death == False:
        if enemy2.index <= len(enemy2.att_frames) - 1:
            enemy2.index += loopspeed
            enemy2.x = 550
        else:
            laser_sound.play()
            enemy2.x = 600
            char.health -= enemy2.dmg
            enemy2.index = 0
            enemy2.attack = False
            enemy3.attack = True
            pygame.time.delay(300)

    if enemy3.attack and enemy3.death == False:
        if enemy3.index <= len(enemy3.att_frames) - 1:
            enemy3.index += loopspeed
            enemy3.x = 550
        else:
            laser_sound.play()
            enemy3.x = 600
            char.health -= enemy3.dmg
            enemy3.index = 0
            enemy3.attack = False
            pygame.time.delay(300)

    #Win condition
    if enemy1.dead and enemy2.dead and enemy3.dead:
        win = True

#Main Game
while stages[1]:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            #Battle key bindings
            if isBattle:
                if event.key == pygame.K_RIGHT and ('right' in current_arrow) != True:
                    if choose == False:
                        arrowx += 375
                        current_arrow[1] = 'right'
                elif event.key == pygame.K_LEFT and ('left' in current_arrow) != True:
                    if choose == False:
                        arrowx -= 375
                        current_arrow[1] = 'left'
                elif event.key == pygame.K_UP and ('up' in current_arrow) != True:
                    if choose == False:
                        arrowy -= 80
                        current_arrow[0] = 'up'
                elif event.key == pygame.K_DOWN and ('down' in current_arrow) != True:
                    if choose:
                        if arrowy == enemy3.y:
                            arrowx = enemy2.x - 50
                            arrowy = enemy2.y
                            choice = 2
                        elif arrowy == enemy2.y:
                            arrowx = enemy1.x - 50
                            arrowy = enemy1.y
                            choice = 1
                        elif arrowy == enemy1.y:
                            arrowx = enemy3.x - 50
                            arrowy = enemy3.y
                            choice = 3
                    else:
                        arrowy += 80
                        current_arrow[0] = 'down'
                elif event.key == pygame.K_BACKSPACE:
                    if inFmenu:
                        inFmenu = False
                    if choose:
                        choose = False
                        arrowx = 20
                        arrowy = 430
                        current_arrow = ['up', 'left']
                elif event.key == pygame.K_RETURN:
                    if char.attack or troop.attack or enemy1.attack or enemy2.attack or enemy3.attack:
                        print('True')
                    elif win:
                        win = False
                        isBattle = False
                        char.x = char.prevx
                        char.y = char.prevy
                        dice = 0
                        char.exp += enemy1.exp + enemy2.exp + enemy3.exp
                        charindex = 0
                        enemy1 = enemy.Bdroid(500, 200, 100, 2)
                        enemy2 = enemy.Bdroid(600, 100, 100, 2)
                        enemy3 = enemy.Bdroid(600, 300, 100, 2)
                    else:
                        if current_arrow == ['up', 'left'] and choose == False:
                            choose = True
                            arrowx = enemy1.x - 50
                            arrowy = enemy1.y
                            choice = 1
                        elif current_arrow == ['down', 'right']:
                            char.health -= 25
                            troop.health -= 25
                            isBattle = False
                            charindex = 0
                            enemy1 = enemy.Bdroid(500, 200, 100, 2)
                            enemy2 = enemy.Bdroid(600, 100, 100, 2)
                            enemy3 = enemy.Bdroid(600, 300, 100, 2)
                            char.x = char.prevx
                            char.y = char.prevy
                            dice = 0
                        elif current_arrow == ['up', 'right'] and choose == False:
                            if inFmenu:
                                if char.force >= char.boltCost and 'ForceBolt' in char.abilities:
                                    choose = True
                                    isBolt = True
                                    arrowx = enemy1.x - 50
                                    arrowy = enemy1.y
                                    choice = 1
                            else:
                                inFmenu = True
                        elif choose:
                            if isBolt:
                                bolt_sound.play()
                                char.force -= char.boltCost
                                forceBolt = True
                                isBolt = False
                            else:
                                saber_sound.play()
                                char.attack = True
                            arrowx = 20
                            arrowy = 430
                            current_arrow = ['up', 'left']
                            inFmenu = False
                            choose = False
                            char.x += 100
                            charindex = 0
            else:
                if event.key == pygame.K_s:
                    if inMenu:
                        save_file = open('Save.txt', 'w').close()
                        save_file = open('Save.txt', 'w')
                        save_file.write(str(char.level) + ' (lvl)\n')
                        save_file.write(str(bgindex) + ' (bgindex)\n')
                        save_file.write(str(char.health) + ' (health)\n')
                        save_file.write(str(char.force) + ' (force)\n')
                        save_file.write(str(char.dmg) + ' (dmg)\n')
                        save_file.write(str(char.maxhealth) + ' (maxhealth)\n')
                        save_file.write(str(char.maxforce) + ' (maxhealth)\n')
                        for ability in char.abilities:
                            save_file.write(str(ability) + ' ')
                        save_file.write('(abilities)\n')
                        save_file.write(str(char.exp) + ' exp\n')
                        save_file.write(str(char.boltLvl) + ' boltlvl\n')
                        save_file.write(str(char.healLvl) + ' heallvl\n')
                        save_file.write(str(char.points) + ' skillpoints\n')
                        save_file.write(str(stageindex) + ' stage\n')
                        save_file.write(str(troop.lvl) + ' trooplvl\n')
                        save_file.write(str(troop.health) + ' troophealth\n')
                        save_file.close()
                elif event.key == pygame.K_m:
                    inMenu = True
                elif event.key == pygame.K_BACKSPACE:
                    if inMenu:
                        inMenu = False

    draw_screen2()

    if isBattle:
        draw_battle()
        draw_HUD2()
        battle2()
    elif inMenu != True:
        keys = pygame.key.get_pressed()
        if dice == 100:
            char.prevx = char.x
            char.prevy = char.y
            char.isLeft = False
            isBattle = True
            char.x = 100
            char.y = 200
        else:
            if keys[pygame.K_LEFT]:
                dice = random.randint(0, 100)
                char.x -= char.speed
                char.isLeft = True
                char.isMove = True
                if charindex <= len(ana_run) - 1:
                    charindex += loopspeed
                else:
                    charindex = 0
            elif keys[pygame.K_RIGHT]:
                dice = random.randint(0, 100)
                char.x += char.speed
                char.isLeft = False
                char.isMove = True
                if charindex <= len(ana_run) - 1:
                    charindex += loopspeed
                else:
                    charindex = 0
            else:
                char.isMove = False

    #Boundary Check
    if char.x < -10:
        bgindex -= 1
        char.x = 700
    elif char.x > 820:
        bgindex += 1
        char.x = 10

    char.levelCheck()

    pygame.display.update()

pygame.quit()
