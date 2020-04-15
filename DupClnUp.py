#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:55:41 2020

@author: runyu
"""


import os,sys
import glob

dir = "/Users/runyu/Documents/Research/Template_Fit/v29starFits/"
os.chdir(dir)
dupFiles = glob.glob('**/* [0-9].*',recursive=True)
rootFiles = glob.glob('**/*.root',recursive=True)
print(len(dupFiles))
print(len(rootFiles))
#print(dupFiles[0].split('/')[-1])
for index,filename in enumerate(dupFiles):
    os.rename(dir+filename,"/Users/runyu/trash/"+filename.split('/')[-1]+ "_" +str(index))
#for index,filename in enumerate(rootFiles):
#    os.rename(dir+filename,"/Users/runyu/trash/"+filename.split('/')[-1]+ "_" +str(index))
   