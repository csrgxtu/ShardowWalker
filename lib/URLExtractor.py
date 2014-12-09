#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 09/Dec/2014
# File: URLExtractor.py
# Desc: class responsible get urls from any html file
#
# Produced By CSRGXTU
from BeautifulSoup import BeautifulSoup
from urlparse import urljoin

class URLExtractor(object):
  soup = False
  baseUrl = False

  # intialization the soup object
  #
  # @param html
  def __init__(self, html, baseUrl):
    try:
      self.soup = BeautifulSoup(html)
    except:
      self.soup = False
    self.baseUrl = baseUrl
  
  # getUrls
  # get all useful urls in the html
  #
  # @return urls list(string) or False
  def getUrls(self):
    if self.soup == False:
      return False

    urls = []

    for a in self.soup.findAll('a', href=True):
      urls.append(urljoin(self.baseUrl, a['href']))
    
    if len(urls) == 0:
      return False
    else:
      return urls
