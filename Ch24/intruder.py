# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:09:42 2017

@author: Kevin Young
"""
#PB for press button
#EP for enter PIN
#ABR for alarm bell ring
#AM for alert mode 
#SA for system activated
#SEA for sensor activated
#SI for system inactive
#TMP for Two minutes pass

state = 'SI'
stop = False
while stop == False:
    action = str(input('please enter the action'))
    if state == 'SI':
        if action == 'PB':
            state ='SA'
    elif state == 'SA':
        if action == 'PB':
            state ='SA'
        elif action == 'EP':
            state = 'SI'
        elif action == 'SEA':
            state = 'AM'
    elif state == 'AM':
         if action == 'EP':
             state = 'SI'
         elif action == 'TMP':
             state = 'ABR'
         elif action == 'PB':
             state = 'AM'
    elif state == 'AMR':
        if action ==  'PB':
            state =  'AMR'
        elif action == 'EP':
            state = 'SI'
    if state == 'SI':
        State =  'system inactivated' 
    elif state == 'SA':
        State = 'system activated' 
    elif state == 'AM':
        State = 'alert mode'
    elif state ==  'ABR':
        State =  'Ring, Ring!!!'
    print (State)