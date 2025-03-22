#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import math
import time


    
noun_list = ['sand','pebble','chair','apple','grape','potato','furniture',
             'rice','lentil','pollen','car','ball','kitchenware',
            'jewelry','gravel','dust','equipment','bean','berry','seed','cabbage']


    
    
print('Enter weights for constraints C1-C3. Values should be in the range [0,1] and sum to 1')

c1_weight = float(input('C1 (indistinguishability) weight [0,1]'))
c2_weight = float(input('C2 (Collective uses of instruments) weight [0,1]'))
c3_weight = float(input('C3 (object splitting) weight [0,1]'))


if round(c1_weight + c2_weight + c3_weight,1) != 1:
    print('Weighting do not sum to 1! Please re-enter weights')
    time.sleep(3)
    c1_weight = float(input('C1 (indistinguishability) weight [0,1]'))
    c2_weight = float(input('C2 (Collective uses of instruments) weight [0,1]'))
    c3_weight = float(input('C3 (object splitting) weight [0,1]'))
else: pass

params = {}
params["C1"] = c1_weight
params["C2"] = c2_weight
params["C3"] = c3_weight

scores_alt_log = {} 
scores_alt_log["C1"] =  {'sand': 0.7986802772872492,
 'pebble': 0.5029240994214357,
 'chair': 0.037723556703629146,
 'apple': 0.08371925466638086,
 'grape': 0.08345377102801421,
 'potato': 0.17988110786594513,
 'furniture': 0.06473673313780814,
 'rice': 0.31245079996663294,
 'lentil': 0.07887183867175607,
 'pollen': 0.6598695189648712,
 'car': 0.007019528068444747,
 'ball': 0.041306648833177695,
 'kitchenware': 0.018396566491603816,
 'jewelry': 0.01192242894437845,
 'gravel': 0.4502340125651543,
 'dust': 0.9981618638504255,
 'equipment': 0.011201899385833713,
 'bean': 0.10140774339421321,
 'berry': 0.2321608613390369,
 'seed': 0.2764481362346105,
 'cabbage': 0.10290522082473774}

scores_alt_log["C2"] = {'sand': 0,
 'pebble': 0,
 'chair': 0,
 'apple': 0,
 'grape': 0,
 'potato': 0,
 'furniture': 1,
 'rice': 0,
 'lentil': 0,
 'pollen': 0,
 'car': 0,
 'ball': 0,
 'kitchenware': 1,
 'jewelry': 1,
 'gravel': 0.0,
 'dust': 0.0,
 'equipment': 1,
 'bean': 0,
 'berry': 0,
 'seed': 0,
 'cabbage': 0}

scores_alt_log["C3"] = {'sand': 0.019049807777117844,
 'pebble': 0.16909315035632289,
 'chair': 0.04815155276578309,
 'apple': 0.581692719513718,
 'grape': 0.1328550521841847,
 'potato': 0.9166011013874353,
 'furniture': 0.0007991984860504786,
 'rice': 0.0020818072972381696,
 'lentil': 0.002430265016830857,
 'pollen': 0.06529437693950046,
 'car': 0.016617292210514667,
 'ball': 0.06554677813144949,
 'kitchenware': 0.024819125494844996,
 'jewelry': 0.0,
 'gravel': 0.0,
 'dust': 0.0,
 'equipment': 0.0,
 'bean': 0.7146363467302068,
 'berry': 0.22353618699102284,
 'seed': 0.0016688502978562392,
 'cabbage': 0.8105376416579552}

scores_weighted_alt_log = {}
scores_weighted_alt_log["C1"] = {}
scores_weighted_alt_log["C2"] = {}
scores_weighted_alt_log["C3"] = {}

for con in params:
    for noun in noun_list:
        scores_weighted_alt_log[con][noun] = params[con] * scores_alt_log[con][noun]
    
scores_agg_log = {}

for noun in noun_list:
    scores_agg_log[noun] = scores_weighted_alt_log["C1"][noun] + scores_weighted_alt_log["C2"][noun] + scores_weighted_alt_log["C3"][noun]


res_series_log = pd.Series(scores_agg_log)
desc_res_series_log = res_series_log.sort_values(ascending=False)

ordering = ''

for x in desc_res_series_log.index:
    if x != desc_res_series_log.index[-1]:
        ordering = ordering+str(x)+" > "
    else:
        ordering = ordering+str(x)
    
command_list = ['results', 'ordering', 'help']


print('List of commands:',command_list)

while True:
    s = input("Enter a command: ")
    if s == 'results':
        print(desc_res_series_log)
    elif s == 'ordering':
        print(ordering)
    else: 
        print('List of commands:',command_list) 



    


# In[12]:





# In[4]:





# In[ ]:




