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
sys.path.insert(0, dirname(__file__) + '/../lib')
#print 'DEBUG: ', dirname(__file__) + '/../lib'

from Download import Download
from SQLiteDatabaseManager import SQLiteDatabaseManager
from URLExtractor import URLExtractor
from NonPlainFileFilter import NonPlainFileFilter
from DomainFilter import DomainFilter
from Utility import loadLstFromFile

class ShadowWalker(object):
  dbm = False
  urlFilter = False
  domainFilter = False

  # intialization database, load seed to unvisitedLinks table
  #
  # @param db string
  # @param seedFile string
  def __init__(self, db, seedFile):
    self.dbm = SQLiteDatabaseManager(db)

    urls = loadLstFromFile(seedFile)
    self.dbm.createUnvisitedLinks(urls)

    self.urlFilter = NonPlainFileFilter()

    self.domainFilter = DomainFilter('xtu.edu.cn')
  
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
          self.dbm.createDeadLink(url)
        else:
          self.dbm.createVisitedLink(url)
          u = URLExtractor(d.getSOURCE(), url)
          tmpUrls = u.getUrls()
          if tmpUrls:
            self.dbm.createUnvisitedLinks(list(set(tmpUrls)))

    return True

  # run
  # start actually walker
  #
  # @return True
  def run(self):
    while True:
      print 'INFO: ........................................ START'
      stats = self.dbm.getStats()
      print 'INFO: deadLinks-', stats[0], ' unvisitedLinks-', stats[1], ' visitedLinks-', stats[2]
      # get an url from unvisitedLinks
      url = self.dbm.retrieveUnvisitedLink()
      if url == False:
        print 'DEBUG: DONE -- retrieveUnvisitedLink return False'
        break

      print 'DEBUG: Processing ', url

      if not self.urlFilter.isPlainText(url):
        print 'DEBUG: NotPlainTextURL ', url
        continue
      
      if not self.domainFilter.isInDomain(url):
        print 'DEBUG: NOT IN DOMAIN ', url
        continue

      # requet the url
      d = Download(url)
      if d.doRequest() == 1:
        if not self.dbm.createDeadLink(url):
          print 'DEBUG: deadLinks already contain ', url
        else:
          print 'DEBUG: Add To deadLinks ', url
      else:
        if self.dbm.createVisitedLink(url):
          print 'DEBUG: Add To visitedLinks ', url
        else:
          print 'DEBUG: Failed Add To visitedLinks ', url

        # extract urls from the sourc2
        u = URLExtractor(d.getSOURCE(), url)
        tmpUrls = u.getUrls()
        if tmpUrls:
          for url in tmpUrls:
            if self.dbm.isInDeadLink(url):
              continue
            elif self.dbm.isInVisitedLink(url):
              continue
            elif self.dbm.isInUnvisitedLink(url):
              continue
            else:
              print 'DEBUG: Add To unvisitedLink ', url
              self.dbm.createUnvisitedLink(url)
    
      print 'INFO: ........................................ END'
