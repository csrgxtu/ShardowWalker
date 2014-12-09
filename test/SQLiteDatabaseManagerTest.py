#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 09/Dec/2014
# File: SQLiteDatabaseManagerTest.py
# Desc: test class for SQLiteDatabaseManager
#
# Produced By CSRGXTU
import unittest
import sys
from os.path import dirname
sys.path.insert(0, dirname(__file__) + '../lib')

class SQLiteDatabaseManagerTest(unittest.TestCase):
  def setUp(self):
    self.fixture = range(1, 10)

  def tearDown(self):
    del self.fixture

  def test(self):
    self.assertEqual(self.fixture, range(1, 10))

if __name__ == '__main__':
  unittest.main()
