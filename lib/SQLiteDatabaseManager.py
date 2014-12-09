#!/usr/bin/env python
# codeing = utf-8
# Author: Archer Reilly
# Date: 08/Dec/2014
# File: SQLiteDatabaseManager.py
# Desc: the management file for sqlite3
#
# Produced By CSRGXTU

#import sqlite3
from sqlite3 import connect

class SQLiteDatabaseManager(object):
  db = False
  cursor = False

  # initialize the database
  #
  # @param db string the database name
  def __init__(self, db):
    self.db = connect('../data/' + db)
    self.cursor = self.db.cursor()

    deadLinksSQL = "CREATE TABLE IF NOT EXISTS deadLinks(url TEXT \
                    PRIMARY KEY)"
    unvisitedLinksSQL = "CREATE TABLE IF NOT EXISTS unvisitedLinks(\
                    url TEXT PRIMARY KEY)"
    visitedLinksSQL = "CREATE TABLE IF NOT EXISTS visitedLinks(\
                    url TEXT PRIMARY KEY)"

    self.cursor.execute(deadLinksSQL)
    self.cursor.execute(unvisitedLinksSQL)
    self.cursor.execute(visitedLinksSQL)
    self.db.commit()
    #pass
  
  # close
  # close the connection to sqlite
  #
  # @return void
  def close(self):
    self.db.close()

  # createDeadLink
  # create a dead link record
  #
  # @param url string
  # @return boolean
  def createDeadLink(self, url):
    sql = "INSERT INTO deadLinks(url) VALUES(:url)"
    try:
      self.cursor.execute(sql, {"url": url})
      return True
    except:
      return False
    #pass

  # createDeadLinks
  # create multiple dead links records
  #
  # @param urls list(string)
  # @return boolean
  def createDeadLinks(self, urls):
    urls = [tuple([x]) for x in urls]
    sql = "INSERT INTO deadLinks(url) VALUES(:url)"
    try:
      self.cursor.executemany(sql, urls)
      self.db.commit()
      return True
    except:
      return False
    #pass

  # createUnvisitedLink
  # create an unvisited link in unvisitedLinks
  #
  # @param url string
  # @return boolean
  def createUnvisitedLink(self, url):
    sql = "INSERT INTO unvisitedLinks(url) VALUES(:url)"
    try:
      self.cursor.execute(sql, {"url": url})
      return True
    except:
      return False
    #pass

  # createUnvisitedLinks
  # create multiple unvisited links in unvisitedLinks
  #
  # @param urls list(string)
  # @return boolean
  def createUnvisitedLinks(self, urls):
    urls = [tuple([x]) for x in urls]
    sql = "INSERT INTO unvisitedLinks(url) VALUES(:url)"
    try:
      self.cursor.executemany(sql, urls)
      self.db.commit()
      return True
    except:
      return False
    #pass

  # createVisitedLink
  # create a visited link in visitedLinks
  #
  # @param url string
  # @return boolean
  def createVisitedLink(self, url):
    sql = "INSERT INTO visitedLinks(url) VALUES(:url)"
    try:
      self.cursor.execute(sql, {"url": url})
      return True
    except:
      return False
    #pass

  # createVisitedLinks
  # create multiple visited links records in visitedLinks
  #
  # @param urls list(string)
  # @return boolean
  def createVisitedLinks(self, urls):
    urls = [tuple([x]) for x in urls]
    sql = "INSERT INTO visitedLinks(url) VALUES(:url)"
    try:
      self.cursor.executemany(sql, urls)
      self.db.commit()
      return True
    except:
      return False
    #pass

  # readDeadLink
  # read a record from deadLinks
  #
  # @return url string or False
  def readDeadLink(self):
    sql = "SELECT url FROM deadLinks LIMIT 1"
    self.cursor.execute(sql)
    allRows = self.cursor.fetchall()
    if len(allRows) == 0:
      return False
    else:
      return allRows[0][0]
    #pass
  
  # readDeadLinks
  # read multiple records from deadLinks
  #
  # @param start int
  # @param offset int
  # @return urls list(string) or False
  def readDeadLinks(self, start, offset):
    sql = "SELECT url FROM deadLinks LIMIT " + str(start) + ", "\
          + str(offset)
    self.cursor.execute(sql)

    res = []
    for row in self.cursor.fetchall():
      res.append(row[0])

    if len(res) == 0:
      return False
    else:
      return res
    #pass

  # readUnvisitedLink
  # read a record from unvisitedLinks
  #
  # @return url string or False
  def readUnvisitedLink(self):
    sql = "SELECT url FROM unvisitedLinks LIMIT 1"
    self.cursor.execute(sql)
    allRows = self.cursor.fetchall()
    if len(allRows) == 0:
      return False
    else:
      return allRows[0][0]
    #pass

  # readUnvisitedLinks
  # read multiple records from unvisitedLinks
  #
  # @param start int
  # @param offset int
  # @return urls list(string) or False
  def readUnvisitedLinks(self, start, offset):
    sql = "SELECT url FROM unvisitedLinks LIMIT " + str(start) + ", "\
          + str(offset)
    self.cursor.execute(sql)

    res = []
    for row in self.cursor.fetchall():
      res.append(row[0])

    if len(res) == 0:
      return False
    else:
      return res
    #pass

  # readVisistedLink
  # read a record from visitedLinks
  #
  # @return url string or False
  def readVisitedLink(self):
    sql = "SELECT url FROM visitedLinks LIMIT 1"
    self.cursor.execute(sql)
    allRows = self.cursor.fetchall()
    if len(allRows) == 0:
      return False
    else:
      return allRows[0][0]
    #pass

  # readVisitedLinks
  # read multiple records from visitedLinks
  #
  # @param start int
  # @param offset int
  # @return urls list(string) or False
  def readVisitedLinks(self, start, offset):
    sql = "SELECT url FROM visitedLinks LIMIT " + str(start) + ", "\
          + str(offset)
    self.cursor.execute(sql)

    res = []
    for row in self.cursor.fetchall():
      res.append(row[0])

    if len(res) == 0:
      return False
    else:
      return res
    #pass

  # retrieveDeadLinks
  # retrieve records from deadLinks with delete operation
  #
  # @param start int
  # @param offset int
  # @return urls list(string) or False
  def retrieveDeadLinks(self, start, offset):
    urls = self.readDeadLinks(start, offset)
    if urls != False:
      self.deleteDeadLinks(urls)
    return urls
    #pass

  # retrieveUnvisitedLinks
  # retrieve records from unvisitedLinks with delete operation
  #
  # @param start int
  # @param offset int
  # @return urls list(string) or False
  def retrieveUnvisitedLinks(self, start, offset):
    urls = self.readUnvisitedLinks(start, offset)
    if urls != False:
      self.deleteUnvisitedLinks(urls)
    return urls
    #pass

  # retrieveVisitedLinks
  # retrieve records from visitedLinks with delte operation
  #
  # @param start int
  # @param offset int
  # @return urls list(string) or False
  def retrieveVisitedLinks(self, start, offset):
    urls = self.readVisitedLinks(start, offset)
    if urls != False:
      self.deleteVisitedLinks(urls)
    return urls
    #pass

  # updateDeadLink
  # update a record in deadLinks
  #
  # @param oldUrl string
  # @param newUrl string
  # @return boolean
  def updateDeadLink(self, oldUrl, newUrl):
    pass

  # updateDeadLinks
  # update multiple records in deadLinks
  #
  # @param urls dict(oldUrl:newUrl)
  # @return boolean
  def updateDeadLinks(self, urls):
    pass

  # updateUnvisitedLink
  # update a record in unvisitedLinks
  #
  # @param oldUrl string
  # @param newUrl string
  # @return boolean
  def updateUnvisitedLink(self, oldUrl, newUrl):
    pass
  
  # updateUnvisitedLinks
  # update multiple records in unvisitedLinks
  #
  # @param urls dict(oldUrl:newUrl)
  # @return boolean
  def updateUnvisitedLinks(self, urls):
    pass
  
  # updateVisitedLink
  # update a record in visitedLinks
  #
  # @param oldUrl string
  # @param newUrl string
  # @return boolean
  def updateVisitedLink(self, oldUrl, newUrl):
    pass
  
  # updateVisitedLinks
  # update multiple records in visitedLinks
  #
  # @param urls dict(oldUrl:newUrl)
  # @return boolean
  def updateVisitedLinks(self, urls):
    pass

  # deleteDeakLink
  # delete a record in deadLinks
  #
  # @param url string
  # @return boolean
  def deleteDeadLink(self, url):
    sql = "DELETE FROM deadLinks WHERE url = '" + url + "'"
    self.cursor.execute(sql)
    return True
    #pass
  
  # deleteDeadLinks
  # delete multiple records in deadLinks
  #
  # @param urls list(string)
  # @return boolean
  def deleteDeadLinks(self, urls):
    for url in urls:
      self.deleteDeadLink(url)
    return True
    #pass
  
  # deleteAllDeadLinks
  # empty the deadLinks table
  #
  # @return boolean
  def deleteAllDeadLinks(self):
    sql = "DELETE FROM deadLinks"
    self.cursor.execute(sql)
    return True
    #pass

  # deleteUnvisitedLink
  # delete a record in unvisitedLinks
  #
  # @param url string
  # @return boolean
  def deleteUnvisitedLink(self, url):
    sql = "DELETE FROM unvisitedLinks WHERE url = '" + url + "'"
    self.cursor.execute(sql)
    return True
    #pass

  # deleteUnvisitedLinks
  # delete multiple records in unvisitedLinks
  #
  # @param urls list(string)
  # @return boolean
  def deleteUnvisitedLinks(self, urls):
    for url in urls:
      self.deleteUnvisitedLink(url)
    return True
    #pass

  # deleteAllUnvisitedLinks
  # empty the unvisitedLinks table
  #
  # @return boolean
  def deleteAllUnvisitedLinks(self):
    sql = "DELETE FROM unvisitedLinks"
    self.cursor.execute(sql)
    return True
    #pass
  
  # deleteVisitedLink
  # delete a record in visitedLinks
  #
  # @param url string
  # @return boolean
  def deleteVisitedLink(self, url):
    sql = "DELETE FROM vistedLinks WHERE url = '" + url + "'"
    self.cursor.execute(sql)
    return True
    #pass

  # deleteVisitedLinks
  # delete multiple records in visitedLinks
  #
  # @param urls list(string)
  # @return boolean
  def deleteVisitedLinks(self, urls):
    for url in urls:
      self.deleteVisitedLink(url)
    return True
    #pass

  # deleteAllVisitedLinks
  # empty visitedLinks tables
  #
  # @return boolean
  def deleteAllVisitedLinks(self):
    sql = "DELETE FROM visitedLinks"
    self.cursor.execute(sql)
    return True
    #pass

  # isInDeadLink
  # check if an url in deadLinks
  #
  # @param url string
  # @return boolean
  def isInDeadLink(self, url):
    sql = "SELECT url FROM deadLinks WHERE url = '" + url + "'"
    self.cursor.execute(sql)
    allRows = self.cursor.fetchall()
    if len(allRows) == 0:
      return False
    else:
      return True
    #pass

  # isInUnvisitedLink
  # check if an url in unvisitedLinks
  #
  # @param url string
  # @return boolean
  def isInUnvisitedLink(self, url):
    sql = "SELECT url FROM unvisitedLinks WHERE url = '" + url + "'"
    self.cursor.execute(sql)
    allRows = self.cursor.fetchall()
    if len(allRows) == 0:
      return False
    else:
      return True
    #pass

  # isInVisitedLink
  # check if an url in visitedLinks
  #
  # @param url string
  # @return boolean
  def isInVisitedLink(self, url):
    sql = "SELECT url FROM visitedLinks WHERE url = '" + url + "'"
    self.cursor.execute(sql)
    allRows = self.cursor.fetchall()
    if len(allRows) == 0:
      return False
    else:
      return True
    #pass
