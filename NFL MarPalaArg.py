# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:39:50 2019

@author: mpala
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('pbp-2019.csv')

table_1 = pd.pivot_table(df, index='OffenseTeam',  aggfunc=np.sum)


def get_data(team):

    
    df = pd.DataFrame({
    'group': [team,'MEAN'],
    'Is Fumble': [np.log(table_1.loc[team,'IsFumble']), np.log(round(table_1['IsFumble'].mean(),0))],
#    'Is Incomplete': [table_1.loc[team,'IsIncomplete'], round(table_1['IsIncomplete'].mean(),0)],
    'Is Interception': [np.log(table_1.loc[team,'IsInterception']), np.log(round(table_1['IsInterception'].mean(),0))],
    'Is Penalty': [np.log(table_1.loc[team,'IsPenalty']), np.log(round(table_1['IsPenalty'].mean(),0))],
    'Is Sack': [np.log(table_1.loc[team,'IsSack']), np.log(round(table_1['IsSack'].mean(),0))]
    })

    
    
    # ------- PART 1: Create background
     
    # number of variable
    categories=list(df)[1:]
    N = len(categories)
     
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
     
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
     
    # If you want the first axis to be on top:
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
     
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories)
     
    # Draw ylabels
    ax.set_rlabel_position(0)
    #plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
    plt.ylim(0,5)
     
     
    # ------- PART 2: Add plots
     
    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable
     
    # Ind1
    values=df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=f"{team}")
    ax.fill(angles, values, 'b', alpha=0.1)
     
    # Ind2
    values=df.loc[1].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="MEAN")
    ax.fill(angles, values, 'r', alpha=0.1)
     
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.show()

# =============================================================================
# Example Mahomes vs Garoppolo team 2020 SuperBowl
# =============================================================================
get_data('KC')
get_data('SF')
