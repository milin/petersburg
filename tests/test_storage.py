#!/usr/bin/env python
#
#Copyright info here
#
#

import sys
sys.path.append("../lib")
import unittest
import getpass
import StorageLibrary as store

class Storage(unittest.TestCase):
   def setUp(self):
      self.data1 = {'username':'pinggoat','message':'hello world test 1',\
                     'location':'san francisco'}
      self.data2 = {'username':'himanshuc','message':'hello world test 2',
                     'location':'new york'}
      self.storage = store.CassandraStorage(column_family="Timeline")
      
   def test_store(self):
      self.storage.store(self.data1)
      self.storage.store(self.data2)

if __name__ == '__main__':
   unittest.main()
