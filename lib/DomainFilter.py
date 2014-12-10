#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 09/Dec/2014
# File: DomainFilter.py
# Desc: filter domains
#
# Produced By CSRGXTU
from urlparse import urlparse

class DomainFilter(object):
  domain = False

  def __init__(self, domain):
    self.domain = domain.lower()

  # getFilteredUrls
  # get urls only in the domain
  #
  # @param urls list(string)
  # @return res list(string) or False
  def getFilteredUrls(self, urls):
    res = []

    for url in ulrs:
      if self.isInDomain(url):
        res.append(url)

    if len(res) == 0:
      return False
    else:
      return res

  # isInDomain
  # check if an url in domain
  #
  # @param url string
  # @return boolean
  def isInDomain(self, url):
    if urlparse(url.lower()).netloc.endswith(self.domain):
      return True
    else:
      return False
