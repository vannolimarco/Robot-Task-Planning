# Import libraries
import aima.utils
import aima.planning


# -----------------------------------------------------------
# Project based on PDDL (AI)
# The Project is based on a planning for some tasks that the robot Ron
# has to compute
# (C) 2021 Vannoli Marco, Rome, Italy
# email vannoli.1860363@studenti.uniroma1.it
# -----------------------------------------------------------


"""
This file show all Global Variable that are important in order
to have ,whenever we need, all Data necessary to continue 
in the interaction
"""

global AllActions
AllActions = [aima.planning.Action("PickupKeys(b, p, r)",
                                   precond="At(b, r) & At(p, r) & ~Has(b, p)",
                                   effect="Has(b, p) & ~At(p, r)",
                                   domain="Robot(b) & Packet(p) & Room(r)"),
              aima.planning.Action("DropKeys(b, p, r)",
                                   precond="At(b, r) & Has(b, p) ",
                                   effect="At(p, r) & ~Has(b, p)",
                                   domain="Robot(b) & Packet(p) & Room(r)"),
              aima.planning.Action("PickupFood(b, p, r)",
                                   precond="At(b, r) & At(p, r) & ~Has(b, p)",
                                   effect="Has(b, p) & ~At(p, r)",
                                   domain="Robot(b) & Food(p) & Room(r)"),
              aima.planning.Action("DropFood(b, p, r)",
                                   precond="At(b, r) & Has(b, p)",
                                   effect="At(p, r) & ~Has(b, p)",
                                   domain="Robot(b) & Food(p) & Room(r)"),
              aima.planning.Action("PickupControllerTV(b, p, r)",
                                   precond="At(b, r) & At(p, r) & ~Has(b, p)",
                                   effect="~At(p, r) & Has(b, p)",
                                   domain="Robot(b) & ControlDevice(p) & Room(r)"),
              aima.planning.Action("OnTv(b, p, r, t)",
                                   precond="At(b, r) &  Has(b, p) & ~On(t)",
                                   effect="On(t)",
                                   domain="Robot(b) & ControlDevice(p) & Device(t) & Room(r)"),
              aima.planning.Action("CookFood(b, p, r)",
                                    precond="At(b, r) & ~On(p) & At(p, r)",
                                    effect="On(p)",
                                    domain="Robot(b) & Food(p) & Room(r)"),
              aima.planning.Action("OffTv(b, p, r, t)",
                                   precond="At(b, r) &  Has(b, p) & On(t)",
                                   effect="~On(t)",
                                   domain="Robot(b) & ControlDevice(p) & Device(t) & Room(r)"),
              aima.planning.Action("OpenGarage(b, p, r,t)",
                                   precond="At(b, r) & ~On(t) & Has(b,p)",
                                   effect="On(t)",
                                   domain="Robot(b) & Packet(p) & Garage(t) & Room(r)"),
              aima.planning.Action("CloseGarage(b, p, r,t)",
                                   precond="At(b, r) & On(t) & Has(b,p)",
                                   effect="~On(t)",
                                   domain="Robot(b) & Packet(p) & Garage(t) & Room(r)"),
              ]
def init():
    global ActualActions
    ActualActions = [aima.planning.Action("Move(b, f, t)",
                                    precond="At(b, f) & Connected(f, t)",
                                    effect="At(b, t) & ~At(b, f)",
                                    domain="Robot(b) & Room(f) & Room(t)")
                    ]
    global PositionRon
    PositionRon = [];
    global PositionPerson
    PositionPerson = [];
    global PositionKeys
    PositionKeys = [];
    global PositionFood
    PositionFood = ['Door'];
    global PositionFoodCooking
    PositionFoodCooking = ['Kitchen'];
    global PositionTv
    PositionTv = ['Livingroom'];
    global PositionController
    PositionController = []
    global  PositionGarage
    PositionGarage = ['Door']
    global OnTv
    OnTv = []
    global OpenGarage
    OpenGarage = []
    global HasKeys
    HasKeys = [];
    global HasFood
    HasFood = [];
    global  TypeFood
    TypeFood = []
    global HasController
    HasController = [];
    global ActualSolution
    ActualSolution = [];
    global Name
    Name = []

def AddAction(action):
        ActualActions.append(action)

def DropAction(name_):
    index = 0;
    for i in AllActions:
        index += 1;
        if(i.name == name_):
            index_i = index;
    AllActions.pop(index_i-1)

def ClearActualActions():
    ActualActions.clear()

def ModifyName(name):
    Name.append(name)
def SetPositionRon(pos):
        PositionRon.append(pos);

def SetPositionPerson(pos):
        PositionPerson.append(pos);

def SetPositionKeys(pos):
        PositionKeys.append(pos);
def SetOpenGarage(pos):
    OpenGarage.append(pos)
def SetPositionFood(pos):
    PositionFood.append(pos);

def SetPositionController(pos):
    PositionController.append(pos);

def SetPositionHasKey(pos):
        HasKeys.append(pos);

def SetPositionHasFood(pos):
    HasFood.append(pos);

def SetTypeFood(food):
    TypeFood.append(food);

def SetPositionHasController(pos):
    HasController.append(pos);
def SetActualSolution(pos):
        ActualSolution.append(pos);

def ClearActualSolution():
     ActualSolution.clear()
def ClearAllSettingTask():
    PositionRon.clear();
    PositionPerson.clear();
    PositionKeys.clear();
    PositionFood.clear();
    HasKeys.clear();
    ActualSolution.clear();