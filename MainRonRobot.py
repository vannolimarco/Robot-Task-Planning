from DefineActionsPlan import define_actions_robot
from RonEnvironment import robot_environment
from Gui import Window, PopupCancel,Popup,ProgressWinodw,WindowTask,ViewMapPopup
from Utils import *
import subprocess
import random
import  Settings
from RonTasks import RonTaskKeys, RonTaskFood, RonTaskOnOffTv, RonTaskCookFood, RonTaskOpenCloseGarage
import PySimpleGUI as sg


# Robot delivery problem
robot_gui_title = "Ron Robot GUI"
robot_gui_aborted = "Ron GUI aborted"

# -----------------------------------------------------------
# Project based on PDDL (AI)
# The Project is based on a planning for some tasks that the robot Ron
# has to compute
# (C) 2021 Vannoli Marco, Rome, Italy
# email vannoli.1860363@studenti.uniroma1.it
# -----------------------------------------------------------


"""
This methods represent All the task that Ron can do. This file
is the Main file to run Ron robot. This kind of Project is an Interface Gui to 
select all task that Ron can do it.
"""

# MainTaskKeys : task of Keys
#
# Parameters:
# -
# task : the type of task
# name : the name selected at beginning

def MainTaskKeys(name,task):
    if(Settings.PositionRon == []):
         Settings.ModifyName(name[0])
         list_rooms = ['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor']
         event, position_start = Window(robot_gui_title, 'Hi %s , in which room i am ?' % (name), 'LB', list_rooms,True)
         if event == 'Ok' or event == 'Read From Sensor':
              if (event != 'Read From Sensor'):
                 Settings.SetPositionRon(position_start['LB'][0])
              else:
                 Settings.SetPositionRon(random.choice(list_rooms))
              if(Settings.HasKeys == [] and Settings.PositionKeys == [] and Settings.PositionPerson == []):
                solution, goal_position, where_key, has_keys = RonTaskKeys(Settings.PositionRon[0])
                actions = define_actions_robot(solution)
                Settings.SetActualSolution(solution)
                if (Settings.ActualSolution != [[]]):
                        start_pos_mess = start_position_message_keys(robot_position=Settings.PositionRon[0], position_object = Settings.PositionKeys[0],
                                                                     person_position= Settings.PositionPerson[0])
                        plan_mess = planning_message_keys(has_keys=has_keys, planning=actions)
                        Popup('Start Position : ', start_pos_mess)
                        Popup('Solution : ', plan_mess)
                        robot_environment(actions, Settings.PositionRon[0], where_key, goal_position, has_keys, targ=task)
                else:
                    event, sol = Window(robot_gui_title,
                                        'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-PickupKeys\n-DropKeys.\nYou can choose one of these actions\nP.s You can Add also an action\nthat will be useful after for other task.'
                                        , list=Settings.AllActions, key="ADD_DEL_ACT")

                    if event == 'Ok':
                        Settings.AddAction(sol['ADD_DEL_ACT'][0])
                        Settings.DropAction((sol['ADD_DEL_ACT'][0]).name)
                        ModifyDatabaseActions(Settings.ActualActions)
                        ModifyDatabaseAllActionsAvailable(Settings.AllActions)
                        MainTaskKeys(name,task)
                    else:
                        PopupCancel(robot_gui_aborted)

         else:
            PopupCancel(robot_gui_aborted)
            Settings.ClearActualSolution();
    else:
      solution, goal_position, where_key, has_keys = RonTaskKeys(Settings.PositionRon[0])
      Settings.SetActualSolution(solution)
      if (Settings.ActualSolution != [[]]):
          if (Settings.HasKeys[0] == 'no'):
              Has_key = False;
          else:
              Has_key = True;
          actions = define_actions_robot(Settings.ActualSolution[0])

          start_pos_mess = start_position_message_keys(robot_position=Settings.PositionRon[0],
                                                       position_object=Settings.PositionKeys[0],
                                                       person_position=Settings.PositionPerson[0])
          plan_mess = planning_message_keys(has_keys=Has_key, planning=actions)

          Popup('Start Position : ', start_pos_mess)
          Popup('Solution : ', plan_mess)
          robot_environment(actions, Settings.PositionRon[0], Settings.PositionKeys[0],
                            Settings.PositionPerson[0], Has_key, targ=task)
      else:
          event, sol = Window(robot_gui_title,
                              'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-PickupKeys\n-DropKeys.\nYou can choose one of these actions\nP.s You can Add also an action\nthat will be useful after for other task.'
                              , list=Settings.AllActions, key="ADD_DEL_ACT")

          if event == 'Ok':
              Settings.AddAction(sol['ADD_DEL_ACT'][0])
              Settings.DropAction(sol['ADD_DEL_ACT'][0].name)
              ModifyDatabaseActions(Settings.ActualActions)
              ModifyDatabaseAllActionsAvailable(Settings.AllActions)
              MainTaskKeys(name,task)
          else:
              PopupCancel(robot_gui_aborted)
              Settings.ClearActualSolution();


# MainTaskKeys : task of Open Close Garage
#
# Parameters:
# -
# task : the type of task
# name : the name selected at beginning

def MainTaskOpenCloseGarage(name,task):
    if(Settings.PositionRon == []):
         Settings.ModifyName(name[0])
         event, taskOpenClose = Window(robot_gui_title, '%s , I have to open or close the Garage?' % (name), 'OCG',
                              ['OpenGarage', 'CloseGarage'])
         Settings.SetOpenGarage(taskOpenClose['OCG'][0])
         if event == 'Ok':
             taskOpenClose = taskOpenClose['OCG'][0]
             list_rooms = ['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor', 'Door']
             event, position_start = Window(robot_gui_title, 'Hi %s , in which room i am ?' % (name), 'LB', list_rooms,True)
             if event == 'Ok' or event == 'Read From Sensor':
                  if (event != 'Read From Sensor'):
                     Settings.SetPositionRon(position_start['LB'][0])
                  else:
                     Settings.SetPositionRon(random.choice(list_rooms))
                  if(Settings.HasKeys == [] and Settings.PositionKeys == []):
                    solution, goal_position, where_key, has_keys = RonTaskOpenCloseGarage(Settings.PositionRon[0],taskOpenCloseOff=taskOpenClose)
                    actions = define_actions_robot(solution)
                    Settings.SetActualSolution(solution)
                    if (Settings.ActualSolution != [[]]):
                            start_pos_mess = start_position_message_open_close_garage(robot_position=Settings.PositionRon[0], position_object = Settings.PositionKeys[0],
                                                                         person_position= Settings.PositionGarage[0])
                            plan_mess = planning_message_open_close_garage(has_keys=has_keys, planning=actions)
                            Popup('Start Position : ', start_pos_mess)
                            Popup('Solution : ', plan_mess)
                            robot_environment(actions, Settings.PositionRon[0], where_key, goal_position, has_keys, targ=task)
                    else:
                        event, sol = Window(robot_gui_title,
                                            'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-PickupKeys\n-OpenGarage / CloseGarage\n.\nYou can choose one of these actions\nP.s You can Add also an action\nthat will be useful after for other task.'
                                            , list=Settings.AllActions, key="ADD_DEL_ACT")

                        if event == 'Ok':
                            Settings.AddAction(sol['ADD_DEL_ACT'][0])
                            Settings.DropAction((sol['ADD_DEL_ACT'][0]).name)
                            ModifyDatabaseActions(Settings.ActualActions)
                            ModifyDatabaseAllActionsAvailable(Settings.AllActions)
                            MainTaskOpenCloseGarage(name,task)
                        else:
                            PopupCancel(robot_gui_aborted)

             else:
                PopupCancel(robot_gui_aborted)
                Settings.ClearActualSolution();
         else:
            PopupCancel(robot_gui_aborted)
            Settings.ClearActualSolution();
    else:
      taskOpenClose = Settings.OpenGarage[0]
      solution, goal_position, where_key, has_keys = RonTaskOpenCloseGarage(Settings.PositionRon[0],taskOpenCloseOff=taskOpenClose)
      Settings.SetActualSolution(solution)
      if (Settings.ActualSolution != [[]]):
          if (Settings.HasKeys[0] == 'no'):
              Has_key = False;
          else:
              Has_key = True;
          actions = define_actions_robot(Settings.ActualSolution[0])

          start_pos_mess = start_position_message_open_close_garage(robot_position=Settings.PositionRon[0],
                                                       position_object=Settings.PositionKeys[0],
                                                       person_position=Settings.PositionGarage[0])
          plan_mess = planning_message_open_close_garage(has_keys=Has_key, planning=actions)

          Popup('Start Position : ', start_pos_mess)
          Popup('Solution : ', plan_mess)
          robot_environment(actions, Settings.PositionRon[0], Settings.PositionKeys[0],
                            Settings.PositionGarage[0], Has_key, targ=task)
      else:
          event, sol = Window(robot_gui_title,
                              'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-PickupKeys\n-OpenGarage / CloseGarage.\nYou can choose one of these actions\nP.s You can Add also an action\nthat will be useful after for other task.'
                              , list=Settings.AllActions, key="ADD_DEL_ACT")

          if event == 'Ok':
              Settings.AddAction(sol['ADD_DEL_ACT'][0])
              Settings.DropAction(sol['ADD_DEL_ACT'][0].name)
              ModifyDatabaseActions(Settings.ActualActions)
              ModifyDatabaseAllActionsAvailable(Settings.AllActions)
              MainTaskOpenCloseGarage(name,task)
          else:
              PopupCancel(robot_gui_aborted)
              Settings.ClearActualSolution();

# MainTaskCook : task of Cook something for Me
#
# Parameters:
# -
# task : the type of task
# name : the name selected at beginning


def MainTaskCook(name,task):
    if(Settings.PositionRon == []):
         Settings.ModifyName(name[0])
         list_rooms =  ['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor']
         event, position_start = Window(robot_gui_title, 'Hi %s , in which room i am ?' % (name), 'LB',list_rooms,True)
         if event == 'Ok' or event == 'Read From Sensor':
              if(event != 'Read From Sensor'):
                Settings.SetPositionRon(position_start['LB'][0])
              else:
                 Settings.SetPositionRon(random.choice(list_rooms))
              if(Settings.PositionPerson == []):
                solution, goal_position, where_food, type_food = RonTaskCookFood(Settings.PositionRon[0])
                actions = define_actions_robot(solution)
                Settings.SetActualSolution(solution)
                if (Settings.ActualSolution != [[]]):
                        start_pos_mess = start_position_message_cook_food(robot_position=Settings.PositionRon[0],
                                                                          position_object = where_food,
                                                                          person_position= goal_position, type_food=type_food)
                        plan_mess = planning_message_cook_food(type_food=type_food, planning=actions)
                        Popup('Start Position : ', start_pos_mess)
                        Popup('Solution : ', plan_mess)
                        robot_environment(actions, Settings.PositionRon[0], where_food, goal_position, type_food, targ=task)
                else:
                    event, sol = Window(robot_gui_title,
                                        'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-PickupFood\n-DropFood\n-CookFood.\nYou can choose one of these actions :\nP.s You can Add also an action\nthat will be useful after for other task.'
                                        , list=Settings.AllActions, key="ADD_DEL_ACT")

                    if event == 'Ok':
                        Settings.AddAction(sol['ADD_DEL_ACT'][0])
                        Settings.DropAction((sol['ADD_DEL_ACT'][0]).name)
                        ModifyDatabaseActions(Settings.ActualActions)
                        ModifyDatabaseAllActionsAvailable(Settings.AllActions)
                        MainTaskCook(name,task)
                    else:
                        PopupCancel(robot_gui_aborted)
                        #ClearDatabaseActions()

         else:
            PopupCancel(robot_gui_aborted)
            #ClearDatabaseActions()
            Settings.ClearActualSolution();
    else:
      solution, goal_position, where_food, type_food = RonTaskCookFood(Settings.PositionRon[0])
      Settings.SetActualSolution(solution)
      if (Settings.ActualSolution != [[]]):
          actions = define_actions_robot(Settings.ActualSolution[0])

          start_pos_mess = start_position_message_cook_food(robot_position=Settings.PositionRon[0],
                                                            position_object=Settings.PositionFoodCooking[0],
                                                            person_position=Settings.PositionPerson[0],
                                                            type_food=type_food)
          plan_mess = planning_message_cook_food(type_food=type_food, planning=actions)
          Popup('Start Position : ', start_pos_mess)
          Popup('Solution : ', plan_mess)
          robot_environment(actions, Settings.PositionRon[0], Settings.PositionFood[0],
                            Settings.PositionPerson[0], type_food, targ=task)
      else:
          event, sol = Window(robot_gui_title,
                              'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-PickupFood\n-DropFood\n-CookFood. \nYou can choose one of these actions :\nP.s You can Add also an action\nthat will be useful after for other task.'
                              , list=Settings.AllActions, key="ADD_DEL_ACT")

          if event == 'Ok':
              Settings.AddAction(sol['ADD_DEL_ACT'][0])
              Settings.DropAction(sol['ADD_DEL_ACT'][0].name)
              ModifyDatabaseActions(Settings.ActualActions)
              ModifyDatabaseAllActionsAvailable(Settings.AllActions)
              MainTaskCook(name,task)
          else:
              PopupCancel(robot_gui_aborted)
              #ClearDatabaseActions()
              Settings.ClearActualSolution();


# MainTaskFood : task of take the food delivered for Me
#
# Parameters:
# -
# task : the type of task
# name : the name selected at beginning


def MainTaskFood(name,task):
    if(Settings.PositionRon == []):
         Settings.ModifyName(name[0])
         list_rooms = ['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor','Door']
         event, position_start = Window(robot_gui_title, 'Hi %s , in which room i am ?' % (name), 'LB', list_rooms,True)
         if event == 'Ok' or event == 'Read From Sensor':
              if (event != 'Read From Sensor'):
                 Settings.SetPositionRon(position_start['LB'][0])
              else:
                 Settings.SetPositionRon(random.choice(list_rooms))
              if(Settings.HasKeys == [] and Settings.PositionPerson == []):
                solution, goal_position, where_food, has_food = RonTaskFood(Settings.PositionRon[0], Settings.PositionFood[0])
                actions = define_actions_robot(solution)
                Settings.SetActualSolution(solution)
                if (Settings.ActualSolution != [[]]):
                        start_pos_mess = start_position_message_food(robot_position=Settings.PositionRon[0], position_object= where_food,
                                                                     person_position= Settings.PositionPerson[0])
                        plan_mess = planning_message_food(has_food =has_food, planning=actions)
                        Popup('Start Position : ', start_pos_mess)
                        Popup('Solution : ', plan_mess)
                        robot_environment(actions, Settings.PositionRon[0], where_food, goal_position, has_food, targ=task)
                else:
                    event, sol = Window(robot_gui_title,
                                        'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-PickupFood\n-DropFood. \nYou can choose one of these actions :\nP.s You can Add also an action\nthat will be useful after for other task.'
                                        , list=Settings.AllActions, key="ADD_DEL_ACT")

                    if event == 'Ok':
                        Settings.AddAction(sol['ADD_DEL_ACT'][0])
                        Settings.DropAction((sol['ADD_DEL_ACT'][0]).name)
                        ModifyDatabaseActions(Settings.ActualActions)
                        ModifyDatabaseAllActionsAvailable(Settings.AllActions)
                        MainTaskFood(name,task)
                    else:
                        PopupCancel(robot_gui_aborted)

         else:
            PopupCancel(robot_gui_aborted)
    else:
      solution, goal_position, where_food, has_keys = RonTaskFood(Settings.PositionRon[0], Settings.PositionFood[0])
      Settings.SetActualSolution(solution)
      if (Settings.ActualSolution != [[]]):
          if (Settings.HasFood[0] == 'no'):
              Has_food = False;
          else:
              Has_food = True;
          actions = define_actions_robot(Settings.ActualSolution[0])

          start_pos_mess = start_position_message_food(robot_position=Settings.PositionRon[0],
                                                       position_object=where_food,
                                                       person_position=Settings.PositionPerson[0])
          plan_mess = planning_message_food(has_food=Has_food, planning=actions)

          Popup('Start Position : ', start_pos_mess)
          Popup('Solution : ', plan_mess)
          robot_environment(actions, Settings.PositionRon[0], where_food, goal_position, Has_food, task)
      else:
          event, sol = Window(robot_gui_title,
                              'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-PickupFood\n-DropFood. \nYou can choose one of these actions :\nP.s You can Add also an action\nthat will be useful after for other task.'
                              , list=Settings.AllActions, key="ADD_DEL_ACT")

          if event == 'Ok':
              Settings.AddAction(sol['ADD_DEL_ACT'][0])
              Settings.DropAction((sol['ADD_DEL_ACT'][0]).name)
              ModifyDatabaseActions(Settings.ActualActions)
              ModifyDatabaseAllActionsAvailable(Settings.AllActions)
              MainTaskFood(name,task)
          else:
              PopupCancel(robot_gui_aborted)
              #ClearDatabaseActions()

# MainTaskOnOffTV : task of On/Off Tv in Livingroom
#
# Parameters:
# -
# task : the type of task
# name : the name selected at beginning

def MainTaskOnOffTV(name,task):
    if(Settings.PositionRon == []  and Settings.PositionController == []):
        Settings.ModifyName(name[0])
        event, onTv = Window(robot_gui_title, '%s , I have to on or off the TV?' % (name), 'OTV',
                                       ['OnTv', 'OffTv'])
        if event == 'Ok':
             Settings.OnTv = onTv['OTV'][0];
             OnOrOffTv = Settings.OnTv;
             list_rooms = ['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor']
             event, position_start = Window(robot_gui_title, 'Hi %s , in which room i am ?' % (name), 'LB', list_rooms,True)
             if event == 'Ok' or event == 'Read From Sensor':
                  if (event != 'Read From Sensor'):
                     Settings.SetPositionRon(position_start['LB'][0])
                  else:
                     Settings.SetPositionRon(random.choice(list_rooms))
                  if(Settings.HasController == []):
                    solution, goal_position, where_controller, has_controller = RonTaskOnOffTv(Settings.PositionRon[0], OnOrOffTv)
                    actions = define_actions_robot(solution)
                    Settings.SetActualSolution(solution)
                    if (Settings.ActualSolution != [[]]):
                            start_pos_mess = start_position_message_tv(robot_position=Settings.PositionRon[0], position_object= where_controller,
                                                                       position_tv= Settings.PositionTv[0])
                            plan_mess = planning_message_tv(has_controller =has_controller, planning=actions)
                            Popup('Start Position : ', start_pos_mess)
                            Popup('Solution : ', plan_mess)
                            robot_environment(actions, Settings.PositionRon[0], where_controller, goal_position, has_controller, targ=task)
                    else:
                        event, sol = Window(robot_gui_title,
                                            'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-OnTv / OffTv\n-PickupController. \nYou can choose one of these actions :\nP.s You can Add also an action\nthat will be useful after for other task.'
                                            , list=Settings.AllActions, key="ADD_DEL_ACT")

                        if event == 'Ok':
                            Settings.AddAction(sol['ADD_DEL_ACT'][0])
                            Settings.DropAction((sol['ADD_DEL_ACT'][0]).name)
                            ModifyDatabaseActions(Settings.ActualActions)
                            ModifyDatabaseAllActionsAvailable(Settings.AllActions)
                            MainTaskOnOffTV(name,task)
                        else:
                            PopupCancel(robot_gui_aborted)


             else:
                PopupCancel(robot_gui_aborted)

        else:
            PopupCancel(robot_gui_aborted)
    else:
          OnOrOffTv =  Settings.OnTv;
          solution, goal_position, where_controller, has_controller = RonTaskOnOffTv(Settings.PositionRon[0], OnOrOffTv)
          Settings.SetActualSolution(solution)
          if (Settings.ActualSolution != [[]]):
              if (Settings.HasController[0] == 'no'):
                  Has_controller = False;
              else:
                  Has_controller = True;
              actions = define_actions_robot(Settings.ActualSolution[0])

              start_pos_mess = start_position_message_tv(robot_position=Settings.PositionRon[0],
                                                         position_object=where_controller,
                                                         position_tv=Settings.PositionTv[0])
              plan_mess = planning_message_tv(has_controller=Has_controller, planning=actions)

              Popup('Start Position : ', start_pos_mess)
              Popup('Solution : ', plan_mess)
              robot_environment(actions, Settings.PositionRon[0], where_controller, goal_position, Has_controller, targ=task)
          else:
              event, sol = Window(robot_gui_title,
                                    'the problem is not feasible.\nIt is necessary to add in Database Of Actions of Ron:\n-OnTv / OffTv\n-PickupController\nYou can choose one of these actions :\nP.s You can Add also an action\nthat will be useful after for other task.'
                                  , list=Settings.AllActions, key="ADD_DEL_ACT")

              if event == 'Ok':
                  Settings.AddAction(sol['ADD_DEL_ACT'][0])
                  Settings.DropAction((sol['ADD_DEL_ACT'][0]).name)
                  ModifyDatabaseActions(Settings.ActualActions)
                  ModifyDatabaseAllActionsAvailable(Settings.AllActions)
                  MainTaskOnOffTV(name,task)
              else:
                  PopupCancel(robot_gui_aborted)


# choosenTasks : The choiche of Tasks that Ron has to do
#
# Parameters:
# -
# allert : when task is not selected , allert message (Allert)
# name : the name selected at beginning


def choosenTasks(name, allert=""):
    message = "%s , how can i help you? \n" %(name)
    message += '{:s}'.format('\u0332'.join(allert)) ;
    event, rips = WindowTask(title=robot_gui_title,message=message,list=['Bring to me keys',
                                                                         'Bring to me food delivered',
                                                                         'On/Off Tv',
                                                                         'Cook me something',
                                                                         'Open/Close Garage'],key="Tk")
    ModifyDatabaseStorage(name)
    Settings.ModifyName(name)
    if event == 'Ok':
        if(rips['Tk'] != []):
            SetAllActionsAvailableFromDB()
            SetAllActionsFromDB()
            if(rips['Tk'][0] == 'Bring to me keys'):
                   MainTaskKeys(name,task=rips['Tk'][0]);
            elif(rips['Tk'][0] == 'Bring to me food delivered'):
                   MainTaskFood(name,task=rips['Tk'][0]);
            elif (rips['Tk'][0] == 'On/Off Tv'):
                  MainTaskOnOffTV(name, task=rips['Tk'][0]);
            elif(rips['Tk'][0] == 'Open/Close Garage'):
                   MainTaskOpenCloseGarage(name,task=rips['Tk'][0]);
            elif(rips['Tk'][0] == 'Cook me something'):
                   MainTaskCook(name,task=rips['Tk'][0]);
        else:
            choosenTasks(name,allert='Please, choose Task')
    if event == 'Reset Db':
        ClearDatabaseStorage();
        ClearDatabaseActions();
        Settings.ClearActualSolution();
        ProgressWinodw(robot_gui_title, 'Reset of Database ...', 100, 10)
        subprocess.run('python MainRonRobot.py')
    if(event == 'View Home'):
        event, result = ViewMapPopup(robot_gui_title);
        if(event == 'Back'):
            choosenTasks(name)
        else:
            PopupCancel(robot_gui_aborted)
    else:
        PopupCancel(robot_gui_aborted)


# The main function

if __name__ == "__main__":
    sg.theme('DarkAmber')
    Settings.init()
    name_db = ReadDatabaseStorage();
    if(name_db != ''):
       result = name_db.index(' 1')
       choosenTasks(name_db[:result]);
    else:
        event, name = sg.Window(
            robot_gui_title,
            [
                [sg.Image(r'Image\robot.png')],
                [sg.Text('Hi, im Ron, The Robot that aims to performs many task on your Home!')],
                [sg.Text('Can i know your Name?'), sg.InputText()],
                [sg.Text('When you are ready, Click OK to Start! ')],
                [sg.Button('Ok'), sg.Button('Off Ron')]]).read(close=True)

        if event == 'Ok':
            choosenTasks(name[1]);

        else:
            PopupCancel(robot_gui_aborted)

