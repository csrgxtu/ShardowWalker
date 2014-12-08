#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 2/Dec/2014
# File: RedisDatabaseManager.py
# Desc: manages the database storage, mainly urls for
# visited unvisisted dead in Redis storage.
#
# Produced By CSRGXTU
import redis
from redis import StrictRedis

class RedisDatabaseManager(object):
  redisHandler = None

  # initialization, establish connection to redis server
  #
  # @param host string host of the redis server
  # @param port int port of the redis server
  # @param db int database you want to use in redis server
  def __init__(self, host, port, db):
    self.redisHandler = StrictRedis(host=host, port=port, db=db)

    # create deadLinks, unvisistedLinks, visitedLinks in redis
    self.redisHandler.ltrim('deadLinks', -1, 0)
    self.redisHandler.ltrim('unvisitedLinks', -1, 0)
    self.redisHandler.ltrim('visitedLinks', -1, 0)

  # createDeadLinks
  # create a record in deadLinks list
  #
  # @param url string
  # @return boolean
  def createDeadLinks(self, url):
    pass

  # readDeadLinks
  # 

