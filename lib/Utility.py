#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 09/Dec/2014
# File: Utility.py
# Desc: some useful functions here
#
# Produced By CSRGXTU

# loadLstFromFile
# load list from file, the file should one item per line
#
# @param inputFile
# @return res list(string)
def loadLstFromFile(inputFile):
  res = []

  with open(inputFile, 'r') as FH:
    for line in FH:
      res.append(line.rstrip())

  return res