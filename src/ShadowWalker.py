#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 09/Dec/2014
# File: ShadowWalker.py
# Desc: walker that walks through the internet until tired or
# done
#
# Produced By CSRGXTU
import sys
from os.path import dirname
sys.path.insert(0, dirname(__file__) + '../lib')

from Utility import loadLstFromFile
from Download import Download
from SQLiteDatabaseManager import SQLiteDatabaseManager
from URLExtractor import URLExtractor
from NonPlainFileFilter import NonPlainFileFilter

class ShadowWalker(object):
  dbm = False
  urlFilter = False

  # intialization database, load seed to unvisitedLinks table
  #
  # @param db string
  # @param seedFile string
  def __init__(self, db, seedFile):
    self.dbm = SQLiteDatabaseManager(db)

    urls = loadLstFromFile(seedFile)
    self.dbm.createUnvisitedLinks(urls)

    self.urlFilter = NonPlainFileFilter()
  
  # walker
  # start actually walker
  #
  # @return True
  def walker(self):
    while True:
      urls = self.dbm.retrieveUnvisitedLinks(0, 100)
      urls = self.urlFilter.getFilteredUrls(urls)
      if len(urls) == 0:
        break

      for url in urls:
        print 'INFO: Processing ', url
        d = Download(url)
        if d.doRequest() == 1:
          self.dbm.createDeadLink(url):
        else:
          self.dbm.createVisitedLink(url)
          u = URLExtractor(d.getSOURCE(), url)
          tmpUrls = u.getUrls()
          if tmpUrls:
            self.dbm.createUnvisitedLinks(list(set(tmpUrls)))

    return True
