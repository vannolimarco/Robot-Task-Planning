

# -----------------------------------------------------------
# Project based on PDDL (AI)
# The Project is based on a planning for some tasks that the robot Ron
# has to compute
# (C) 2021 Vannoli Marco, Rome, Italy
# email vannoli.1860363@studenti.uniroma1.it
# -----------------------------------------------------------


"""
This file has the method that give an interpretetion of Actions
produced by Aima Library.
"""

def define_actions_robot(plan):
    actions = []
    for i in plan:
        for e in i:
            action = []
            if('Move' in str(e)):
                action.append('move')
                u = str(e).split()
                action.append(u[1].replace(')',''))
                action.append(u[2].replace(')',''))
            if('PickupKeys' in str(e)):
                action.append('pickupkeys')
                u = str(e).split()
                action.append(u[1].replace(')',''))
                action.append(u[2].replace(')',''))
            if('DropKeys' in str(e)):
                action.append('dropkeys')
                u = str(e).split()
                action.append(u[1].replace(')',''))
                action.append(u[2].replace(')',''))
            if ('PickupFood' in str(e)):
                action.append('pickupfood')
                u = str(e).split()
                action.append(u[1].replace(')', ''))
                action.append(u[2].replace(')', ''))
            if ('DropFood' in str(e)):
                action.append('dropfood')
                u = str(e).split()
                action.append(u[1].replace(')', ''))
                action.append(u[2].replace(')', ''))
            if ('PickupControllerTV' in str(e)):
                action.append('pickupcontroller')
                u = str(e).split()
                action.append(u[1].replace(')', ''))
                action.append(u[2].replace(')', ''))
            if ('OnTv' in str(e)):
                action.append('ontv')
                u = str(e).split()
                action.append(u[1].replace(')', ''))
                action.append(u[2].replace(')', ''))
            if ('OffTv' in str(e)):
                action.append('offtv')
                u = str(e).split()
                action.append(u[1].replace(')', ''))
                action.append(u[2].replace(')', ''))
            if ('CookFood' in str(e)):
                action.append('cookfood')
                u = str(e).split()
                action.append(u[1].replace(')', ''))
                action.append(u[2].replace(')', ''))
            if ('OpenGarage' in str(e)):
                action.append('opengarage')
                u = str(e).split()
                action.append(u[1].replace(')', ''))
                action.append(u[2].replace(')', ''))
            if ('CloseGarage' in str(e)):
                action.append('closegarage')
                u = str(e).split()
                action.append(u[1].replace(')', ''))
                action.append(u[2].replace(')', ''))
            actions.append(action)
    return actions

