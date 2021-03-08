import pickle
import  Settings


# -----------------------------------------------------------
# Project based on PDDL (AI)
# The Project is based on a planning for some tasks that the robot Ron
# has to compute
# (C) 2021 Vannoli Marco, Rome, Italy
# email vannoli.1860363@studenti.uniroma1.it
# -----------------------------------------------------------


"""
This file show all methods that are important to create particular message
whenever is necessary. For example, the message that show the Start Positions
and all that is necessary in order to describe all Tasks.
There are also other methods that we need in order to Save or Delete 
the Data in Database. The Database is a simple files pickle/txt that 
allow us to save data that will be used in future by user. 
"""


def start_position_message_keys(robot_position, position_object, person_position):
    message = ""
    message += 'Position Ron : %s \n' % (robot_position)
    message += 'Position Keys : %s \n'% (position_object)
    message += 'Position You : %s \n'% (person_position)

    return message

def start_position_message_food(robot_position, position_object, person_position):
    message = ""
    message += 'Position Ron : %s \n' % (robot_position)
    message += 'Position Food : %s \n'% (position_object)
    message += 'Position You : %s \n'% (person_position)

    return message

def start_position_message_cook_food(robot_position, position_object, person_position,type_food):
    message = ""
    message += 'Position Ron : %s \n' % (robot_position)
    message += 'Position Food : %s \n'% (position_object)
    message += 'Position You : %s \n'% (person_position)
    message += 'Food : %s \n' % (type_food)

    return message

def start_position_message_open_close_garage(robot_position, position_object, person_position):
    message = ""
    message += 'Position Ron : %s \n' % (robot_position)
    message += 'Position Keys : %s \n'% (position_object)
    message += 'Position Of Garage : %s \n'% (person_position)

    return message

def start_position_message_tv(robot_position, position_object, position_tv):
    message = ""
    message += 'Position Ron : %s \n' % (robot_position)
    message += 'Position Controller : %s \n'% (position_object)
    message += 'Position Tv : %s \n'% (position_tv)

    return message
def planning_message_keys(has_keys,planning):
    has_key = has_keys
    message = ""
    for i in planning:
        if (i[0] == 'move'):
            if (has_key):
                message += 'Ron moves with keys from %s to %s\n' % (i[1], i[2])
            else:
                message += 'Ron moves without keys from %s to %s\n' % (i[1], i[2])
        if (i[0] == 'pickupkeys'):
            message += 'Ron pichups keys from {}\n'.format(i[2])
            has_key = True;
        if (i[0] == 'dropkeys'):
            message += 'Ron drops keys from {}\n'.format(i[2])
            has_key = False;
    return message

def planning_message_open_close_garage(has_keys,planning):
    has_key = has_keys
    message = ""
    for i in planning:
        if (i[0] == 'move'):
            if (has_key):
                message += 'Ron moves with keys from %s to %s\n' % (i[1], i[2])
            else:
                message += 'Ron moves without keys from %s to %s\n' % (i[1], i[2])
        if (i[0] == 'pickupkeys'):
            message += 'Ron pichups keys from {}\n'.format(i[2])
            has_key = True;
        if (i[0] == 'opengarage'):
            message += 'Ron open garage with keys from {}\n'.format(i[2])
            has_key = True;
        if (i[0] == 'closegarage'):
            message += 'Ron close garage with keys from {}\n'.format(i[2])
            has_key = True;
    return message


def planning_message_food(has_food,planning):
    has_food = has_food
    message = ""
    for i in planning:
        if (i[0] == 'move'):
            if (has_food):
                message += 'Ron moves with Food from %s to %s\n' % (i[1], i[2])
            else:
                message += 'Ron moves without Food from %s to %s\n' % (i[1], i[2])
        if (i[0] == 'pickupfood'):
            message += 'Ron pichups Food from {}\n'.format(i[2])
            has_food = True;
        if (i[0] == 'dropfood'):
            message += 'Ron drops Food from {}\n'.format(i[2])
            has_food = False;
    return message

def planning_message_cook_food(type_food,planning):
    has_food = False;
    message = ""
    for i in planning:
        if (i[0] == 'move'):
            if (has_food):
                message += 'Ron moves with Food from %s to %s\n' % (i[1], i[2])
            else:
                message += 'Ron moves without Food from %s to %s\n' % (i[1], i[2])
        if (i[0] == 'pickupfood'):
            message += 'Ron pichups Food from {}\n'.format(i[2])
            has_food = True;
        if (i[0] == 'dropfood'):
            message += 'Ron drops Food from {}\n'.format(i[2])
            has_food = False;
        if (i[0] == 'cookfood'):
            message += 'Ron cook the {}'.format(type_food) + ' from {}\n'.format(i[2])
            has_food = False;
    return message

def planning_message_tv(has_controller,planning):
    has_controller = has_controller
    message = ""
    for i in planning:
        if (i[0] == 'move'):
            if (has_controller):
                message += 'Ron moves with Controller from %s to %s\n' % (i[1], i[2])
            else:
                message += 'Ron moves without Controller from %s to %s\n' % (i[1], i[2])
        if (i[0] == 'pickupcontroller'):
            message += 'Ron pichups Controller from {}\n'.format(i[2])
            has_controller = True;
        if (i[0] == 'dropcontroller'):
            message += 'Ron drops Controller from {}\n'.format(i[2])
            has_controller = False;
        if (i[0] == 'ontv'):
            message += 'Ron on Tv ';
            has_controller = True;
        if (i[0] == 'offtv'):
            message += 'Ron on Off ';
            has_controller = False;
    return message

def ModifyDatabaseActions(actions):
    with open('StorageData\\actions.pkl', 'wb') as file:
        pickle.dump(actions, file)

def ModifyDatabaseAllActionsAvailable(actions):
    with open('StorageData\\actions_available.pkl', 'wb') as file:
        pickle.dump(actions, file)

def SetAllActionsAvailableFromDB():
    try:
       with open('StorageData\\actions_available.pkl', 'rb') as file:
            list = pickle.load(file)
            if(list != []):
                 Settings.AllActions = list;
    except:
        None

def SetAllActionsFromDB():
    try:
       with open('StorageData\\actions.pkl', 'rb') as file:
            list = pickle.load(file)
            if(list != []):
                 Settings.ActualActions = list;
    except:
        None
def ModifyDatabaseActionsTxt(actions):
    with open('StorageData\\actions_storage.txt', 'w') as file:
        for item in actions:
            file.write("%s\n" % item)

def ModifyDatabaseStorage(name):
    with open('StorageData\\storage.txt', 'w') as file:
        file.write(name+ ' 1')
def ClearDatabaseStorage():
        with open('StorageData\\storage.txt', 'w') as file:
            file.write('')
def ReadDatabaseStorage():
    with open('StorageData\\storage.txt', 'r') as file:
        name = file.read()
        return name

def ClearDatabaseActions():
    with open('StorageData\\actions.pkl', 'wb') as file:
        pickle.dump([], file)
    with open('StorageData\\actions_available.pkl', 'wb') as file:
        pickle.dump([], file)

