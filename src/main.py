#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 09/Dec/2014
# File: main.py
# Desc: main program invokes all
#
# Produced By CSRGXTU
from ShadowWalker import ShadowWalker

db = 'ShadowWalker'
seedFile = '../data/seeds.txt'

sd = ShadowWalker(db, seedFile)
sd.walker()
