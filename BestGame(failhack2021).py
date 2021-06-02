import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv
from geopy import distance
from math import radians, sin, cos, acos

scr1 = 0
scr2 = 0
i = 0
crd1 = []
crd2 = []
banned = []

s1 = input().lower()
banned.append(s1)
with open('worldcities_for_best_game.csv') as database:
    reader = csv.reader(database)

    for row in reader:
        if(row[1].lower() == s1):
            crd1.append(row[2])
            crd1.append(row[3])
            break

    fig = go.Figure(go.Scattergeo())
    fig.update_geos(projection_type='orthographic')
    fig.update_layout(height=250, margin={"r":0,"t":0,"l":0,"b":0})
    while True:
        s2 = input().lower()
        if (s2 == 'end the game'):
            if (scr1 > scr2):
                print('Player 1 wins!!! Congrats!!!')
            elif (scr1 < scr2):
                print('Player 2 wins!!! Congrats!!!')
            else: 
                print('Draw, nobody won :(')
            break
        while s1[-1] != s2[0] and s2 not in banned:
            s2 = input().lower()
            banned.append(s2)
        database.seek(0)
        reader = csv.reader(database)
        for row in reader:
            if (row[1].lower() == s2):
                crd2.append(row[2])
                crd2.append(row[3])
                break
                
        fig.add_trace(go.Scattergeo(
            mode = 'markers+lines',
            lon = [crd1[1], crd2[1]],
            lat =[crd1[0], crd2[0]],
            marker = {'size':10}
            ))

        slat = radians(float(crd1[0]))
        slon = radians(float(crd1[1]))
        elat = radians(float(crd2[0]))
        elon = radians(float(crd2[1]))
        dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))

        if (i == 0):
            scr1 += dist
        else:
            scr2 += dist

        i+= 1
        s1 = s2
        crd1 = crd2
        crd2 = []
        fig.show() 
