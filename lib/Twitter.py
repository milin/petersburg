#! /usr/bin/env python
#
# Copyright (c) 2010 Okoye Chuka D.<okoye9@gmail.com>      
#                    All rights reserved.
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
 
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import tweepy
import getpass
import lib.Logger as logger

#Implements basic methods such as retrieving specific message
#or profile information.
class TwitterBasic:
   #Authenticates our twitter bot for streaming
   def authenticate(self,username,password):
      auth = tweepy.BasicAuthHandler(username,password)
      return tweepy.API(auth)
   
class TwitterStream(tweepy.StreamListener):
   def on_status(self, status):
      try:
         #TODO: Implement cassandra interface libs & logging mechanism
         logger.subsection("received new status")
      except:
         pass

   def on_error(self, status_code):
      #Call logging mechanism
      return True

   def on_timeout(self):
      #Call logging mechanism and attempt to reconnect

   def on_limit(self, track):
      #Call logging mechanism

