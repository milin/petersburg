#!/usr/bin/env python
#
#Copyright info here
#
#

import sys
sys.path.append("../lib")
import unittest
import getpass
import TwitterLibrary

class TestAuthentication(unittest.TestCase):
   def setUp(self):
      self.username = raw_input("enter username: ")
      self.password = getpass.getpass("enter password: ")
   
   def test_authenticate(self):
      x = TwitterLibrary.TwitterBasic()
      portal = x.authenticate(self.username, self.password)
      portal.update_status("hello world, data is yummy")

if __name__ == '__main__':
   unittest.main()
