#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 02/Dec/2014
# File: DatabaseConfigParser.py
# Desc: responsible parse the data base connection configurations
# in conf/DatabaseConnections.ini
#
# Produced By CSRGXTU
from ConfigParser import ConfigParser

class DatabaseConfigParser(object):
  CONF_FILE = None
  CONF_OBJ = None

  # confFile: the configuration file path
  def __init__(self, confFile):
    if confFile is None:
      
    self.CONF_FILE = confFile
