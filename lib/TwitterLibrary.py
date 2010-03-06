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
import Logger as logger
import StorageLibrary as store

#Implements basic methods such as retrieving specific message
#or profile information.
class TwitterBasic:
   #Authenticates our twitter bot for streaming
   def authenticate(self,username,password):
      auth = tweepy.BasicAuthHandler(username,password)
      return tweepy.API(auth)

#Implements methods related to streaming of twitter data
class TwitterStream(tweepy.StreamListener):
   def __init(self):
      self.cassandra = store.CassandraStorage("Timeline")

   def on_status(self, status):
      try:
         #TODO: Connect hash to storage system
         logger.subsection("received new status")
         
      except:
         logger.subsection("WARN: status error")

   def on_error(self, status_code):
      logger.subsection("WARN: non-200 HTTP code returned "+ str(status_code))
      return True

   def on_timeout(self):
      logger.subsection("WARN: connection timeout")
      #TODO: attempt to reconnect

   def on_limit(self, track):
      logger.subsection("WARN: limit message encountered")


