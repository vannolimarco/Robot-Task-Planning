# Import libraries
import aima.utils
import aima.planning
import  Settings
import pickle

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
This file aims to built a planning problem for the Task selected.
Thus this methods provide all Knowledge,Domains that Actions
(Database or Not) that are important in order to perform 
the Algorithm based on PDDL.
Thus, will be used aima object that allow us to use a PDDL 
language for Graph algorithm. 
"""


def ron_plannig_problem_keys(initial_state, goals):

    # Create a knowledge base
    kb = [
          aima.utils.expr("Connected(Floor,Bedroom)"),
          aima.utils.expr("Connected(Floor,Kitchen)"),
          aima.utils.expr("Connected(Kitchen,Floor)"),
          aima.utils.expr("Connected(Floor,Bathroom)"),
          aima.utils.expr("Connected(Bathroom,Floor)"),
          aima.utils.expr("Connected(Livingroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Personalroom)"),
          aima.utils.expr("Connected(Personalroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Floor)"),
          aima.utils.expr("Connected(Bedroom,Livingroom)")
          ]

    # Add initial state to the knowledge base
    kb.extend(initial_state)

    # Create domains
    domains = [aima.utils.expr("Robot(Ron)"),
               aima.utils.expr("Packet(Keys)"),
               aima.utils.expr("Room(Personalroom)"),
               aima.utils.expr("Room(Floor)"),
               aima.utils.expr("Room(Kitchen)"),
               aima.utils.expr("Room(Bathroom)"),
               aima.utils.expr("Room(Bedroom)"),
               aima.utils.expr("Room(Livingroom)")
               ]

    try:
       filehandler = open('actions.pkl', 'rb')
       actions_store = pickle.load(filehandler)
    except:
        actions_store = [];
    if(actions_store != None and actions_store != [] ):
        actions = actions_store;
    else:
        actions = Settings.ActualActions;

    # Create a planning problem
    problem = aima.planning.PlanningProblem(kb, goals, actions, domains)

    # Return the problem
    return problem


def ron_plannig_problem_food(initial_state, goals):

    # Create a knowledge base
    kb = [
          aima.utils.expr("Connected(Floor,Bedroom)"),
          aima.utils.expr("Connected(Floor,Kitchen)"),
          aima.utils.expr("Connected(Kitchen,Floor)"),
          aima.utils.expr("Connected(Floor,Bathroom)"),
          aima.utils.expr("Connected(Floor,Door)"),
          aima.utils.expr("Connected(Door,Floor)"),
          aima.utils.expr("Connected(Bathroom,Floor)"),
          aima.utils.expr("Connected(Livingroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Personalroom)"),
          aima.utils.expr("Connected(Personalroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Floor)"),
          aima.utils.expr("Connected(Bedroom,Livingroom)")
          ]

    # Add initial state to the knowledge base
    kb.extend(initial_state)

    # Create domains
    domains = [aima.utils.expr("Robot(Ron)"),
               aima.utils.expr("Food(Food)"),
               aima.utils.expr("Room(Personalroom)"),
               aima.utils.expr("Room(Floor)"),
               aima.utils.expr("Room(Door)"),
               aima.utils.expr("Room(Kitchen)"),
               aima.utils.expr("Room(Bathroom)"),
               aima.utils.expr("Room(Bedroom)"),
               aima.utils.expr("Room(Livingroom)")
               ]

    try:
       filehandler = open('actions.pkl', 'rb')
       actions_store = pickle.load(filehandler)
    except:
        actions_store = [];
    if(actions_store != None and actions_store != [] ):
        actions = actions_store;
    else:
        actions = Settings.ActualActions;

    # Create a planning problem
    problem = aima.planning.PlanningProblem(kb, goals, actions, domains)

    # Return the problem
    return problem

def ron_plannig_problem_cook_food(initial_state, goals):

    # Create a knowledge base
    kb = [
          aima.utils.expr("Connected(Floor,Bedroom)"),
          aima.utils.expr("Connected(Floor,Kitchen)"),
          aima.utils.expr("Connected(Kitchen,Floor)"),
          aima.utils.expr("Connected(Floor,Bathroom)"),
          aima.utils.expr("Connected(Floor,Door)"),
          aima.utils.expr("Connected(Door,Floor)"),
          aima.utils.expr("Connected(Bathroom,Floor)"),
          aima.utils.expr("Connected(Livingroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Personalroom)"),
          aima.utils.expr("Connected(Personalroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Floor)"),
          aima.utils.expr("Connected(Bedroom,Livingroom)")
          ]

    # Add initial state to the knowledge base
    kb.extend(initial_state)

    # Create domains
    domains = [aima.utils.expr("Robot(Ron)"),
               aima.utils.expr("Food(Sandwich)"),
               aima.utils.expr("Food(Pasta)"),
               aima.utils.expr("Food(Hamburger)"),
               aima.utils.expr("Room(Personalroom)"),
               aima.utils.expr("Room(Floor)"),
               aima.utils.expr("Room(Door)"),
               aima.utils.expr("Room(Kitchen)"),
               aima.utils.expr("Room(Bathroom)"),
               aima.utils.expr("Room(Bedroom)"),
               aima.utils.expr("Room(Livingroom)")
               ]

    try:
       filehandler = open('actions.pkl', 'rb')
       actions_store = pickle.load(filehandler)
    except:
        actions_store = [];
    if(actions_store != None and actions_store != [] ):
        actions = actions_store;
    else:
        actions = Settings.ActualActions;

    # Create a planning problem
    problem = aima.planning.PlanningProblem(kb, goals, actions, domains)

    # Return the problem
    return problem

def ron_plannig_problem_on_off_tv(initial_state, goals):

    # Create a knowledge base
    kb = [
          aima.utils.expr("Connected(Floor,Bedroom)"),
          aima.utils.expr("Connected(Floor,Kitchen)"),
          aima.utils.expr("Connected(Kitchen,Floor)"),
          aima.utils.expr("Connected(Floor,Bathroom)"),
          aima.utils.expr("Connected(Floor,Door)"),
          aima.utils.expr("Connected(Door,Floor)"),
          aima.utils.expr("Connected(Bathroom,Floor)"),
          aima.utils.expr("Connected(Livingroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Personalroom)"),
          aima.utils.expr("Connected(Personalroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Floor)"),
          aima.utils.expr("Connected(Bedroom,Livingroom)")
          ]

    # Add initial state to the knowledge base
    kb.extend(initial_state)

    # Create domains
    domains = [aima.utils.expr("Robot(Ron)"),
               aima.utils.expr("ControlDevice(Controller)"),
               aima.utils.expr("Device(Tv)"),
               aima.utils.expr("Room(Personalroom)"),
               aima.utils.expr("Room(Floor)"),
               aima.utils.expr("Room(Door)"),
               aima.utils.expr("Room(Kitchen)"),
               aima.utils.expr("Room(Bathroom)"),
               aima.utils.expr("Room(Bedroom)"),
               aima.utils.expr("Room(Livingroom)")
               ]

    try:
       filehandler = open('actions.pkl', 'rb')
       actions_store = pickle.load(filehandler)
    except:
        actions_store = [];
    if(actions_store != None and actions_store != [] ):
        actions = actions_store;
    else:
        actions = Settings.ActualActions;

    # Create a planning problem
    problem = aima.planning.PlanningProblem(kb, goals, actions, domains)

    # Return the problem
    return problem


def ron_plannig_problem_open_close_garage(initial_state, goals):

    # Create a knowledge base
    kb = [
          aima.utils.expr("Connected(Floor,Bedroom)"),
          aima.utils.expr("Connected(Floor,Kitchen)"),
          aima.utils.expr("Connected(Kitchen,Floor)"),
          aima.utils.expr("Connected(Floor,Bathroom)"),
          aima.utils.expr("Connected(Bathroom,Floor)"),
          aima.utils.expr("Connected(Floor,Door)"),
          aima.utils.expr("Connected(Door,Floor)"),
          aima.utils.expr("Connected(Livingroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Personalroom)"),
          aima.utils.expr("Connected(Personalroom,Bedroom)"),
          aima.utils.expr("Connected(Bedroom,Floor)"),
          aima.utils.expr("Connected(Bedroom,Livingroom)")
          ]

    # Add initial state to the knowledge base
    kb.extend(initial_state)

    # Create domains
    domains = [aima.utils.expr("Robot(Ron)"),
               aima.utils.expr("Packet(Keys)"),
               aima.utils.expr("Garage(Garage)"),
               aima.utils.expr("Room(Personalroom)"),
               aima.utils.expr("Room(Door)"),
               aima.utils.expr("Room(Floor)"),
               aima.utils.expr("Room(Kitchen)"),
               aima.utils.expr("Room(Bathroom)"),
               aima.utils.expr("Room(Bedroom)"),
               aima.utils.expr("Room(Livingroom)")
               ]

    try:
       filehandler = open('actions.pkl', 'rb')
       actions_store = pickle.load(filehandler)
    except:
        actions_store = [];
    if(actions_store != None and actions_store != [] ):
        actions = actions_store;
    else:
        actions = Settings.ActualActions;

    # Create a planning problem
    problem = aima.planning.PlanningProblem(kb, goals, actions, domains)

    # Return the problem
    return problem