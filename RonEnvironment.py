import pygame
import time
import subprocess
import os
from Utils import *
import Settings



# -----------------------------------------------------------
# Project based on PDDL (AI)
# The Project is based on a planning for some tasks that the robot Ron
# has to compute
# (C) 2021 Vannoli Marco, Rome, Italy
# email vannoli.1860363@studenti.uniroma1.it
# -----------------------------------------------------------


"""
This file aims to Crate an Environment for The Ron's Tasks. Infact once the solution
form Graph Algorithm based on PDDL is computed, Then this file will 
render a scene in order to visualize Ron that compute he Task.
Thus, provide all Objects and Persons that are inside to the Task 
"""

def robot_environment(planning,robot_pos,object_pos,person_pos,has_object,targ):

    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    win = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Robot Ron Planning")

    loc_personalroom_x = 450
    loc_personalroom_y = 50

    loc_kitchen_x = 50
    loc_kitchen_y = 200

    loc_bathroom_x = 50
    loc_bathroom_y = 500

    loc_floor_x = 500
    loc_floor_y = 400

    loc_door_x = 500;
    loc_door_y = 700;

    loc_livingroom_x = 800
    loc_livingroom_y = 500

    loc_bedroom_x = 800
    loc_bedroom_y = 200





    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    bg = pygame.image.load('Image\\map_game.png')
    robot = pygame.image.load('Image\\robot.png')
    text_drop = myfont.render('Drop!', False, (255, 255, 255))
    text_onTv = myfont.render('On!', False, (255, 255, 255))

    text_open_garage = myfont.render('Open!', False, (255, 255, 255))
    text_close_garage = myfont.render('Close!', False, (255, 255, 255))

    text_pickup = myfont.render('Pickup!', False, (255, 255, 255))
    text_offTv = myfont.render('Off!', False, (255, 255, 255))
    text_cook = myfont.render('Cook Food!', False, (255, 255, 255))

    person = pygame.image.load('Image\\person.png')
    keys = pygame.image.load('Image\\keys.png')
    food = pygame.image.load('Image\\food.png')

    garage_open = pygame.image.load('Image\\garage_open.png')
    garage_close =  pygame.image.load('Image\\garage_close.png')

    pasta = pygame.image.load('Image\\pasta.png')

    sandwich = pygame.image.load('Image\\sandwich.png')

    hamburger = pygame.image.load('Image\\hamburger.png')

    controller = pygame.image.load('Image\\controller.png')
    tv_on = pygame.image.load('Image\\tv_on.png')
    tv_off = pygame.image.load('Image\\tv_off.png')
    delivery = pygame.image.load('Image\\delivery.png')

    flag_black = pygame.image.load('Image\\black_flag.png')
    flag_green = pygame.image.load('Image\\green_flag.png')

    print('PLAN SOLUTION: {} ->\n'.format(planning))
    win.blit(bg, (0, 0))


    def goFloor(char,shift):
        win.blit(char, (loc_floor_x-shift,loc_floor_y-shift))
        pygame.display.flip()
        time.sleep(1)

    def goDoor(char, shift):
        win.blit(char, (loc_door_x - shift, loc_door_y - shift))
        pygame.display.flip()
        time.sleep(1)

    def goLivingroom(char,shift):
        win.blit(char, (loc_livingroom_x-shift,loc_livingroom_y-shift))
        pygame.display.flip()
        time.sleep(1)

    def goBathroom(char,shift):
        win.blit(char, (loc_bathroom_x-shift,loc_bathroom_y-shift))
        pygame.display.flip()
        time.sleep(1)

    def goKitchen(char,shift):
        win.blit(char, (loc_kitchen_x-shift, loc_kitchen_y-shift))
        pygame.display.flip()
        time.sleep(1)

    def goBedroom(char,shift):
        win.blit(char, (loc_bedroom_x-shift, loc_bedroom_y-shift))
        pygame.display.flip()
        time.sleep(1)

    def goPersonalroom(char,shift):
        win.blit(char, (loc_personalroom_x-shift,loc_personalroom_y-shift))
        pygame.display.flip()
        time.sleep(1)

    def moveGarage(char,move_loc, shift=0):
        if (move_loc == 'Livingroom'):
            goLivingroom(char, shift)

        if (move_loc == 'Personalroom'):
            goPersonalroom(char, shift)

        if (move_loc == 'Floor'):
            goFloor(char, shift)

        if (move_loc == 'Bathroom'):
            goBathroom(char, shift)

        if (move_loc == 'Bedroom'):
            goBedroom(char, shift)

        if (move_loc == 'Kitchen'):
            goKitchen(char, shift)

        if (move_loc == 'Door'):
            win.blit(char, (loc_door_x + 40, loc_door_y - 40))
            pygame.display.flip()
            time.sleep(1)

    def move(char,move_loc,shift=0):
        if(move_loc == 'Livingroom'):
            goLivingroom(char,shift)

        if (move_loc == 'Personalroom'):
            goPersonalroom(char,shift)

        if (move_loc == 'Floor'):
            goFloor(char,shift)

        if (move_loc == 'Bathroom'):
            goBathroom(char,shift)

        if (move_loc == 'Bedroom'):
            goBedroom(char,shift)

        if (move_loc == 'Kitchen'):
            goKitchen(char,shift)

        if (move_loc == 'Door'):
            goDoor(char, shift)

    def pichup(loc,object,shift=0):
        if (loc == 'Livingroom'):
            goLivingroom(object,shift)
            win.blit(text_pickup, (loc_livingroom_x-shift,  loc_livingroom_y-shift-50))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Personalroom'):
            goPersonalroom(object,shift)
            win.blit(text_pickup,( loc_personalroom_x - shift, loc_personalroom_y - shift-50))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Floor'):
            goFloor(object,shift)
            win.blit(text_pickup, (loc_floor_x - shift, loc_floor_y - shift-50))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Bathroom'):
            goBathroom(object,shift)
            win.blit(text_pickup, (loc_bathroom_x - shift, loc_bathroom_y - shift-50))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Bedroom'):
            goBedroom(object,shift)
            win.blit(text_pickup, (loc_bedroom_x - shift, loc_bedroom_y - shift-50))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Kitchen'):
            goKitchen(object,shift)
            win.blit(text_pickup, (loc_kitchen_x - shift, loc_kitchen_y - shift-50))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Door'):
            goDoor(object, shift)
            win.blit(text_pickup, (loc_door_x - shift, loc_door_y - shift - 50))
            pygame.display.flip()
            time.sleep(1)

    def drop(loc,object,shift=0):
        if (loc == 'Livingroom'):
            goLivingroom(object,shift)
            win.blit(text_drop, (loc_livingroom_x - shift, loc_livingroom_y - shift-80))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Personalroom'):
            goPersonalroom(object,shift)
            win.blit(text_drop, (loc_personalroom_x - shift, loc_personalroom_y - shift-80))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Floor'):
            goFloor(object,shift)
            win.blit(text_drop, (loc_floor_x - shift, loc_floor_y - shift-80))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Bathroom'):
            goBathroom(object,shift)
            win.blit(text_drop, (loc_bathroom_x - shift, loc_bathroom_y - shift-80))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Bedroom'):
            goBedroom(object,shift)
            win.blit(text_drop, (loc_bedroom_x - shift, loc_bedroom_y - shift-80))
            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Kitchen'):
            goKitchen(object,shift)
            win.blit(text_drop, (loc_kitchen_x - shift, loc_kitchen_y - shift-80))

            pygame.display.flip()
            time.sleep(1)
        if (loc == 'Door'):
            goDoor(object, shift)
            win.blit(text_drop, (loc_door_x - shift, loc_door_y - shift - 80))

            pygame.display.flip()
            time.sleep(1)

    def onTv(shift=0):
            move(tv_on, tv_pos, 90)
            win.blit(text_onTv, (loc_livingroom_x - shift, loc_livingroom_y - shift-60))
            pygame.display.flip()
            time.sleep(1)

    def offTv(shift=0):
        move(tv_off, tv_pos, 90)
        win.blit(text_offTv, (loc_livingroom_x - shift, loc_livingroom_y - shift - 30))
        pygame.display.flip()
        time.sleep(1)

    def openGarage(shift=0):
            moveGarage(garage_open, garage_pos, 0)
            win.blit(text_open_garage, (loc_door_x - shift, loc_door_y- shift+10))
            pygame.display.flip()
            time.sleep(1)

    def closeGarage(shift=0):
        moveGarage(garage_close, garage_pos, 0)
        win.blit(text_close_garage, (loc_door_x - shift, loc_door_y- shift + 10))
        pygame.display.flip()
        time.sleep(1)

    def start_position_keys(robot_position,keys_position,person_position):
        move(robot, robot_position)
        move(keys, keys_position,30)
        move(person, person_position,-30)
        move(flag_black, person_position,50)
        print('START POSITIONS : \n')
        print(('Position Ron : {} \n').format(robot_position))
        print(('Position Keys : {} \n').format(keys_position))
        print(('Position You : {} \n').format(person_position))

    def start_position_open_close_garage(robot_position,keys_position,garage_position):
        move(robot, robot_position)
        move(keys, keys_position, 30)
        if (Settings.OpenGarage[0] == 'OpenGarage'):
            moveGarage(garage_close,garage_pos, 0)
        else:
            moveGarage(garage_open, garage_pos, 0)
        move(flag_black, garage_position, 50)
        print('START POSITIONS : \n')
        print(('Position Ron : {} \n').format(robot_position))
        print(('Position Keys : {} \n').format(keys_position))
        print(('Position Garage : {} \n').format(garage_position))

    def start_position_food(robot_position,food_position,person_position):
        move(robot, robot_position)
        move(food, food_position,30)
        move(person, person_position,-30)
        move(flag_black, person_position,50)
        if(has_object == False):
           move(delivery, food_position, 10)
        print('START POSITIONS : \n')
        print(('Position Ron : {} \n').format(robot_position))
        print(('Position Food Delivered : {} \n').format(food_position))
        print(('Position You : {} \n').format(person_position))

    def start_position_cook_food(robot_position,food_position,person_position,type_food):

        move(robot, robot_position)
        move(person, person_position, -30)
        move(flag_black, person_position, 50)
        if (has_object == False):
            move(delivery, food_position, 10)
        print('START POSITIONS : \n')
        print(('Position Ron : {} \n').format(robot_position))
        print(('Position of {}'.format(type_food) +' to cook : {} \n').format(food_position))
        print(('Position You : {} \n').format(person_position))


    def start_position_tv(robot_position,controller_position,tv_position):
        move(robot, robot_position)
        move(controller, controller_position,30)
        if(Settings.OnTv == 'OnTv'):
           move(tv_off, tv_position,90)
        else:
            move(tv_on, tv_position, 90)
        move(flag_black, tv_position,50)
        print('START POSITIONS : \n')
        print(('Position Ron : {} \n').format(robot_position))
        print(('Position Controller : {} \n').format(controller_position))
        print(('Position Tv : {} \n').format(tv_position))


    def plankeys(has_keys):
            has_key = has_keys
            print('ACTIONS PLAN : \n')
            for i in planning:
                if(i[0] == 'move'):
                    if(has_key):
                        move(robot,i[2])
                        move(keys, i[2],30)
                        print('Ron moves with keys from %s to %s \n' %(i[1],i[2]))
                    else:
                        move(robot, i[2])
                        print('Ron moves without keys from %s to %s \n' % (i[1], i[2]))
                if (i[0] == 'pickupkeys'):
                    pichup(i[2],object=keys,shift=20)
                    print('Ron pichups keys from {} \n'.format(i[2]))
                    has_key = True;
                if (i[0] == 'dropkeys'):
                    drop(i[2],object=keys,shift=20)
                    print('Ron drops keys from {} \n'.format(i[2]))
                    has_key = False;
            move(flag_green, person_pos, 50)
    def planopenclosegarage(has_keys):
        has_key = has_keys
        print('ACTIONS PLAN : \n')
        for i in planning:
            if (i[0] == 'move'):
                if (has_key):
                    move(robot, i[2])
                    move(keys, i[2], 30)
                    print('Ron moves with keys from %s to %s \n' % (i[1], i[2]))
                else:
                    move(robot, i[2])
                    print('Ron moves without keys from %s to %s \n' % (i[1], i[2]))
            if (i[0] == 'pickupkeys'):
                pichup(i[2], object=keys, shift=20)
                print('Ron pichups keys from {} \n'.format(i[2]))
                has_key = True;
            if (i[0] == 'opengarage'):
                openGarage(shift=10)
                print('Ron open garage with keys from {} \n'.format(i[2]))
                has_key = True;
            if (i[0] == 'closegarage'):
                closeGarage(shift=10)
                print('Ron close garage with from {} \n'.format(i[2]))
                has_key = True;
        move(flag_green, person_pos, 50)
    def planfood(has_food):
            has_food = has_food
            print('ACTIONS PLAN : \n')
            for i in planning:
                if(i[0] == 'move'):
                    if(has_food):
                        move(robot,i[2])
                        move(food, i[2],30)
                        print('Ron moves with Food from %s to %s \n' %(i[1],i[2]))
                    else:
                        move(robot, i[2])
                        print('Ron moves without Food from %s to %s \n' % (i[1], i[2]))
                if (i[0] == 'pickupfood'):
                    pichup(i[2], object=food,shift=20)
                    print('Ron pichups Food from {} \n'.format(i[2]))
                    has_food = True;
                if (i[0] == 'dropfood'):
                    drop(i[2], object=food)
                    print('Ron drops Food from {} \n'.format(i[2]))
                    has_food = False;
            move(flag_green, person_pos, 50)
    def cookFood(type_food,food_position):
        if(type_food == 'Pasta'):
            move(pasta, food_position, 30)
        elif(type_food == 'Sandwich'):
            move(sandwich, food_position, 30)
        elif(type_food == 'Hamburger'):
            move(hamburger, food_position, 30)

    def getFoodObjByType(type_food):
        if (type_food == 'Pasta'):
            obj = pasta;
        elif (type_food == 'Sandwich'):
            obj = sandwich;
        elif (type_food == 'Hamburger'):
            obj = hamburger;
        return obj;
    def plancookfood(type_food):
        has_food = False;

        print('ACTIONS PLAN : \n')
        for i in planning:
            if (i[0] == 'move'):
                if (has_food):
                    food_cook = getFoodObjByType(type_food)
                    move(robot, i[2])
                    move(food_cook, i[2], 30)
                    print('Ron moves with the {}'.format(type_food)+'   from %s to %s \n' % (i[1], i[2]))
                else:
                    move(robot, i[2])
                    print('Ron moves without the {}'.format(type_food)+'   from %s to %s \n' % (i[1], i[2]))
            if (i[0] == 'pickupfood'):
                food_cook = getFoodObjByType(type_food)
                pichup(i[2], object=food_cook,shift=20)
                print('Ron pichups the {}'.format(type_food)+'  from {} \n'.format(i[2]))
                has_food = True;
            if (i[0] == 'dropfood'):
                food_cook = getFoodObjByType(type_food)
                drop(i[2], object=food_cook,shift=20)
                print('Ron drops the {}'.format(type_food)+'  from {} \n'.format(i[2]))
                has_food = False;
            if (i[0] == 'cookfood'):
                win.blit(text_cook, (loc_kitchen_x + 40, loc_kitchen_y + 40))
                cookFood(type_food,i[2]);
                print('Ron cook the {}'.format(type_food)+' from {} \n'.format(i[2]))
                has_food = False;
        move(flag_green, person_pos, 50)

    def plantv(has_controller):
            has_controller = has_controller
            print('ACTIONS PLAN : \n')
            for i in planning:
                if(i[0] == 'move'):
                    if(has_controller):
                        move(robot,i[2])
                        move(controller, i[2],30)
                        print('Ron moves with controller from %s to %s \n' %(i[1],i[2]))
                    else:
                        move(robot, i[2])
                        print('Ron moves without controller from %s to %s \n' % (i[1], i[2]))
                if (i[0] == 'pickupcontroller'):
                    pichup(i[2],object=controller,shift=20)
                    print('Ron pichups controller from {} \n'.format(i[2]))
                    has_controller = True;
                if (i[0] == 'dropcontroller'):
                    drop(i[2],object=controller)
                    print('Ron drops controller from {} \n'.format(i[2]))
                    has_controller = True;
                if (i[0] == 'ontv'):
                    onTv(shift=10)
                    print('Ron on Tv ')
                    has_controller = True;
                if (i[0] == 'offtv'):
                    offTv(shift=11)
                    print('Ron off Tv ')
                    has_controller = True;
            move(flag_green, person_pos, 50)

    run = True

    while run:
        if(targ == 'Bring to me keys'):
           start_position_keys(robot_pos, object_pos, person_pos)
           plankeys(has_object)
           pygame.quit()

           ModifyDatabaseActions(Settings.ActualActions)
           ModifyDatabaseStorage(Settings.Name[0])
           ModifyDatabaseActionsTxt(Settings.ActualActions)
           ModifyDatabaseAllActionsAvailable(Settings.AllActions)


           subprocess.run('python MainRonRobot.py')
        if(targ == 'Bring to me food delivered'):
           start_position_food(robot_pos, object_pos, person_pos)
           planfood(has_object)
           pygame.quit()

           ModifyDatabaseStorage(Settings.Name[0])
           ModifyDatabaseActions(Settings.ActualActions)
           ModifyDatabaseAllActionsAvailable(Settings.AllActions)
           ModifyDatabaseActionsTxt(Settings.ActualActions)

           subprocess.run('python MainRonRobot.py')

        if (targ == 'On/Off Tv'):
            tv_pos = person_pos;
            start_position_tv(robot_pos, object_pos, tv_pos)
            plantv(has_object)
            pygame.quit()

            ModifyDatabaseStorage(Settings.Name[0])
            ModifyDatabaseActions(Settings.ActualActions)
            ModifyDatabaseAllActionsAvailable(Settings.AllActions)
            ModifyDatabaseActionsTxt(Settings.ActualActions)

            subprocess.run('python MainRonRobot.py')
        if(targ == 'Cook me something'):
            type_food = has_object;
            start_position_cook_food(robot_pos, object_pos, person_pos,type_food)
            plancookfood(has_object)
            pygame.quit()

            ModifyDatabaseStorage(Settings.Name[0])
            ModifyDatabaseActions(Settings.ActualActions)
            ModifyDatabaseAllActionsAvailable(Settings.AllActions)
            ModifyDatabaseActionsTxt(Settings.ActualActions)

            subprocess.run('python MainRonRobot.py')

        if (targ == 'Open/Close Garage'):
            garage_pos = person_pos;
            start_position_open_close_garage(robot_pos, object_pos, garage_pos)
            planopenclosegarage(has_object)
            pygame.quit()

            ModifyDatabaseStorage(Settings.Name[0])
            ModifyDatabaseActions(Settings.ActualActions)
            ModifyDatabaseAllActionsAvailable(Settings.AllActions)
            ModifyDatabaseActionsTxt(Settings.ActualActions)

            subprocess.run('python MainRonRobot.py')


