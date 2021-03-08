import PySimpleGUI as sg

# -----------------------------------------------------------
# Project based on PDDL (AI)
# The Project is based on a planning for some tasks that the robot Ron
# has to compute
# (C) 2021 Vannoli Marco, Rome, Italy
# email vannoli.1860363@studenti.uniroma1.it
# -----------------------------------------------------------


"""
This file aims to give all method to create a Gui that User can use to interact with Ron robot.
"""

def WindowOnlyText(title, listMessage=[]):
         obj = [];
         for i in listMessage:
             obj.append(sg.Text(i))
             return  obj
         event, result = sg.Window(title,
             [obj,[sg.Button('Ok'), sg.Button('Off Ron')]]).read(close=True)
         return event, result

def Window(title,message,key,list=[], btn_sensor=False):

    if(list != []):
        if(btn_sensor):
         event, result = sg.Window(title,
        [
            [sg.Text(message),
             sg.Listbox(list, size=(30, len(list)),key=key)],
            [sg.Button('Ok'), sg.Button('Off Ron'), sg.Button('Read From Sensor')]]).read(close=True)
        else:
            event, result = sg.Window(title,
                                      [
                                          [sg.Text(message),
                                           sg.Listbox(list, size=(30, len(list)), key=key)],
                                          [sg.Button('Ok'), sg.Button('Off Ron')]]).read(
                close=True)
    else:
         event, result = sg.Window(title,
                                  [
                                      [sg.Text(message)],
                                      [sg.Button('Ok'), sg.Button('Off Ron')]]).read(close=True)

    return event,result


def Window(title,message,key,list=[], btn_sensor=False):

    if(list != []):
        if(btn_sensor):
         event, result = sg.Window(title,
        [
            [sg.Text(message),
             sg.Listbox(list, size=(30, len(list)),key=key)],
            [sg.Button('Ok'), sg.Button('Off Ron'), sg.Button('Read From Sensor')]]).read(close=True)
        else:
            event, result = sg.Window(title,
                                      [
                                          [sg.Text(message),
                                           sg.Listbox(list, size=(30, len(list)), key=key)],
                                          [sg.Button('Ok'), sg.Button('Off Ron')]]).read(
                close=True)
    else:
         event, result = sg.Window(title,
                                  [
                                      [sg.Text(message)],
                                      [sg.Button('Ok'), sg.Button('Off Ron')]]).read(close=True)

    return event,result

def WindowTask(title,message,key,list=[]):

    if(list != []):
         event, result = sg.Window(title,
        [
            [sg.Text(message),
             sg.Listbox(list, size=(30, len(list)),key=key)],
            [sg.Text('Do you want reset the Database current? (name/actions'),sg.Button('Reset Db')],
            [sg.Button('Ok'), sg.Button('Off Ron'), sg.Button('View Home')]]).read(close=True)
    else:
         event, result = sg.Window(title,
                                  [
                                      [sg.Text(message)],
                                      [sg.Text('Do you want reset the Database current? (eliminate data as name/actions in the storage)'),sg.Button('Ok-Reset-Db')],
                                      [sg.Button('Ok'), sg.Button('Off Ron')]]).read(close=True)

    return event,result

def ViewMapPopup(title):
         event, result = sg.Window(title,
             [[sg.Text('Home Map :')],
             [sg.Image(r'Image\map_game_popup.png')],
             [sg.Button('Back'), sg.Button('Off Ron')]]).read(close=True)
         return event, result
def  PopupCancel(title):
     return  sg.popup_cancel(title)


def Popup(title,message):
    return sg.popup( title, message)


def ProgressWinodw(title,message,range_int,step=1):

    # layout the window
    layout = [[sg.Text(message)],
              [sg.ProgressBar(range_int, orientation='h', size=(20, 20), key='progressbar')],
              [sg.Cancel()]]

    # create the window`
    window = sg.Window(title, layout)
    progress_bar = window['progressbar']
    # loop that would normally do something useful
    for i in range(range_int):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=10)
        if event == 'Off Ron' or event == sg.WIN_CLOSED:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i + step)
    # done with loop... need to destroy the window as it's still open
    window.close()