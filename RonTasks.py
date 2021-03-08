from Gui import Window,PopupCancel,ProgressWinodw
from RonPlanning import *
import aima.utils
import aima.planning
from Utils import *
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
This file aims to create all interaction (not all) for each task 
and to Create the Start situations from all Informations given from User.
Thus this methods provide all Knowledge,Domains that Actions
Thus, will be used aima object that allow us to use a PDDL 
language for Graph algorithm. This methods create all 
interaction and start position for each Tasks.
(selected bu User)
"""


def RonTaskKeys(position_start):
    solution = []
    Settings.ClearActualSolution();
    if(Settings.HasKeys == [] and Settings.PositionKeys == [] and Settings.PositionPerson == []):
        event, goal_position = Window(robot_gui_title, 'Where are you now? ', 'LC',['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor'])
        if event == 'Ok':
            goal_position = goal_position["LC"][0];
            event, keys = Window(robot_gui_title, 'I already have the keys you need (no or yes) ', 'LF',['no', 'yes'])
            if event == 'Ok':
                keys = keys["LF"][0];
                if (keys.strip() == "no"):
                    has_keys = False
                    event, where_keys = Window(robot_gui_title, 'Where are the keys? ', 'LR',['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor'])
                    if event == 'Ok':

                        where_keys =where_keys["LR"][0]

                        Settings.SetPositionHasKey(keys);
                        Settings.SetPositionPerson(goal_position);
                        Settings.SetPositionKeys(where_keys);
                        try:
                            solution.append(RonTaskKeysPosStart(initial_position=position_start.strip(), has_keys=keys.strip(),
                                                                 where_keys=where_keys.strip(),
                                                                 goal_position=where_keys.strip()))

                            solution.append(RonTaskKeysPosStart(initial_position=where_keys.strip(), has_keys="go_with_keys",
                                                                 where_keys=where_keys.strip(),
                                                                 goal_position=goal_position.strip()))
                            solution.append(RonTaskKeysPosStart(initial_position=goal_position.strip(), has_keys="bo",
                                                                 where_keys=goal_position.strip(),
                                                                 goal_position=goal_position.strip()))
                            ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                            solution = [x for x in solution if x != []]
                            Settings.SetActualSolution(solution)
                        except:
                            Settings.ClearActualSolution();
                            solution = [];
                    else:
                        PopupCancel(robot_gui_aborted)
                        #ClearDatabaseActions()
                else:
                    has_keys = True;
                    where_keys = position_start
                    Settings.SetPositionHasKey(keys.strip());
                    Settings.SetPositionPerson(goal_position.strip());
                    Settings.SetPositionKeys(where_keys.strip());
                    try:
                       solution.append(RonTaskKeysPosStart(initial_position=position_start, has_keys="go_with_keys",
                                                         where_keys=position_start,
                                                         goal_position=goal_position))
                       solution.append(RonTaskKeysPosStart(initial_position=goal_position, has_keys="bo",
                                                         where_keys=goal_position,
                                                         goal_position=goal_position))
                       ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)

                       solution = [x for x in solution if x != []]
                       Settings.SetActualSolution(solution)
                    except:
                        Settings.ClearActualSolution();
                        solution = [];
            else:
                PopupCancel(robot_gui_aborted)
                #ClearDatabaseActions()
        else:
            PopupCancel(robot_gui_aborted)
            #ClearDatabaseActions()
    else:
        if(Settings.HasKeys[0] == 'no'):
            has_keys = False;
        else:
            has_keys = True;
        where_keys = Settings.PositionKeys[0];
        goal_position = Settings.PositionPerson[0];
        if(Settings.HasKeys[0] == 'no'):
            try:
                solution.append(RonTaskKeysPosStart(initial_position=position_start.strip(), has_keys=Settings.HasKeys[0],
                                                    where_keys=Settings.PositionKeys[0],
                                                    goal_position=Settings.PositionKeys[0]))

                solution.append(RonTaskKeysPosStart(initial_position=Settings.PositionKeys[0], has_keys="go_with_keys",
                                                    where_keys=Settings.PositionKeys[0],
                                                    goal_position=Settings.PositionPerson[0]))
                solution.append(RonTaskKeysPosStart(initial_position=Settings.PositionPerson[0], has_keys="bo",
                                                    where_keys=Settings.PositionPerson[0],
                                                    goal_position=Settings.PositionPerson[0]))
                ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                solution = [x for x in solution if x != []]
                Settings.SetActualSolution(solution)
            except:
                Settings.ClearActualSolution();
                solution = [];
        else:
            try:
                solution.append(RonTaskKeysPosStart(initial_position=position_start.strip(), has_keys="go_with_keys",
                                                    where_keys=position_start.strip(),
                                                    goal_position=Settings.PositionPerson[0]))
                solution.append(RonTaskKeysPosStart(initial_position=Settings.PositionPerson[0], has_keys="bo",
                                                    where_keys=Settings.PositionPerson[0],
                                                    goal_position=Settings.PositionPerson[0]))
                ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)

                solution = [x for x in solution if x != []]
                Settings.SetActualSolution(solution)
            except:
                Settings.ClearActualSolution();
                solution = [];
    return solution,goal_position,where_keys,has_keys

def RonTaskOpenCloseGarage(position_start,taskOpenCloseOff):
    solution = []
    Settings.ClearActualSolution();
    if(Settings.HasKeys == [] and Settings.PositionKeys == []):
            goal_position = Settings.PositionGarage[0];
            event, keys = Window(robot_gui_title, 'I already have the keys you need (no or yes) ', 'LF',['no', 'yes'])
            if event == 'Ok':
                keys = keys["LF"][0];
                if (keys.strip() == "no"):
                    has_keys = False
                    event, where_keys = Window(robot_gui_title, 'Where are the keys? ', 'LR',['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor'])
                    if event == 'Ok':

                        where_keys =where_keys["LR"][0]

                        Settings.SetPositionHasKey(keys);
                        Settings.SetPositionKeys(where_keys);
                        try:
                            solution.append(RonTaskOpenCloseGaragePosStart(initial_position=position_start.strip(), has_keys=keys.strip(),
                                                                 where_keys=where_keys.strip(),
                                                                 goal_position=where_keys.strip(),taskOpenCloseOff=taskOpenCloseOff))

                            solution.append(RonTaskOpenCloseGaragePosStart(initial_position=where_keys.strip(), has_keys="go_with_keys",
                                                                 where_keys=where_keys.strip(),
                                                                 goal_position=goal_position.strip(),taskOpenCloseOff=taskOpenCloseOff))
                            solution.append(RonTaskOpenCloseGaragePosStart(initial_position=goal_position.strip(), has_keys="OpenCloseGarage",
                                                                 where_keys=goal_position.strip(),
                                                                 goal_position=goal_position.strip(),taskOpenCloseOff=taskOpenCloseOff))
                            ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                            solution = [x for x in solution if x != []]
                            Settings.SetActualSolution(solution)
                        except:
                            Settings.ClearActualSolution();
                            solution = [];
                    else:
                        PopupCancel(robot_gui_aborted)
                else:
                    has_keys = True;
                    where_keys = position_start
                    Settings.SetPositionHasKey(keys.strip());
                    Settings.SetPositionPerson(goal_position.strip());
                    Settings.SetPositionKeys(where_keys.strip());
                    try:
                       solution.append(RonTaskOpenCloseGaragePosStart(initial_position=position_start, has_keys="go_with_keys",
                                                         where_keys=position_start,
                                                         goal_position=goal_position,taskOpenCloseOff=taskOpenCloseOff))
                       solution.append(RonTaskOpenCloseGaragePosStart(initial_position=goal_position, has_keys="OpenCloseGarage",
                                                         where_keys=goal_position,
                                                         goal_position=goal_position,taskOpenCloseOff=taskOpenCloseOff))
                       ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)

                       solution = [x for x in solution if x != []]
                       Settings.SetActualSolution(solution)
                    except:
                        Settings.ClearActualSolution();
                        solution = [];
            else:
                PopupCancel(robot_gui_aborted)
    else:
        if(Settings.HasKeys[0] == 'no'):
            has_keys = False;
        else:
            has_keys = True;
        where_keys = Settings.PositionKeys[0];
        goal_position = Settings.PositionGarage[0];
        if(Settings.HasKeys[0] == 'no'):
            try:
                solution.append(RonTaskOpenCloseGaragePosStart(initial_position=position_start.strip(), has_keys=Settings.HasKeys[0],
                                                    where_keys=Settings.PositionKeys[0],
                                                    goal_position=Settings.PositionKeys[0],taskOpenCloseOff=taskOpenCloseOff))

                solution.append(RonTaskOpenCloseGaragePosStart(initial_position=Settings.PositionKeys[0], has_keys="go_with_keys",
                                                    where_keys=Settings.PositionKeys[0],
                                                    goal_position=Settings.PositionGarage[0],taskOpenCloseOff=taskOpenCloseOff))
                solution.append(RonTaskOpenCloseGaragePosStart(initial_position=Settings.PositionGarage[0], has_keys="OpenCloseGarage",
                                                    where_keys=Settings.PositionGarage[0],
                                                    goal_position=Settings.PositionGarage[0],taskOpenCloseOff=taskOpenCloseOff))
                ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                solution = [x for x in solution if x != []]
                Settings.SetActualSolution(solution)
            except:
                Settings.ClearActualSolution();
                solution = [];
        else:
            try:
                solution.append(RonTaskOpenCloseGaragePosStart(initial_position=position_start.strip(), has_keys="go_with_keys",
                                                    where_keys=position_start.strip(),
                                                    goal_position=Settings.PositionGarage[0],taskOpenCloseOff=taskOpenCloseOff))
                solution.append(RonTaskOpenCloseGaragePosStart(initial_position=Settings.PositionGarage[0], has_keys="OpenCloseGarage",
                                                    where_keys=Settings.PositionGarage[0],
                                                    goal_position=Settings.PositionGarage[0],taskOpenCloseOff=taskOpenCloseOff))
                ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)

                solution = [x for x in solution if x != []]
                Settings.SetActualSolution(solution)
            except:
                Settings.ClearActualSolution();
                solution = [];
    return solution,goal_position,where_keys,has_keys

def RonTaskFood(position_start, where_food):
    solution = []
    Settings.ClearActualSolution();
    if(Settings.HasFood == []  and Settings.PositionPerson == []):
        event, goal_position = Window(robot_gui_title, 'Where are you now? ', 'LC',['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor'])
        if event == 'Ok':
            goal_position = goal_position["LC"][0];
            event, food = Window(robot_gui_title, 'I already have the Food you need (no or yes) ', 'LF',['no', 'yes'])
            if event == 'Ok':
                food = food["LF"][0];
                if (food.strip() == "no"):
                    has_food = False
                    #event, where_keys = Window(robot_gui_title, 'Where are the keys? ', 'LR',['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor'])
                    #if event == 'Ok':
                    Settings.SetPositionHasFood(food);
                    Settings.SetPositionPerson(goal_position);
                   # settings.SetPositionFood(where_food);
                    try:
                        solution.append(RonTaskFoodPosStart(initial_position=position_start.strip(), has_food=food.strip(),
                                                             where_food=where_food.strip(),
                                                             goal_position=where_food.strip()))

                        solution.append(RonTaskFoodPosStart(initial_position=where_food.strip(), has_food="go_with_food",
                                                             where_food=where_food.strip(),
                                                             goal_position=goal_position.strip()))
                        solution.append(RonTaskFoodPosStart(initial_position=goal_position.strip(), has_food="bo",
                                                             where_food=goal_position.strip(),
                                                             goal_position=goal_position.strip()))
                        ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                        solution = [x for x in solution if x != []]
                        Settings.SetActualSolution(solution)
                    except:
                        Settings.ClearActualSolution();
                        solution = [];
                else:
                    has_food = True;
                    where_food = position_start
                    Settings.SetPositionHasFood(food.strip());
                    Settings.SetPositionPerson(goal_position.strip());
                    Settings.SetPositionFood(where_food.strip());
                    try:
                       solution.append(RonTaskFoodPosStart(initial_position=position_start, has_food="go_with_food",
                                                         where_food=where_food,
                                                         goal_position=goal_position))
                       solution.append(RonTaskFoodPosStart(initial_position=goal_position, has_food="bo",
                                                         where_food=goal_position,
                                                         goal_position=goal_position))
                       ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)

                       solution = [x for x in solution if x != []]
                       Settings.SetActualSolution(solution)
                    except:
                        Settings.ClearActualSolution();
                        solution = [];
            else:
                PopupCancel(robot_gui_aborted)
                #ClearDatabaseActions()
        else:
            PopupCancel(robot_gui_aborted)
            #ClearDatabaseActions()
    else:
        if(Settings.HasFood[0] == 'no'):
            has_food = False;
            where_food = Settings.PositionFood[0];
        else:
            has_food = True;
            where_food = Settings.PositionRon[0];

        goal_position = Settings.PositionPerson[0];
        if(Settings.HasFood[0] == 'no'):
            try:
                solution.append(RonTaskFoodPosStart(initial_position=position_start.strip(), has_food=Settings.HasFood[0],
                                                    where_food=where_food,
                                                    goal_position=where_food))

                solution.append(RonTaskFoodPosStart(initial_position=where_food, has_food="go_with_food",
                                                    where_food=where_food,
                                                    goal_position=Settings.PositionPerson[0]))
                solution.append(RonTaskFoodPosStart(initial_position=Settings.PositionPerson[0], has_food="bo",
                                                    where_food=Settings.PositionPerson[0],
                                                    goal_position=Settings.PositionPerson[0]))
                ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                solution = [x for x in solution if x != []]
                Settings.SetActualSolution(solution)
            except:
                Settings.ClearActualSolution();
                solution = [];
        else:
            try:
                solution.append(RonTaskFoodPosStart(initial_position=position_start.strip(), has_food="go_with_food",
                                                    where_food=where_food,
                                                    goal_position=Settings.PositionPerson[0]))
                solution.append(RonTaskFoodPosStart(initial_position=Settings.PositionPerson[0], has_food="bo",
                                                    where_food=Settings.PositionPerson[0],
                                                    goal_position=Settings.PositionPerson[0]))
                ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)

                solution = [x for x in solution if x != []]
                Settings.SetActualSolution(solution)
            except:
                Settings.ClearActualSolution();
                solution = [];
    return solution,goal_position,where_food,has_food

def RonTaskOnOffTv(position_start,OnOrOffTv):
    solution = []
    Settings.ClearActualSolution();
    goal_position = Settings.PositionTv[0];
    if (Settings.PositionController == []  and Settings.HasController == []):
            event, controller_tv = Window(robot_gui_title, 'I already have the Controller of Tv you need (no or yes) ', 'LF', ['no', 'yes'])
            if event == 'Ok':
                controller_tv_ = controller_tv["LF"][0];
                if (controller_tv_.strip() == "no"):
                    has_controller = False

                    Settings.SetPositionHasController(controller_tv_);
                    event, where_controller = Window(robot_gui_title, 'Where are the Controller? ', 'LR',['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom','Floor'])
                    where_controller = where_controller["LR"][0];
                    Settings.SetPositionController(where_controller)
                    if event == 'Ok':

                        try:
                            solution.append(
                                RonTaskOnOffTvPosStart(initial_position=position_start.strip(), has_controller=controller_tv_.strip(),
                                                    where_controller=where_controller.strip(),
                                                    goal_position=where_controller.strip(),taskOnOff=OnOrOffTv))

                            solution.append(RonTaskOnOffTvPosStart(initial_position=where_controller.strip(), has_controller="go_with_controller",
                                                     where_controller=where_controller.strip(),
                                                     goal_position=goal_position.strip(),taskOnOff=OnOrOffTv))
                            solution.append(RonTaskOnOffTvPosStart(initial_position=goal_position.strip(), has_controller="bo",
                                                                where_controller=goal_position.strip(),
                                                               goal_position=goal_position.strip(),taskOnOff=OnOrOffTv))
                            ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                            solution = [x for x in solution if x != []]
                            Settings.SetActualSolution(solution)
                        except:
                            Settings.ClearActualSolution();
                            solution = [];

                    else:
                        PopupCancel(robot_gui_aborted)
                        #ClearDatabaseActions()

                else:
                    has_controller = True;
                    where_controller = position_start
                    Settings.SetPositionHasController(controller_tv);

                    try:
                        solution.append(RonTaskOnOffTvPosStart(initial_position=position_start, has_controller="go_with_controller",
                                                            where_controller=where_controller,
                                                            goal_position=goal_position,taskOnOff=OnOrOffTv))
                        solution.append(RonTaskOnOffTvPosStart(initial_position=goal_position, has_controller="bo",
                                                            where_controller=goal_position,
                                                            goal_position=goal_position,taskOnOff=OnOrOffTv))
                        ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)

                        solution = [x for x in solution if x != []]
                        Settings.SetActualSolution(solution)
                    except:
                        Settings.ClearActualSolution();
                        solution = [];
            else:
                PopupCancel(robot_gui_aborted)
                #ClearDatabaseActions()
    else:
        if (Settings.HasController[0] == 'no'):
            has_controller = False;
            where_controller = Settings.PositionController[0];
        else:
            has_controller = True;
            where_controller = Settings.PositionRon[0];
        if (Settings.HasController[0] == 'no'):
            try:
                solution.append(RonTaskOnOffTvPosStart(initial_position=position_start.strip(), has_controller=Settings.HasController[0],
                                                       where_controller=where_controller,
                                                       goal_position=where_controller, taskOnOff=OnOrOffTv))

                solution.append(RonTaskOnOffTvPosStart(initial_position=where_controller, has_controller="go_with_controller",
                                                    where_controller=where_controller,
                                                    goal_position=goal_position,taskOnOff=OnOrOffTv))
                solution.append(RonTaskOnOffTvPosStart(initial_position=goal_position, has_controller="bo",
                                                    where_controller=goal_position,
                                                    goal_position=goal_position,taskOnOff=OnOrOffTv))
                ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                solution = [x for x in solution if x != []]
                Settings.SetActualSolution(solution)
            except:
                Settings.ClearActualSolution();
                solution = [];
        else:
            try:
                solution.append(RonTaskOnOffTvPosStart(initial_position=position_start.strip(), has_controller="go_with_controller",
                                                    where_controller=where_controller,
                                                    goal_position=goal_position,taskOnOff=OnOrOffTv))
                solution.append(RonTaskOnOffTvPosStart(initial_position=goal_position, has_controller="bo",
                                                   where_controller=goal_position,
                                                     goal_position=goal_position,taskOnOff=OnOrOffTv))
                ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)

                solution = [x for x in solution if x != []]
                Settings.SetActualSolution(solution)
            except:
                Settings.ClearActualSolution();
                solution = [];
    return solution, goal_position, where_controller, has_controller

def RonTaskCookFood(position_start):
    solution = []
    Settings.ClearActualSolution();
    where_food = Settings.PositionFoodCooking[0];
    if(Settings.TypeFood == []  and Settings.PositionPerson == []):
        event, goal_position = Window(robot_gui_title, 'Where are you now? ', 'LC',['Personalroom', 'Kitchen', 'Bedroom', 'Bathroom', 'Livingroom', 'Floor'])
        if event == 'Ok':
            goal_position = goal_position["LC"][0];
            event, type_food = Window(robot_gui_title, 'What type of food do you prefer?', 'FF',['Pasta', 'Sandwich','Hamburger'])
            if event == 'Ok':
                type_food = type_food["FF"][0];

                Settings.SetTypeFood(type_food);
                Settings.SetPositionPerson(goal_position);

                try:
                    solution.append(RonTaskCookFoodPosStart(initial_position=position_start.strip(), process_task='go_cook',
                                                         where_food=where_food.strip(),
                                                         goal_position=where_food.strip(),type_food=type_food))

                    solution.append(RonTaskCookFoodPosStart(initial_position=where_food.strip(), process_task="take",
                                                         where_food=where_food.strip(),
                                                         goal_position=where_food.strip(),type_food=type_food))
                    solution.append(RonTaskCookFoodPosStart(initial_position=goal_position.strip(), process_task="bring_to",
                                                         where_food=where_food.strip(),
                                                         goal_position=goal_position.strip(),type_food=type_food))
                    solution.append(RonTaskCookFoodPosStart(initial_position=goal_position.strip(), process_task="drop",
                                                            where_food=goal_position.strip(),
                                                            goal_position=goal_position.strip(),type_food=type_food))
                    ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
                    solution = [x for x in solution if x != []]
                    Settings.SetActualSolution(solution)
                except:
                    Settings.ClearActualSolution();
                    solution = [];
            else:
                PopupCancel(robot_gui_aborted)

        else:
            PopupCancel(robot_gui_aborted)

    else:
        where_food = Settings.PositionFoodCooking[0];
        goal_position = Settings.PositionPerson[0];
        type_food = Settings.TypeFood[0];
        try:
            solution.append(RonTaskCookFoodPosStart(initial_position=position_start.strip(), process_task='go_cook',
                                                    where_food=where_food.strip(),
                                                    goal_position=where_food.strip(), type_food=type_food))

            solution.append(RonTaskCookFoodPosStart(initial_position=where_food.strip(), process_task="take",
                                                    where_food=where_food.strip(),
                                                    goal_position=where_food.strip(), type_food=type_food))
            solution.append(RonTaskCookFoodPosStart(initial_position=goal_position.strip(), process_task="bring_to",
                                                    where_food=where_food.strip(),
                                                    goal_position=goal_position.strip(), type_food=type_food))
            solution.append(RonTaskCookFoodPosStart(initial_position=goal_position.strip(), process_task="drop",
                                                    where_food=goal_position.strip(),
                                                    goal_position=goal_position.strip(), type_food=type_food))
            ProgressWinodw('Load Solution ...', 'Solution AI from aima ...', 100, 10)
            solution = [x for x in solution if x != []]
            Settings.SetActualSolution(solution)
        except:
            Settings.ClearActualSolution();
            solution = [];

    return solution,goal_position,where_food,type_food

def RonTaskKeysPosStart(initial_position,has_keys, goal_position,where_keys):
    if(has_keys == "no"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("At(Keys, {})".format(where_keys)),
            aima.utils.expr("~Has(Ron, Keys)"),
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position)), aima.utils.expr("Has(Ron, Keys)")]
    if(has_keys == "go_with_keys"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("Has(Ron, Keys)"),
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position))]

    if (has_keys == "bo"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("Has(Ron, Keys)"),
            #aima.utils.expr("On(Keys)")
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position)), aima.utils.expr("~Has(Ron, Keys)")]#,aima.utils.expr("~On(Keys)")]

    problem = ron_plannig_problem_keys(initial_state, goals)
    solution = aima.planning.GraphPlan(problem).execute()
    if(solution == None):
        Settings.ClearActualSolution()
    return aima.planning.linearize(solution)

def RonTaskOpenCloseGaragePosStart(initial_position,has_keys, goal_position,where_keys,taskOpenCloseOff="OpenGarage"):

    if(has_keys == "no"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("At(Keys, {})".format(where_keys)),
            aima.utils.expr("~Has(Ron, Keys)"),
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position)), aima.utils.expr("Has(Ron, Keys)")]
    if(has_keys == "go_with_keys"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("Has(Ron, Keys)"),
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position))]

    if (has_keys == "OpenCloseGarage"):
        if(taskOpenCloseOff=="OpenGarage"):
            initial_state = [
                aima.utils.expr("At(Ron, {})".format(initial_position)),
                aima.utils.expr("Has(Ron, Keys)"),
                aima.utils.expr("~On(Garage)"),
            ]
            goals = [aima.utils.expr("On(Garage)")]
        else:
            initial_state = [
                aima.utils.expr("At(Ron, {})".format(goal_position)),
                aima.utils.expr("Has(Ron, Keys)"),
                aima.utils.expr("On(Garage)"),
            ]
            goals = [aima.utils.expr("~On(Garage)")]

    problem = ron_plannig_problem_open_close_garage(initial_state, goals)
    solution = aima.planning.GraphPlan(problem).execute()
    if(solution == None):
        Settings.ClearActualSolution()
    return aima.planning.linearize(solution)

def RonTaskFoodPosStart(initial_position,has_food, goal_position, where_food):
    if(has_food == "no"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("At(Food, {})".format(where_food)),
            aima.utils.expr("~Has(Ron, Food)"),
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position)), aima.utils.expr("Has(Ron, Food)")]
    if(has_food == "go_with_food"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("Has(Ron, Food)")
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position))]

    if (has_food == "bo"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("Has(Ron, Food)")
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position)), aima.utils.expr("~Has(Ron, Food)")]

    problem = ron_plannig_problem_food(initial_state, goals)
    solution = aima.planning.GraphPlan(problem).execute()
    if(solution == None):
        Settings.ClearActualSolution()
    return aima.planning.linearize(solution)

def RonTaskOnOffTvPosStart(initial_position,has_controller, goal_position, where_controller,taskOnOff="OnTv"):
    if(has_controller == "no"):
         initial_state = [
             aima.utils.expr("At(Ron, {})".format(initial_position)),
             aima.utils.expr("At(Controller, {})".format(where_controller)),
             aima.utils.expr("~Has(Ron, Controller)"),
         ]
         goals = [aima.utils.expr("At(Ron, {})".format(where_controller)), aima.utils.expr("Has(Ron, Controller)")]
    if(has_controller == "go_with_controller"):
        if (taskOnOff == "OnTv"):
            initial_state = [
                aima.utils.expr("At(Ron, {})".format(initial_position)),
                aima.utils.expr("Has(Ron, Controller)"),
                aima.utils.expr("~On(Tv)")
            ]
            goals = [aima.utils.expr("At(Ron, {})".format(goal_position))]
        else:
            initial_state = [
             aima.utils.expr("At(Ron, {})".format(initial_position)),
             aima.utils.expr("Has(Ron, Controller)"),
             aima.utils.expr("On(Tv)")
            ]
            goals = [aima.utils.expr("At(Ron, {})".format(goal_position))]

    if (has_controller == "bo"):
         if(taskOnOff == "OnTv"):
             initial_state = [
                 aima.utils.expr("At(Ron, {})".format(initial_position)),
                 aima.utils.expr("Has(Ron, Controller)"),
                 aima.utils.expr("~On(Tv)")
             ]
             goals = [aima.utils.expr("At(Ron, {})".format(goal_position)),  aima.utils.expr("On(Tv)")]
         else:
             initial_state = [
                 aima.utils.expr("At(Ron, {})".format(initial_position)),
                 aima.utils.expr("Has(Ron, Controller)"),
                 aima.utils.expr("On(Tv)")
             ]
             goals = [aima.utils.expr("At(Ron, {})".format(goal_position)),aima.utils.expr("~On(Tv)")]

    problem = ron_plannig_problem_on_off_tv(initial_state, goals)
    solution = aima.planning.GraphPlan(problem).execute()
    if(solution == None):
        Settings.ClearActualSolution()
    return aima.planning.linearize(solution)


def RonTaskCookFoodPosStart(initial_position,process_task, goal_position,where_food, type_food="Pasta"):
    if (process_task == "go_cook"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(initial_position)),
            aima.utils.expr("At("+type_food+", {})".format(where_food)),
            aima.utils.expr("~On({})".format(type_food)),
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position)), aima.utils.expr("On({})".format(type_food))]
    if (process_task == "take"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(where_food)),
            aima.utils.expr("At("+type_food+", {})".format(where_food)),
            aima.utils.expr("~Has(Ron, {})".format(type_food)),
        ]
        goals = [aima.utils.expr("Has(Ron, {})".format(type_food))]

    if (process_task == "bring_to"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(where_food)),
            aima.utils.expr("Has(Ron, {})".format(type_food)),
        ]
        goals = [aima.utils.expr("At(Ron, {})".format(goal_position))]
    if (process_task == "drop"):
        initial_state = [
            aima.utils.expr("At(Ron, {})".format(goal_position)),
            aima.utils.expr("Has(Ron, {})".format(type_food)),
        ]
        goals = [aima.utils.expr("~Has(Ron, {})".format(type_food))]

    problem = ron_plannig_problem_cook_food(initial_state, goals)
    solution = aima.planning.GraphPlan(problem).execute()
    if (solution == None):
        Settings.ClearActualSolution()
    return aima.planning.linearize(solution)