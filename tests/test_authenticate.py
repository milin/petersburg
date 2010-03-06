#!/usr/bin/env python
#
#Copyright info here
#
#

import sys
sys.path.append("../")
import unittest
import getpass
import Ingest

class TestAuthentication(unittest.TestCase):
   def setUp(self):
      self.username = raw_input("enter username: ")
      self.password = getpass.getpass("enter password: ")
   
   def test_authenticate(self):
      x = Ingest.TwitterBasic()
      portal = x.authenticate(self.username, self.password)
      portal.update_status("hello world test from cscbot1")

if __name__ == '__main__':
   unittest.main()
